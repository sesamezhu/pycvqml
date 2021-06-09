import cv2
import numpy as np
from PySide2 import QtGui, QtCore, QtQuick, QtQml
import PyCVQML
import time_log

QML_FILE_NAME = "pycv.qml"


def qml_source():
    __dir_path = os.path.dirname(os.path.realpath(__file__))
    __qml_path = QtCore.QDir(__dir_path).absoluteFilePath(QML_FILE_NAME)
    print(__qml_path)
    return QtCore.QUrl.fromLocalFile(__qml_path)


def max_rgb_filter(image):
    time_log.time_log("max_rgb_filter")
    # split the image into its BGR components
    (B, G, R) = cv2.split(image)

    # find the maximum pixel intensity values for each
    # (x, y)-coordinate,, then set all pixel values less
    # than M to zero
    M = np.maximum(np.maximum(R, G), B)
    R[R < M] = 0
    G[G < M] = 0
    B[B < M] = 0

    # merge the channels back together and return the image
    return cv2.merge([B, G, R])


def rgb_to_gray(image):
    time_log.time_log("rgb_to_gray")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray


class MaxRGBFilter(PyCVQML.CVAbstractFilter):
    def process_image(self, src):
        time_log.time_log("MaxRGBFilter")
        return max_rgb_filter(src)


class GrayFilter(PyCVQML.CVAbstractFilter):
    def process_image(self, src):
        time_log.time_log("GrayFilter")
        return rgb_to_gray(src)


if __name__ == '__main__':
    import os
    import sys

    app = QtGui.QGuiApplication(sys.argv)

    PyCVQML.registerTypes()
    QtQml.qmlRegisterType(MaxRGBFilter, "Filters", 1, 0, "MaxRGBFilter")
    QtQml.qmlRegisterType(GrayFilter, "Filters", 1, 0, "GrayFilter")

    view = QtQuick.QQuickView()
    view.setTitle("炼钢厂天车挂钩检测系统")
    item = view.rootObject()
    view.setSource(qml_source())

    view.show()
    sys.exit(app.exec_())
