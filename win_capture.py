import numpy
import time_log
import cv2
from PySide2 import QtCore, QtGui
# import mask_rcnn
import win_cuda_capture
import win_app_model
import win_cap_utils
import logging
from concurrent.futures import ThreadPoolExecutor
import traceback
import time
import datetime

cv_captures = []
global cv_cap_index
cv_cap_index = 0
global cv_read_index
cv_read_index = 0
global cv_capture_enable
cv_capture_enable = True
# global cuda_device_index
# cuda_device_index = 0
    # global cuda_device_index
    # cuda_device_index += 1
    # cuda_device_index %= 2
    # time_log.time_log("cuda_device_index:{}".format(cuda_device_index))
    # cv2.cuda.setDevice(cuda_device_index)
# cv2.cuda.setDevice(1)
capture_executor = ThreadPoolExecutor(max_workers=4)

# m_mask_rcnn = mask_rcnn.MASK_RCNN()


def get_indexed_capture():
    if len(cv_captures) == 0:
        return None
    global cv_cap_index
    cv_cap_index = (cv_cap_index + 1) % len(cv_captures)
    return cv_captures[cv_cap_index]

def read_next_capture():
    if len(cv_captures) == 0:
        time_log.time_log("read failure for empty captures")
        return False
    global cv_read_index
    cv_read_index = (cv_read_index + 1) % len(cv_captures)
    cap = cv_captures[cv_read_index]
    if cap._reading:
        time_log.time_log("read failure for reading already")
        return False
    # elapse = datetime.datetime.now() - cap._start_time
    # if elapse.total_seconds() > 300:
    #     time_log.time_log("started elapse:{}".format(elapse))
    #     cap.start()
    if not cap.m_videoCapture.isOpened():
        time_log.time_log("read failure for closed")
        return False
    
    cap._reading = True
    try:
        if cap.do_read_cap():
            return True
        else:
            time_log.time_log("read failure")
            return False
    except:
        traceback.print_exc()
        return False
    finally:
        #reset reading flag
        cap._reading = False

def capture_threading():
    while cv_capture_enable:
        ret = False
        try:
            ret = read_next_capture()
        except:
            traceback.print_exc()
        if not ret:
            time.sleep(0.002)


class CVAbstractFilter(QtCore.QObject):
    def process_image(self, src):
        dst = src
        return dst


