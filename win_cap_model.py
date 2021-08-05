from PySide2 import QtCore
from PySide2.QtCore import QObject

global win_cap_model_index
win_cap_model_index = 0


class WinCapModel(QObject):
    def __init__(self, parent=None):
        super(WinCapModel, self).__init__(parent)
        global win_cap_model_index
        win_cap_model_index += 1
        self.m_cap_type = str(win_cap_model_index)
        self.m_cap_url = ""

    def get_cap_type(self):
        return self.m_cap_type

    def set_cap_type(self, value):
        self.m_cap_type = value

    def get_cap_url(self):
        return self.m_cap_url

    def set_cap_url(self, value):
        self.m_cap_url = value

    cap_type = QtCore.Property(str, fget=get_cap_type, fset=set_cap_type)
    cap_url = QtCore.Property(str, fget=get_cap_url, fset=set_cap_url)
