import numpy
import time_log
import cv2

from PySide2 import QtCore, QtGui, QtQml

gray_color_table = [QtGui.qRgb(i, i, i) for i in range(256)]


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
        self._image = QtGui.QImage()
        self._index = 0
        self._interval = 0
        self._cap_type = ""
        self._url = ""

        self.m_videoCapture = cv2.VideoCapture()
        self.m_timer = QtCore.QBasicTimer()
        self.m_filters = []
        self.m_busy = False

    @QtCore.Slot()
    @QtCore.Slot(int)
    def start(self, *args):
        # if args:
        #     self.setIndex(args[0])
        self.m_videoCapture.release()
        if self.capType == "index":
            self.m_videoCapture = cv2.VideoCapture(self.index)
        elif self.capType == "url":
            self.m_videoCapture = cv2.VideoCapture(self.url)
        if self.m_videoCapture.isOpened():
            self.m_timer.start(self.interval, self)
            self.started.emit()

    @QtCore.Slot()
    def stop(self):
        self.m_timer.stop()

    def timerEvent(self, e):
        if e.timerId() != self.m_timer.timerId():
            return
        ret, frame = self.m_videoCapture.read()
        if not ret:
            self.m_timer.stop()
            return
        if not self.m_busy:
            self.process_image(frame)
            # threading.Thread(target=self.process_image, args=(numpy.copy(frame),)).start()

    @QtCore.Slot(numpy.ndarray)
    def process_image(self, frame):
        time_log.time_log("process_image")
        self.m_busy = True
        for f in self.m_filters:
            frame = f.process_image(frame)
        image = CVCapture.ToQImage(frame)
        self.m_busy = False
        QtCore.QMetaObject.invokeMethod(self,
                                        "set_image",
                                        QtCore.Qt.AutoConnection,
                                        QtCore.QGenericArgument("QImage", image))

    @staticmethod
    def ToQImage(im):
        if im is None:
            return QtGui.QImage()
        if im.dtype == numpy.uint8:
            if len(im.shape) == 2:
                qim = QtGui.QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QtGui.QImage.Format_Indexed8)
                qim.setColorTable(gray_color_table)
                return qim.copy()

            elif len(im.shape) == 3:
                if im.shape[2] == 3:
                    w, h, _ = im.shape
                    rgb_image = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
                    flip_image = cv2.flip(rgb_image, 1)
                    qim = QtGui.QImage(flip_image.data, h, w, QtGui.QImage.Format_RGB888)
                    return qim.copy()
        return QtGui.QImage()

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

    def get_interval(self):
        return self._interval

    def set_interval(self, value):
        self._interval = value

    def get_cap_type(self):
        return self._cap_type

    def set_cap_type(self, value):
        self._cap_type = value

    def get_url(self):
        return self._url

    def set_url(self, value):
        self._url = value

    def append_filter(self, sub):
        self.m_filters.append(sub)

    def get_filters(self):
        return self.m_filters

    filters = QtQml.ListProperty(CVAbstractFilter, append_filter)

    image = QtCore.Property(QtGui.QImage, fget=get_image, notify=imageReady)
    index = QtCore.Property(int, fget=get_index, fset=set_index, notify=indexChanged)
    interval = QtCore.Property(int, fget=get_interval, fset=set_interval)
    capType = QtCore.Property(str, fget=get_cap_type, fset=set_cap_type)
    url = QtCore.Property(str, fget=get_url, fset=set_url)
