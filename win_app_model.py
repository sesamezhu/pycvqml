from PySide2 import QtCore
from PySide2.QtCore import QObject

import win_config
import cv2
import win_cap_utils


class WinAppModel(QObject):
    def __init__(self, parent=None):
        super(WinAppModel, self).__init__(parent)
        self.m_cuda = self.read_config("cuda", True)
        self.m_continuous = self.read_config("continuous", True)
        
        self.m_rcnn = self.read_config("rcnn", True)
        self.m_gray = self.read_config("gray", False)
        self.m_gaussian = self.read_config("gaussian", False)
        self.m_mean = self.read_config("mean", False)
        self.m_hist = self.read_config("hist", False)
        self.m_scale_up = self.read_config("scale_up", False)
        self.m_scale_down = self.read_config("scale_down", False)
        
        self.m_sec_last = 0
        self.m_mask_last = 0
        self.m_timer_last = 0 # 统计每秒计数的定时器id

    def get_cuda(self):
        return self.m_cuda

    def set_cuda(self, value):
        self.m_cuda = value
        win_config.save_config("cuda", value)

    def get_rcnn(self):
        return self.m_rcnn

    def set_rcnn(self, value):
        self.m_rcnn = value
        win_config.save_config("rcnn", value)

    def get_continuous(self):
        return self.m_continuous

    def set_continuous(self, value):
        self.m_continuous = value
        win_config.save_config("continuous", value)

    def get_enable_filters(self):
        return self.m_gray or self.m_gaussian or self.m_mean or self.m_hist or self.m_scale_up or self.m_scale_down

    def get_gaussian(self):
        return self.m_gaussian

    def set_gaussian(self, value):
        self.m_gaussian = value
        win_config.save_config("gaussian", value)

    def get_mean(self):
        return self.m_mean

    def set_mean(self, value):
        self.m_mean = value
        win_config.save_config("mean", value)

    def get_hist(self):
        return self.m_hist

    def set_hist(self, value):
        self.m_hist = value
        win_config.save_config("hist", value)

    def get_scale_up(self):
        return self.m_scale_up

    def set_scale_up(self, value):
        self.m_scale_up = value
        win_config.save_config("scale_up", value)

    def get_scale_down(self):
        return self.m_scale_down

    def set_scale_down(self, value):
        self.m_scale_down = value
        win_config.save_config("scale_down", value)
        
    def get_gray(self):
        return self.m_gray

    def set_gray(self, value):
        self.m_gray = value
        win_config.save_config("gray", value)
        
    def get_sec_last(self):
        return self.m_sec_last
    
    def set_sec_last(self, value):
        self.m_sec_last = value
    
    def get_mask_last(self):
        return self.m_mask_last
    
    def set_mask_last(self, value):
        self.m_mask_last = value


    cuda = QtCore.Property(bool, fget=get_cuda, fset=set_cuda)
    continuous = QtCore.Property(bool, fget=get_continuous, fset=set_continuous)
    rcnn = QtCore.Property(bool, fget=get_rcnn, fset=set_rcnn)
    
    gaussian = QtCore.Property(bool, fget=get_gaussian, fset=set_gaussian)
    mean = QtCore.Property(bool, fget=get_mean, fset=set_mean)
    hist = QtCore.Property(bool, fget=get_hist, fset=set_hist)
    scaleUp = QtCore.Property(bool, fget=get_scale_up, fset=set_scale_up)
    scaleDown = QtCore.Property(bool, fget=get_scale_down, fset=set_scale_down)
    gray = QtCore.Property(bool, fget=get_gray, fset=set_gray)
    secLast = QtCore.Property(int, fget=get_sec_last, fset=set_sec_last)
    maskLast = QtCore.Property(int, fget=get_mask_last, fset=set_mask_last)

    def read_config(self, key, default):
        value = win_config.read_config(key)
        if value is None:
            return default
        else:
            return value
    
    def cv2_filter(self, frame):
        if self.get_enable_filters():
            frame = cv2.cvtColor(frame, win_cap_utils.get2GrayType(frame.shape))
        if self.m_gaussian:
            frame = cv2.adaptiveThreshold(
                frame,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                cv2.THRESH_BINARY,7,2)
        if self.m_mean:
            frame = cv2.adaptiveThreshold(
                frame,255,cv2.ADAPTIVE_THRESH_MEAN_C,
                cv2.THRESH_BINARY,7,2)
        if self.m_hist:
            frame = cv2.equalizeHist(frame)
        if self.m_scale_up:
            frame = cv2.convertScaleAbs(frame, alpha=2, beta=25)
        if self.m_scale_down:
            frame = cv2.convertScaleAbs(frame, alpha=2, beta=-50)
        return frame
    
win_app_data_model = WinAppModel()

