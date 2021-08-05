import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import sys
os.environ['QT_API'] = 'pyside2'
import matplotlib
print(matplotlib.get_backend())
matplotlib.use("module://ipykernel.pylab.backend_inline")
import matplotlib.pyplot as plt

import win_cap_thread
import win_app_model
import time_log
import win_capture
import win_cap_item

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QObject, QUrl
from PySide2 import QtQml, QtCore
import traceback
import time


class WinAppMainAction(QObject):
    def __init__(self, parent=None):
        super(WinAppMainAction, self).__init__(parent)

    @QtCore.Slot(str)
    def play(self, url):
        time_log.time_log(url)
        file = url[8:]
        time_log.time_log(file)
        for capture in win_capture.cv_captures:
            capture.set_url(file)
            capture.start()


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    QtQml.qmlRegisterType(win_capture.CVCapture, "PyCVQML", 1, 0, "CVCapture")
    QtQml.qmlRegisterType(win_cap_item.CVItem, "PyCVQML", 1, 0, "CVItem")
    QtQml.qmlRegisterType(WinAppMainAction, "PyCVQML", 1, 0, "CVAction")

    engine = QQmlApplicationEngine(parent=app)

    context = engine.rootContext()
    context.setContextProperty("data_model", win_app_model.win_app_data_model)

    engine.load(QUrl('win_qml.qml'))

    win = engine.rootObjects()[0]
    win_cap_thread.detect_run()
    rc = app.exec_()
    try:
        win_capture.cv_capture_enable = False
        win_cap_thread.detect_stop()
        for capture in win_capture.cv_captures:
            capture.stop()
        # win_capture.m_mask_rcnn.close_session()
        for capture in win_capture.cv_captures:
            capture.stop()
    except:
        traceback.print_exc()
    plt.close("all")
    time_log.time_log(rc)
    time.sleep(1)
    sys.exit(rc)
