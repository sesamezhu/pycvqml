import os
import sys

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QObject, QUrl
from PySide2 import QtQml, QtCore
import traceback
import time

global app
app = QGuiApplication(sys.argv)

def main():
    # QtQml.qmlRegisterType(win_capture.CVCapture, "PyCVQML", 1, 0, "CVCapture")
    # QtQml.qmlRegisterType(win_cap_item.CVItem, "PyCVQML", 1, 0, "CVItem")
    # QtQml.qmlRegisterType(win_cap_item.CVLayout, "PyCVQML", 1, 0, "CVLayout")
    # QtQml.qmlRegisterType(WinAppMainAction, "PyCVQML", 1, 0, "CVAction")
    global app
    engine = QQmlApplicationEngine(parent=app)

    context = engine.rootContext()
    # context.setContextProperty("data_model", win_app_model.win_app_data_model)

    engine.load(QUrl('test_qml.qml'))

    win = engine.rootObjects()[0]
    rc = app.exec_()
    print(rc)
    print(sys.argv)
    # sys.exit(rc)
    

if __name__ == "__main__":
    # app = QGuiApplication(sys.argv)
    main()
