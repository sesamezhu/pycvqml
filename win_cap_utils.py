# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 16:39:41 2021

@author: zhugh
"""
import cv2
from PySide2 import QtGui
import numpy


gray_color_table = [QtGui.qRgb(i, i, i) for i in range(256)]


def get_color_len(shape):
    if len(shape) == 3:
        return shape[2]
    else:
        return 1

def get2GrayType(shape):
    color_len = get_color_len(shape)
    if color_len == 3:
        return cv2.COLOR_BGR2GRAY
    if color_len == 4:
        return cv2.COLOR_BGRA2GRAY
    return None

def ToQImage(im):
    if im is None:
        return QtGui.QImage()
    if im.dtype == numpy.uint8:
        if len(im.shape) == 2:
            qim = QtGui.QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QtGui.QImage.Format_Indexed8)
            qim.setColorTable(gray_color_table)
            return qim.copy()

        elif len(im.shape) == 3:
            # time_log.time_log("toQImage:{}-{}-{}".format(
                              # im.shape[0],im.shape[1],im.shape[2]))
            if im.shape[2] == 3:
                w, h, _ = im.shape
                # rgb_image = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
                # flip_image = cv2.flip(rgb_image, 1)
                qim = QtGui.QImage(im.data, h, w, QtGui.QImage.Format_RGB888)
                return qim.copy()
            elif im.shape[2] == 4:
                w, h, _ = im.shape
                rgb_image = cv2.cvtColor(im, cv2.COLOR_BGRA2RGB)
                flip_image = cv2.flip(rgb_image, 1)
                qim = QtGui.QImage(flip_image, h, w, QtGui.QImage.Format_RGB888)#RGBA8888)
                return qim.copy()

    return QtGui.QImage()