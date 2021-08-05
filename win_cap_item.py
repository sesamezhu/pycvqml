from PySide2 import QtCore, QtGui, QtQuick
from PySide2.QtGui import QColor
from PySide2.QtCore import QObject
import time_log

# cv_cap_items = []

class CVItem(QtQuick.QQuickPaintedItem):
    imageChanged = QtCore.Signal()

    def __init__(self, parent=None):
        super(CVItem, self).__init__(parent)
        self.m_desc = ""
        self.m_image = QtGui.QImage()
        # cv_cap_items.append(self)

    def paint(self, painter):
        image = self.m_image
        if not image or image.isNull():
            return
        size = QtCore.QSize(self.width(), self.height())
        image = image.scaled(size)
        painter.drawImage(0, 0, image)
        painter.fillRect(10, 10, 140, 30, QColor(222, 222, 222))
        # font = painter.font()
        # font.setBold(True)
        # font.setPointSize(16)
        # painter.setFont(font)
        # painter.drawText(10, 10, 140, 30, 0x84, self.m_desc)

    def get_image(self):
        return self.m_image

    def set_image(self, image):
        if self.m_image == image:
            return
        self.m_image = image
        self.imageChanged.emit()
        self.update()
        
    def get_desc(self):
        return self.m_desc
    
    def set_desc(self, value):
        self.m_desc = value

    image = QtCore.Property(QtGui.QImage, fget=get_image, fset=set_image, notify=imageChanged)
    desc = QtCore.Property(str, fget=get_desc, fset=set_desc)
