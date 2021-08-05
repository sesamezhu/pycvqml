from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QToolTip,QLabel
from gangtie import Ui_MainWindow
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QFont, QImage
from PyQt5.QtCore import QTimer, QDateTime
import cv2
import os
import sys

style1 = '''
         QPushButton{
         border-image:url('./images/按钮.png')
         }
          QPushButton:Clicked{border-image: url('./images/按钮1.png')}
          
QPushButton{font-family:'黑体';font-size:16px;color:white;}
'''
style2 = '''
QPushButton{
         border-image:url('./images/按钮1.png')
         }
         QPushButton{font-family:'黑体';font-size:16px;color:white;}
'''
dingweiButton="1#监控位"

class Test(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Test, self).__init__(parent)
        self.labeldeng = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17]
        self.setupUi(self)

        desktopsize = QApplication.desktop()
        self.setFixedSize(desktopsize.width(), desktopsize.height() - 80)
        self.timer = QTimer(self)
        self.video_timer = QTimer(self)
        time = QDateTime.currentDateTime()
        # 设置系统时间显示格式
        timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd");
        # 在标签上显示时间
        self.cap =cv2.VideoCapture("./VID9.mp4")
        self.labeltime.setText(timeDisplay)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
        self.label.setGeometry(40, 110, 900, 360)
        self.label1.setGeometry(40, 490, 900, 360)
        self.label2.setGeometry(960, 110, 900, 360)
        self.label3.setGeometry(960, 490, 900, 360)
        '''
        self.label4.setGeometry(660, 340, 600, 250)
        self.label5.setGeometry(1280, 340, 600, 250)
        self.label6.setGeometry(40, 600, 600, 250)
        self.label7.setGeometry(660, 600, 600, 250)
        self.label8.setGeometry(1280, 600, 600, 250)
        '''
        self.labelhen.setGeometry(40, 890, 1840, 5)
        self.pushButton1.setGeometry(1500, 925, 140, 40)
        self.pushButton1.setStyleSheet(style2)
        self.pushButton1.clicked.connect(self.show_vis)
        self.pushButton2.setGeometry(1700, 925, 140, 40)
        self.pushButton2.setStyleSheet(style1)
        self.pushButton2.clicked.connect(self.show_vis)
        '''
        self.pushButton3.setGeometry(1700, 925, 140, 40)
        self.pushButton3.setStyleSheet(style1)
        '''
        self.labeltuoyuan1.setGeometry(1370, 910, 10, 10)
        self.labeltuoyuan2.setGeometry(1570, 910, 10, 10)
        self.labeltuoyuan3.setGeometry(1770, 910, 10, 10)
        print(self.labeltuoyuan3.x())
        print(self.labeltuoyuan3.width())

        #self.pushButton3.clicked.connect(lambda: buttonpress(self))
        self.pushButton2.clicked.connect(lambda: buttonpress(self))
        self.pushButton1.clicked.connect(lambda: buttonpress(self))
    def showTime(self):
        # 获取系统现在的时间
        time = QDateTime.currentDateTime()
        # 设置系统时间显示格式
        timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd");
        # 在标签上显示时间
        self.labeltime.setText(timeDisplay)

    def show_vis(self):
        self.video_timer.timeout.connect(self.show_vid)
    
    def show_vid():
        flag,img = self.cap.read()
        if flag:
            img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            img = QImage(img.data,img.shape[1],img.shape[0],QImage.Format_BGR888)
            self.label.setPixmap(QPixmap.fromImage(img))
        else:
            self.cap.release()
            self.video_timer.stop()



def buttonpress(self):
    sender = self.sender()
    clickevent = sender.text()
    global dingweiButton
    if(clickevent!=dingweiButton):

        if (clickevent == "1#监控位"):
            self.pushButton1.setStyleSheet(style2)
            self.pushButton2.setStyleSheet(style1)

        else:
            self.pushButton1.setStyleSheet(style1)
            self.pushButton2.setStyleSheet(style2)

        dingweiButton=clickevent



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Test()
    ui.setWindowTitle("展示界面")
    desktop = QApplication.desktop()
    print("屏幕宽:" + str(desktop.width()))
    print("屏幕高:" + str(desktop.height()))

    ui.setStyleSheet("border-image:url(./images/整体背景.png);")
    # palette = QPalette()
    # palette.setBrush(QPalette.Background, QBrush(QPixmap(r"C:\Users\hrrr123\Desktop\天车切图\炼钢厂天车挂钩智能检测系统2x.png")))
    #
    # ui.setPalette(palette)
    ui.show()
    sys.exit(app.exec_())
