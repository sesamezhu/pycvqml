from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QToolTip, QLabel, QMessageBox, QDialog ,QPushButton, QTextEdit
from gangtie import Ui_MainWindow
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QFont, QImage, QFont, QMovie
from PyQt5.QtCore import QTimer, QDateTime, QRect, Qt
import cv2
from mask_rcnn import MASK_RCNN
# from PIL import Image
# import skimage
# import os
import time
import sys
import numpy as np


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
style3 = '''
QPushButton{
         border-image:url('./images/按钮.png')
         }
         QPushButton{font-family:'黑体';font-size:16px;color:yellow;}
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
        self.video_timer.setTimerType(Qt.PreciseTimer)
        self.mask_timer = QTimer(self)
        self.mask_timer.setTimerType(Qt.PreciseTimer)
        time = QDateTime.currentDateTime()
        # 设置系统时间显示格式
        timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")
        # 在标签上显示时间
        #self.cap =cv2.VideoCapture("E:/BaiduNetdiskDownload/angang3/VID9.mp4")
        #self.cap = cv2.VideoCapture("./VID2.mp4")
        self.labeltime.setText(timeDisplay)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
        self.label.setGeometry(120, 200, 533, 947)
        self.label1.setGeometry(770, 200, 533, 947)
        self.label2.setGeometry(1330, 200, 533, 947)
        self.label3.setGeometry(2000, 200, 533, 947)
        
        self.label4.setGeometry(QRect(1901,100,60,10))
        self.label4.setText('检测点2')
        self.label4.setStyleSheet("color:white;")
        self.label4.setFont(QFont("宋体", 24))
        self.label4.adjustSize()

        self.label5.setGeometry(QRect(681,100,60,10))
        self.label5.setText('检测点1')
        self.label5.setStyleSheet("color:white;")
        self.label5.setFont(QFont("宋体", 24))
        self.label5.adjustSize()
        
        self.label6.setGeometry(QRect(140,160,60,10))
        self.label6.setText('相机a')
        self.label6.setStyleSheet("color:white;")
        self.label6.setFont(QFont("宋体", 18))
        self.label6.adjustSize()

        self.label7.setGeometry(QRect(790,160,60,10))
        self.label7.setText('相机b')
        self.label7.setStyleSheet("color:white;")
        self.label7.setFont(QFont("宋体", 18))
        self.label7.adjustSize()

        self.label8.setGeometry(QRect(1350,160,60,10))
        self.label8.setText('相机b')
        self.label8.setStyleSheet("color:white;")
        self.label8.setFont(QFont("宋体", 18))
        self.label8.adjustSize()

        self.label9.setGeometry(QRect(2020,160,60,10))
        self.label9.setText('相机b')
        self.label9.setStyleSheet("color:white;")
        self.label9.setFont(QFont("宋体", 18))
        self.label9.adjustSize()


        '''
        self.label4.setGeometry(660, 340, 600, 250)
        self.label5.setGeometry(1280, 340, 600, 250)
        self.label6.setGeometry(40, 600, 600, 250)
        self.label7.setGeometry(660, 600, 600, 250)
        self.label8.setGeometry(1280, 600, 600, 250)
        '''
        self.labelhen.setGeometry(40, 890, 1840, 5)
        self.pushButton1.setGeometry(1800, 1260, 140, 40)
        self.pushButton1.setStyleSheet(style1)
        self.pushButton1.clicked.connect(self.show_vis)
        self.pushButton2.setGeometry(2000, 1260, 140, 40)
        self.pushButton2.setStyleSheet(style1)
        self.pushButton2.clicked.connect(self.show_vis_2)

        self.pushButton3.setGeometry(2200, 1260, 140, 40)
        self.pushButton3.setStyleSheet(style2)
        self.pushButton3.clicked.connect(self.showDialog)

        self.labeltuoyuan1.setGeometry(1370, 910, 10, 10)
        self.labeltuoyuan2.setGeometry(1570, 910, 10, 10)
        self.labeltuoyuan3.setGeometry(1770, 910, 10, 10)
        print(self.labeltuoyuan3.x())
        print(self.labeltuoyuan3.width())


        self.pushButton3.clicked.connect(lambda: buttonpress(self))
        self.pushButton2.clicked.connect(lambda: buttonpress(self))
        self.pushButton1.clicked.connect(lambda: buttonpress(self))

    def showTime(self):
        # 获取系统现在的时间
        time = QDateTime.currentDateTime()
        # 设置系统时间显示格式
        timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")
        # 在标签上显示时间
        self.labeltime.setText(timeDisplay)

    def showDialog(self):
        self.mask_rcnn = MASK_RCNN()
        dialog = QDialog()
        dialog.setFixedSize(240, 100)
        dialog.setWindowFlags(Qt.FramelessWindowHint)
        dialog.setWindowTitle('提示')
        dialog.setWindowModality(Qt.ApplicationModal)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./images/shangwu.jpg")))
        dialog.setPalette(palette)

        button = QPushButton('OK',dialog)
        dialog.setStyleSheet("QPushButton:hover{background-color: rgb(255, 93, 52);}")
        button.clicked.connect(dialog.close)
        button.move(85,70)

        Text_dia = QLabel(dialog)
        Text_dia.setGeometry(QRect(45, 25, 160, 30))
        Text_dia.setText("模型加载完成！")
        Text_dia.setStyleSheet("color:white;")
        Text_dia.setFont(QFont("宋体", 18))

        dialog.exec()
        self.pushButton3.setText("  加载完成！")

    def showBox(self):
        mesBox = QMessageBox(QMessageBox.Information, '提示', '<font color=\"#0000FF\" size="12" face="verdana">模型加载完成！</font>')
        # mesBox.setStyleSheet("mesBox{border-image:url(./images/screen2.jpg;}")
        mesBox.setWindowFlags(Qt.FramelessWindowHint)
        mesBox.setStyleSheet("QPushButton:hover{background-color: rgb(255, 93, 52);}")
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./images/矩形 5@2x.png")))
        mesBox.setPalette(palette)
        mesBox.exec_()


    def load_model(self):

        # self.mask_rcnn = MASK_RCNN()
        # QMessageBox.about(self, '提示', '<font color=\"#0000FF\" size="12" face="verdana">模型加载完成！</font>')
        mesBox = QMessageBox()
        mesBox.setWindowTitle('提示')
        mesBox.setText('模型加载完成！')
        mesBox.setIcon(QMessageBox.about)
        # mesBox.setStyleSheet("QMessageBox{border-image:url(./images/screen2.jpg;}")
        mesBox.exec_()
        # self.pushButton3.setText("  加载完成！")



    def show_vis(self):
        self.cap = cv2.VideoCapture("./VID3.mp4")
        # self.cap.open("./VID3.mp4")
        self.fps = int(round(self.cap.get(cv2.CAP_PROP_FPS),0))
        self.jshu = 0
        self.video_timer.start(30)
        self.video_timer.timeout.connect(self.show_vid)
        # self.mask_timer.start(1)
        # self.mask_timer.timeout.connect(self.show_mask)


    def show_vis_2(self):
        self.cap_2 = cv2.VideoCapture("./VID5.mp4")
        # self.cap.open("./VID3.mp4")
        self.fps_2 = int(round(self.cap_2.get(cv2.CAP_PROP_FPS),0))
        self.jshu_2 = 0
        self.video_timer.start(15)
        self.video_timer.timeout.connect(self.show_vid_2)
        # self.mask_timer.start(1)
        # self.mask_timer.timeout.connect(self.show_mask)

    def slotStop(self):
        """ Slot function to stop the programme
            """
        self.cap.release()
        self.video_timer.stop()  # 停止计时器

    def imgresize(self,img,width_size):
        height, width = img.shape[:2]
        scale = width_size / width
        width = width_size
        height = int(height * scale)
        img = cv2.resize(img, (width, height))
        return img

    def show_vid(self):
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, int(((self.fps)/2)*(self.jshu)))
        # self.cap.set(cv2.CAP_PROP_POS_FRAMES, int((self.fps - 15) * self.jshu))
        self.jshu = self.jshu + 1
        flag, img = self.cap.read()
        if flag:
            #img = cv2.resize(img, (360, 640), interpolation=cv2.INTER_AREA)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = self.imgresize(img, 512)
            img = self.mask_rcnn.detect_image(img)
            img = np.array(img)
            img_show = QImage(img.data, img.shape[1], img.shape[0], img.shape[1]*3, QImage.Format_RGB888)
            self.label.setPixmap(QPixmap.fromImage(img_show))
            print(str(self.jshu))
            # img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            # img = QImage(img.data,img.shape[1],img.shape[0],QImage.Format_RGB888)
            # self.label.setPixmap(QPixmap.fromImage(img))
            # img = self.imgresize(img, 540)
            # img_mask = mask_rcnn.detect_image(img)
            # img_mask = np.array(img_mask)
            # print(img_mask.shape)
            # self.label1.setPixmap(QPixmap.fromImage(img_mask))
            # self.label2.setPixmap(QPixmap.fromImage(img))
            # self.label3.setPixmap(QPixmap.fromImage(img))
            # return img
        else:
            self.cap.release()
            self.video_timer.stop()

    def show_vid_2(self):
        self.cap_2.set(cv2.CAP_PROP_POS_FRAMES, int(((self.fps_2)/2) * self.jshu_2))
        self.jshu_2 = self.jshu_2 + 1
        flag_2, img_2 = self.cap_2.read()
        if flag_2:
            #img = cv2.resize(img, (360, 640), interpolation=cv2.INTER_AREA)
            img_2 = cv2.cvtColor(img_2, cv2.COLOR_BGR2RGB)
            img_2 = self.imgresize(img_2, 512)
            img_2 = self.mask_rcnn.detect_image(img_2)
            img_2 = np.array(img_2)
            img_show = QImage(img_2.data, img_2.shape[1], img_2.shape[0], img_2.shape[1]*3, QImage.Format_RGB888)
            self.label2.setPixmap(QPixmap.fromImage(img_show))
            # img_2 = cv2.cvtColor(img_2,cv2.COLOR_BGR2RGB)
            # img_2 = QImage(img_2.data,img.shape[1],img.shape[0],QImage.Format_RGB888)
            # self.label.setPixmap(QPixmap.fromImage(img))
            # img = self.imgresize(img, 540)
            # img_mask = mask_rcnn.detect_image(img)
            # img_mask = np.array(img_mask)
            # print(img_mask.shape)
            # self.label1.setPixmap(QPixmap.fromImage(img_mask))
            # self.label2.setPixmap(QPixmap.fromImage(img))
            # self.label3.setPixmap(QPixmap.fromImage(img))
            # return img
        else:
            self.cap.release()
            self.video_timer.stop()

    # def show_vid(self):
    #     i = 1
    #     flag,img = self.cap.read()
    #     while flag:
    #         if (i % 30) == 0:
    #             flag, img = self.cap.read()
    #             #img = cv2.resize(img, (360, 640), interpolation=cv2.INTER_AREA)
    #             img = self.imgresize(img, 540)
    #             img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #             img = QImage(img.data, img.shape[1], img.shape[0], QImage.Format_RGB888)
    #             self.label.setPixmap(QPixmap.fromImage(img))
    #             i = i + 1
    #             cv2.waitKey(1)
                # img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
                # img = QImage(img.data,img.shape[1],img.shape[0],QImage.Format_RGB888)
                # self.label.setPixmap(QPixmap.fromImage(img))
                # img = self.imgresize(img, 540)
                # img_mask = mask_rcnn.detect_image(img)
                # img_mask = np.array(img_mask)
                # print(img_mask.shape)
                # self.label1.setPixmap(QPixmap.fromImage(img_mask))
                # self.label2.setPixmap(QPixmap.fromImage(img))
                # self.label3.setPixmap(QPixmap.fromImage(img))
        # else:
        #     self.cap.release()
        #     self.video_timer.stop()



def buttonpress(self):
    sender = self.sender()
    clickevent = sender.text()
    global dingweiButton
    if(clickevent!=dingweiButton):

        if (clickevent == "1#监控位"):
            self.pushButton1.setStyleSheet(style2)
            self.pushButton2.setStyleSheet(style1)

        elif (clickevent == "2#监控位"):
            self.pushButton1.setStyleSheet(style1)
            self.pushButton2.setStyleSheet(style2)

        else:
            self.pushButton3.setStyleSheet(style3)

        dingweiButton=clickevent



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Test()
    ui.setWindowTitle("展示界面")
    desktop = QApplication.desktop()
    print("屏幕宽:" + str(desktop.width()))
    print("屏幕高:" + str(desktop.height()))

    ui.setStyleSheet("#MainWindow{border-image:url(./images/整体背景.png);}")
    # palette = QPalette()
    # palette.setBrush(QPalette.Background, QBrush(QPixmap(r"C:\Users\hrrr123\Desktop\天车切图\炼钢厂天车挂钩智能检测系统2x.png")))
    #
    # ui.setPalette(palette)
    ui.show()
    sys.exit(app.exec_())
