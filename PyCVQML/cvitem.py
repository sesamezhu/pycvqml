from PySide2 import QtCore, QtGui, QtQuick


class CVItem(QtQuick.QQuickPaintedItem):
    imageChanged = QtCore.Signal()

    def __init__(self, parent=None):
        super(CVItem, self).__init__(parent)
        self.column_no = 0
        self.m_image = QtGui.QImage()

    def next_column_no(self):
        self.column_no = (self.column_no + 1) % 2
        return self.column_no

    def paint(self, painter):
        image = self.m_image
        if image.isNull():
            return
        size = QtCore.QSize(self.width(), self.height())
        image = image.scaled(size)
        painter.drawImage(0, 0, image)

    def get_image(self):
        return self.m_image

    def set_image(self, image):
        if self.m_image == image:
            return
        self.m_image = image
        self.imageChanged.emit()
        self.update()

    image = QtCore.Property(QtGui.QImage, fget=get_image, fset=set_image, notify=imageChanged)