class CVCapture(QtCore.QObject):
    started = QtCore.Signal()
    imageReady = QtCore.Signal()
    indexChanged = QtCore.Signal()

    def __init__(self, parent=None):
        super(CVCapture, self).__init__(parent)
        print("CVCapture__init__")
        self._image = QtGui.QImage()
        self._index = 0
        self._cap_type = ""
        self._url = ""
        self._read_total = 0 #图像读取总计数
        self._sec_count = 0
        self._sec_last = 0
        self._mask_total = 0
        self._mask_count = 0
        self._mask_last = 0
        self._reading = False
        self._detecting = False
        self._start_time = datetime.datetime.now()
        self._failure_total = 0
        self._error_total = 0

        self.m_videoCapture = cv2.VideoCapture()
        sec_timer = QtCore.QBasicTimer()
        self.m_sec_timer = sec_timer
        # self.m_timer = QtCore.QBasicTimer()
        # self.m_timer.start(50, self)
        self.m_raw_data = numpy.ndarray(numpy.shape(0))
                
        global cv_captures
        cv_captures.append(self)
        if len(cv_captures) == 1:
            # 仅限第一个定时器做计数统计
            sec_timer.start(1000, self)
            win_app_model.win_app_data_model.m_timer_last = sec_timer.timerId()
            time_log.time_log("sec-timeId:" + str(sec_timer.timerId()))
        
    @QtCore.Slot()
    @QtCore.Slot(int)
    def start(self, *args):
        self.m_videoCapture.release()
        if self.capType == "index":
            self.m_videoCapture = cv2.VideoCapture(self.index)
        else:
            if win_app_model.win_app_data_model.m_cuda:
                self.m_videoCapture = win_cuda_capture.CudaCap(self.url)
            else:
                self.m_videoCapture = cv2.VideoCapture(self.url)
        self._start_time = datetime.datetime.now()
        if self.m_videoCapture.isOpened():
            capture_executor.submit(self.while_read_cap)
            self.started.emit()
            time_log.time_log(self._url + " started")

    @QtCore.Slot()
    def stop(self):
        self.m_videoCapture.release()
        # self.m_timer.stop()
        
    def while_read_cap(self):
        while cv_capture_enable and self.m_videoCapture.isOpened():
            ret = False
            try:
                ret, frame = self.m_videoCapture.read()
            except:
                traceback.print_exc()
                self._error_total += 1
                time.sleep(0.5)
                continue
            if ret:
                self.m_raw_data = frame
                self.update_count()
            else:
                capture_logger.warn("read failed: " + str(ret))
                self._failure_total += 1
                time.sleep(0.1)
            
    def do_read_cap(self):
        ret, frame = self.m_videoCapture.read()
        if ret:
            self.m_raw_data = frame
            self.update_count()
        else:
            capture_logger.warn("read failed: " + str(ret))
            if win_app_model.win_app_data_model.continuous:
                self.start()
            time.sleep(0.5)
        return ret

    def timerEvent(self, e):
        self.calc_last(e)
        # if e.timerId() != self.m_timer.timerId():
        #     return
        # if self._sec_last <= 0:
        #     return
        # frame = self.m_raw_data
        # if win_app_model.win_app_data_model.m_rcnn:
        #     if win_cap_utils.get_color_len(frame.shape) == 4:
        #         frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGB)
        #         frame = cv2.flip(frame, 1)
                
        #     time_log.time_log("detecting.no-{}-{}".format(
        #         self._read_total, self._mask_total))
        #     try:
        #         frame = m_mask_rcnn.detect_image(frame)
        #     except:
        #         traceback.print_exc()
        #     time_log.time_log("detectedddddd.no-{}".format(
        #         self._read_total))
        #     self._mask_count += 1
        #     self._mask_total += 1
        #     self.process_image(frame)
        # else:
        #     frame = win_app_model.win_app_data_model.cv2_filter(frame)
        #     self.process_image(frame)

    def update_count(self):
        self._read_total += 1
        self._sec_count += 1

    @QtCore.Slot(numpy.ndarray)
    def process_image(self, frame):
        image = win_cap_utils.ToQImage(frame)
        QtCore.QMetaObject.invokeMethod(self,
                                        "set_image",
                                        QtCore.Qt.AutoConnection,
                                        QtCore.QGenericArgument("QImage", image))
        
    def calc_last(self, e):
        if e.timerId() != win_app_model.win_app_data_model.m_timer_last:
            return
        sec_total = 0
        mask_total = 0
        error_total = 0
        failure_total = 0
        for cap in cv_captures:
            cap._sec_last = cap._sec_count
            cap._sec_count = 0
            sec_total += cap._sec_last
            
            cap._mask_last = cap._mask_count
            cap._mask_count = 0
            mask_total += cap._mask_last
            
            error_total += cap._error_total
            failure_total += cap._failure_total
        win_app_model.win_app_data_model.m_sec_last = sec_total
        win_app_model.win_app_data_model.m_mask_last = mask_total
        time_log.time_log("sec:{},mask:{},error:{},fail:{}"
                          .format(sec_total, mask_total, error_total, failure_total))

    def get_image(self):
        return self._image

    @QtCore.Slot(QtGui.QImage)
    def set_image(self, image):
        if self._image == image:
            return
        self._image = image
        self.imageReady.emit()

    def get_index(self):
        return self._index

    def set_index(self, value):
        if self._index == value:
            return
        self._index = value
        self.indexChanged.emit()

    def get_cap_type(self):
        return self._cap_type

    def set_cap_type(self, value):
        self._cap_type = value

    def get_url(self):
        return self._url

    def set_url(self, value):
        self._url = value
     
    def get_sec_last(self):
        return self._sec_last
    
    def get_mask_last(self):
        return self._mask_last
    
    # def append_filter(self, sub):
    #     self.m_filters.append(sub)

    # def get_filters(self):
    #     return self.m_filters
    
    # def set_filters(self, value):
    #     self.m_filters = value

    # filters = QtQml.ListProperty(CVAbstractFilter, append_filter)
    # filters = QtCore.Property(str, fget=get_filters, fset=set_filters)

    image = QtCore.Property(QtGui.QImage, fget=get_image, notify=imageReady)
    index = QtCore.Property(int, fget=get_index, fset=set_index, notify=indexChanged)
    capType = QtCore.Property(str, fget=get_cap_type, fset=set_cap_type)
    url = QtCore.Property(str, fget=get_url, fset=set_url)
    secLast = QtCore.Property(int, fget=get_sec_last)
    maskLast = QtCore.Property(int, fget=get_mask_last)
    
capture_logger = logging.getLogger(__name__)
# capture_executor.submit(capture_threading)
# capture_executor.submit(capture_threading)
