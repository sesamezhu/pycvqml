# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gangtie.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(20, 20)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labeltime = QtWidgets.QLabel(self.centralwidget)
        self.labeltime.setGeometry(QtCore.QRect(1600, 30, 300, 20))
        self.labeltime.setText("2019-02-05 12:00:00 星期二")
        self.labeltime.setStyleSheet("color:red;")
        self.labeltime.setFont(QtGui.QFont("黑体", 12))
        self.labeltime.adjustSize()
        # self.label = QtWidgets.QLabel(self.centralwidget)
        # self.label.setPixmap(QtGui.QPixmap("C:/Users/hrrr123/Desktop/天车切图/框.png"))
        self.labeltime.setObjectName("labeltime")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 60, 1154, 612))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/hrrr123/Desktop/天车切图/框.png"))
        self.label.setObjectName("label")

        self.label.setScaledContents(True)  # 让图片自适应label大
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(290, 280, 54, 12))
        self.label1.setText("")
        self.label1.setPixmap(QtGui.QPixmap("C:/Users/hrrr123/Desktop/天车切图/框.png"))
        self.label1.setObjectName("label1")
        self.label1.setScaledContents(True)  # 让图片自适应label大
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(620, 390, 54, 12))
        self.label2.setText("")
        self.label2.setPixmap(QtGui.QPixmap("C:/Users/hrrr123/Desktop/天车切图/框.png"))
        self.label2.setObjectName("label2")
        self.label2.setScaledContents(True)  # 让图片自适应label大
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(620, 390, 54, 12))
        self.label3.setText("")
        self.label3.setPixmap(QtGui.QPixmap("C:/Users/hrrr123/Desktop/天车切图/框.png"))
        self.label3.setObjectName("label3")
        self.label3.setScaledContents(True)  # 让图片自适应label大
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(620, 390, 54, 12))
        self.label4.setText("")
        self.label4.setPixmap(QtGui.QPixmap("C:/Users/hrrr123/Desktop/天车切图/框.png"))
        self.label4.setObjectName("label4")
        self.label4.setScaledContents(True)  # 让图片自适应label大
        self.label5 = QtWidgets.QLabel(self.centralwidget)
        self.label5.setGeometry(QtCore.QRect(620, 390, 54, 12))
        self.label5.setText("")
        self.label5.setPixmap(QtGui.QPixmap("C:/Users/hrrr123/Desktop/天车切图/框.png"))
        self.label5.setObjectName("label5")
        self.label5.setScaledContents(True)  # 让图片自适应label大
        self.label6 = QtWidgets.QLabel(self.centralwidget)
        self.label6.setGeometry(QtCore.QRect(620, 390, 54, 12))
        self.label6.setText("")
        self.label6.setPixmap(QtGui.QPixmap("C:/Users/hrrr123/Desktop/天车切图/框.png"))
        self.label6.setObjectName("label6")
        self.label6.setScaledContents(True)  # 让图片自适应label大
        self.label7 = QtWidgets.QLabel(self.centralwidget)
        self.label7.setGeometry(QtCore.QRect(620, 390, 54, 12))
        self.label7.setText("")
        self.label7.setPixmap(QtGui.QPixmap("C:/Users/hrrr123/Desktop/天车切图/框.png"))
        self.label7.setObjectName("label7")
        self.label7.setScaledContents(True)  # 让图片自适应label大
        self.label8 = QtWidgets.QLabel(self.centralwidget)
        self.label8.setGeometry(QtCore.QRect(620, 390, 54, 12))
        self.label8.setText("")
        self.label8.setPixmap(QtGui.QPixmap("C:/Users/hrrr123/Desktop/天车切图/框.png"))
        self.label8.setObjectName("label8")
        self.label8.setScaledContents(True)  # 让图片自适应label大
        self.label9 = QtWidgets.QLabel(self.centralwidget)
        self.label9.setGeometry(QtCore.QRect(620, 390, 54, 12))
        self.label9.setText("")
        self.label9.setPixmap(QtGui.QPixmap("C:/Users/hrrr123/Desktop/天车切图/框.png"))
        self.label9.setObjectName("label8")
        self.label9.setScaledContents(True)  # 让图片自适应label大

        self.labelhen = QtWidgets.QLabel(self.centralwidget)
        self.labelhen.setGeometry(QtCore.QRect(50, 640, 1000, 12))
        self.labelhen.setText("")
        self.labelhen.setPixmap(QtGui.QPixmap("C:/Users/hrrr123/Desktop/天车切图/圆角矩形 3.png"))
        self.labelhen.setObjectName("labelhen")
        self.labelhen.setScaledContents(True)  # 让图片自适应label大
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(210, 160, 75, 23))
        self.pushButton1.setText("1#监控位")
        self.pushButton1.setObjectName("B1")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(210, 160, 75, 23))
        self.pushButton2.setText("2#监控位")
        self.pushButton2.setObjectName("B2")

        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(210, 160, 75, 23))
        self.pushButton3.setText("加载模型")
        self.pushButton3.setObjectName("B3")


        self.labeltuoyuan1 = QtWidgets.QLabel(self.centralwidget)
        self.labeltuoyuan1.setGeometry(QtCore.QRect(620, 390, 54, 12))
        self.labeltuoyuan1.setText("")
        self.labeltuoyuan1.setPixmap(QtGui.QPixmap("C:/Users/hrrr123/Desktop/天车切图/椭圆 2@2x.png"))
        self.labeltuoyuan1.setObjectName("labeltuoyuan1")
        self.labeltuoyuan1.setScaledContents(True)  # 让图片自适应label大
        self.labeltuoyuan2 = QtWidgets.QLabel(self.centralwidget)
        self.labeltuoyuan2.setGeometry(QtCore.QRect(620, 390, 54, 12))
        self.labeltuoyuan2.setText("")
        self.labeltuoyuan2.setPixmap(QtGui.QPixmap("C:/Users/hrrr123/Desktop/天车切图/椭圆 2@2x(1).png"))
        self.labeltuoyuan2.setObjectName("labeltuoyuan1")
        self.labeltuoyuan2.setScaledContents(True)  # 让图片自适应label大
        self.labeltuoyuan3 = QtWidgets.QLabel(self.centralwidget)
        self.labeltuoyuan3.setGeometry(QtCore.QRect(620, 390, 54, 12))
        self.labeltuoyuan3.setText("")
        self.labeltuoyuan3.setPixmap(QtGui.QPixmap("C:/Users/hrrr123/Desktop/天车切图/椭圆 2@2x(1).png"))
        self.labeltuoyuan3.setObjectName("labeltuoyuan1")
        self.labeltuoyuan3.setScaledContents(True)  # 让图片自适应label大
        # self.__dict__[f'x{i}'].setGeometry(QtCore.QRect(100 + (i + 1) * 10, 95, 20, 20))
        '''
        for i in range(18):
            self.__dict__[f'x{i}'] = QtWidgets.QLabel(self.centralwidget)
            if i<6:
                if i%2==0:
                    self.__dict__[f'x{i}'].setGeometry(QtCore.QRect(100+(i//2)*620, 95, 20, 20))
                    self.__dict__[f'x{i}'].setPixmap(QtGui.QPixmap("C:/Users/hrrr123/Desktop/天车切图/绿@2x.png"))
                if i % 2 == 1:
                    self.__dict__[f'x{i}'].setGeometry(QtCore.QRect(600+(i//2)*620, 95, 20, 20))
                    self.__dict__[f'x{i}'].setPixmap(QtGui.QPixmap("C:/Users/hrrr123/Desktop/天车切图/红@2x.png"))
            elif 6<=i<12:
                if i%2==0:
                    self.__dict__[f'x{i}'].setGeometry(QtCore.QRect(100+((i-6)//2)*620, 95+260, 20, 20))
                    self.__dict__[f'x{i}'].setPixmap(QtGui.QPixmap("C:/Users/hrrr123/Desktop/天车切图/绿@2x.png"))
                if i % 2 == 1:
                    self.__dict__[f'x{i}'].setGeometry(QtCore.QRect(600+((i-6)//2)*620, 95+260, 20, 20))
                    self.__dict__[f'x{i}'].setPixmap(QtGui.QPixmap("C:/Users/hrrr123/Desktop/天车切图/红@2x.png"))
            else:
                if i%2==0:
                    self.__dict__[f'x{i}'].setGeometry(QtCore.QRect(100+((i-12)//2)*620, 95+260+260, 20, 20))
                    self.__dict__[f'x{i}'].setPixmap(QtGui.QPixmap("C:/Users/hrrr123/Desktop/天车切图/绿@2x.png"))
                if i % 2 == 1:
                    self.__dict__[f'x{i}'].setGeometry(QtCore.QRect(600+((i-12)//2)*620, 95+260+260, 20, 20))
                    self.__dict__[f'x{i}'].setPixmap(QtGui.QPixmap("C:/Users/hrrr123/Desktop/天车切图/红@2x.png"))

            self.__dict__[f'x{i}'].setText("")
            self.__dict__[f'x{i}'].setObjectName("labelz"+str(i))
            self.__dict__[f'x{i}'].setScaledContents(True)  # 让图片自适应label大
        
        for i in range(4):
            self.__dict__[f'name{i}'] = QtWidgets.QLabel(self.centralwidget)
            if i<2:
                self.__dict__[f'name{i}'].setGeometry(QtCore.QRect(460+900*(i),80,60,10))
                self.__dict__[f'name{i}'].setText("测试东西")
                self.__dict__[f'name{i}'].setStyleSheet("color:white;")
                self.__dict__[f'name{i}'].setFont(QtGui.QFont("黑体", 12));
                self.__dict__[f'name{i}'].adjustSize()
                self.__dict__[f'name{i}'].setObjectName("labelname" + str(i))
 
            else:
                self.__dict__[f'name{i}'].setGeometry(QtCore.QRect(40 + 500 * (i - 4), 60 + 260+260, 60, 10))
                self.__dict__[f'name{i}'].setText("测试东西")
                self.__dict__[f'name{i}'].setStyleSheet("color:white;")
                self.__dict__[f'name{i}'].setFont(QtGui.QFont("黑体", 12))
                self.__dict__[f'name{i}'].adjustSize()
                self.__dict__[f'name{i}'].setObjectName("labelname" + str(i))

        print(self.__dict__[f'name0'].x())
        print(self.__dict__[f'name0'].y())
        print(self.__dict__[f'name0'].width())
        print(self.__dict__[f'name0'].height())
        
        for i in range(18):
            self.__dict__[f'namehen{i}'] = QtWidgets.QLabel(self.centralwidget)
            if i<6:
                if i%2==0:
                    self.__dict__[f'namehen{i}'].setGeometry(QtCore.QRect(248+620*(i//2), 105, 40, 5))
                    self.__dict__[f'namehen{i}'].setPixmap(QtGui.QPixmap("C:/Users/hrrr123/Desktop/天车切图/矩形 4@2x.png"))
                    self.__dict__[f'namehen{i}'].setText("")
                    self.__dict__[f'namehen{i}'].setObjectName("labelnamehen" + str(i))
                    self.__dict__[f'namehen{i}'].setScaledContents(True)  # 让图片自适应label大
                else:
                    self.__dict__[f'namehen{i}'].setGeometry(QtCore.QRect(390+620*(i//2), 105, 40, 5))
                    self.__dict__[f'namehen{i}'].setPixmap(QtGui.QPixmap("C:/Users/hrrr123/Desktop/天车切图/矩形 4 拷贝@2x.png"))
                    self.__dict__[f'namehen{i}'].setText("")
                    self.__dict__[f'namehen{i}'].setObjectName("labelnamehen" + str(i))
                    self.__dict__[f'namehen{i}'].setScaledContents(True)  # 让图片自适应label大
            elif 6<=i<12:
                if i%2==0:
                    self.__dict__[f'namehen{i}'].setGeometry(QtCore.QRect(248+620*((i-6)//2), 105+260, 40, 5))
                    self.__dict__[f'namehen{i}'].setPixmap(QtGui.QPixmap("C:/Users/hrrr123/Desktop/天车切图/矩形 4@2x.png"))
                    self.__dict__[f'namehen{i}'].setText("")
                    self.__dict__[f'namehen{i}'].setObjectName("labelnamehen" + str(i))
                    self.__dict__[f'namehen{i}'].setScaledContents(True)  # 让图片自适应label大
                else:
                    self.__dict__[f'namehen{i}'].setGeometry(QtCore.QRect(390+620*((i-6)//2), 105+260, 40, 5))
                    self.__dict__[f'namehen{i}'].setPixmap(QtGui.QPixmap("C:/Users/hrrr123/Desktop/天车切图/矩形 4 拷贝@2x.png"))
                    self.__dict__[f'namehen{i}'].setText("")
                    self.__dict__[f'namehen{i}'].setObjectName("labelnamehen" + str(i))
                    self.__dict__[f'namehen{i}'].setScaledContents(True)  # 让图片自适应label大
            else:
                if i % 2 == 0:
                    self.__dict__[f'namehen{i}'].setGeometry(QtCore.QRect(248 + 620 * ((i-12) // 2), 105 + 260+260, 40, 5))
                    self.__dict__[f'namehen{i}'].setPixmap(QtGui.QPixmap("C:/Users/hrrr123/Desktop/天车切图/矩形 4@2x.png"))
                    self.__dict__[f'namehen{i}'].setText("")
                    self.__dict__[f'namehen{i}'].setObjectName("labelnamehen" + str(i))
                    self.__dict__[f'namehen{i}'].setScaledContents(True)  # 让图片自适应label大
                else:
                    self.__dict__[f'namehen{i}'].setGeometry(QtCore.QRect(390 + 620 * ((i-12) // 2), 105 + 260+260, 40, 5))
                    self.__dict__[f'namehen{i}'].setPixmap(
                        QtGui.QPixmap("C:/Users/hrrr123/Desktop/天车切图/矩形 4 拷贝@2x.png"))
                    self.__dict__[f'namehen{i}'].setText("")
                    self.__dict__[f'namehen{i}'].setObjectName("labelnamehen" + str(i))
                    self.__dict__[f'namehen{i}'].setScaledContents(True)  # 让图片自适应label大
        '''

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 954, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
