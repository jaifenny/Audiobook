# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 950)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Image1 = QtWidgets.QLabel(self.centralwidget)
        self.Image1.setGeometry(QtCore.QRect(40, 120, 360, 270))
        self.Image1.setFrameShape(QtWidgets.QFrame.Panel)
        self.Image1.setAlignment(QtCore.Qt.AlignCenter)
        self.Image1.setObjectName("Image1")
        self.select_img_1 = QtWidgets.QPushButton(self.centralwidget)
        self.select_img_1.setGeometry(QtCore.QRect(40, 330, 61, 61))
        self.select_img_1.setAutoFillBackground(False)
        self.select_img_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"C:\Users\elain\OneDrive\文件\大學資料\1112\機器學習\final project\pratice\image test/1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.select_img_1.setIcon(icon)
        self.select_img_1.setIconSize(QtCore.QSize(40, 40))
        self.select_img_1.setAutoDefault(False)
        self.select_img_1.setObjectName("select_img_1")
        self.show_story = QtWidgets.QTextBrowser(self.centralwidget)
        self.show_story.setGeometry(QtCore.QRect(40, 590, 1131, 301))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        self.show_story.setFont(font)
        self.show_story.setObjectName("show_story")
        self.Image2 = QtWidgets.QLabel(self.centralwidget)
        self.Image2.setGeometry(QtCore.QRect(450, 120, 360, 270))
        self.Image2.setFrameShape(QtWidgets.QFrame.Panel)
        self.Image2.setAlignment(QtCore.Qt.AlignCenter)
        self.Image2.setObjectName("Image2")
        self.Image3 = QtWidgets.QLabel(self.centralwidget)
        self.Image3.setGeometry(QtCore.QRect(850, 120, 360, 270))
        self.Image3.setFrameShape(QtWidgets.QFrame.Panel)
        self.Image3.setAlignment(QtCore.Qt.AlignCenter)
        self.Image3.setObjectName("Image3")
        self.select_img_2 = QtWidgets.QPushButton(self.centralwidget)
        self.select_img_2.setGeometry(QtCore.QRect(450, 330, 61, 61))
        self.select_img_2.setAutoFillBackground(False)
        self.select_img_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/elain/OneDrive/文件/大學資料/1112/機器學習/final project/pratice/image test/2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.select_img_2.setIcon(icon1)
        self.select_img_2.setIconSize(QtCore.QSize(40, 40))
        self.select_img_2.setAutoDefault(False)
        self.select_img_2.setObjectName("select_img_2")
        self.select_img_3 = QtWidgets.QPushButton(self.centralwidget)
        self.select_img_3.setGeometry(QtCore.QRect(850, 330, 61, 61))
        self.select_img_3.setAutoFillBackground(False)
        self.select_img_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/elain/OneDrive/文件/大學資料/1112/機器學習/final project/pratice/image test/3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.select_img_3.setIcon(icon2)
        self.select_img_3.setIconSize(QtCore.QSize(40, 40))
        self.select_img_3.setAutoDefault(False)
        self.select_img_3.setObjectName("select_img_3")
        self.notice1 = QtWidgets.QLabel(self.centralwidget)
        self.notice1.setGeometry(QtCore.QRect(50, 410, 481, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.notice1.setFont(font)
        self.notice1.setObjectName("notice1")
        self.style_happy = QtWidgets.QPushButton(self.centralwidget)
        self.style_happy.setGeometry(QtCore.QRect(110, 490, 201, 51))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.style_happy.setFont(font)
        self.style_happy.setObjectName("style_happy")
        self.style_horror = QtWidgets.QPushButton(self.centralwidget)
        self.style_horror.setGeometry(QtCore.QRect(370, 490, 201, 51))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.style_horror.setFont(font)
        self.style_horror.setObjectName("style_horror")
        self.style_sad = QtWidgets.QPushButton(self.centralwidget)
        self.style_sad.setGeometry(QtCore.QRect(630, 490, 201, 51))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.style_sad.setFont(font)
        self.style_sad.setObjectName("style_sad")
        self.style_heatwarming = QtWidgets.QPushButton(self.centralwidget)
        self.style_heatwarming.setGeometry(QtCore.QRect(900, 490, 201, 51))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.style_heatwarming.setFont(font)
        self.style_heatwarming.setObjectName("style_heatwarming")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(500, 30, 271, 51))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(24)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.download = QtWidgets.QPushButton(self.centralwidget)
        self.download.setGeometry(QtCore.QRect(1180, 610, 80, 80))
        self.download.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/Users/elain/OneDrive/文件/大學資料/1112/機器學習/final project/pratice/image test/download.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.download.setIcon(icon3)
        self.download.setIconSize(QtCore.QSize(80, 80))
        self.download.setObjectName("download")
        self.speaker = QtWidgets.QPushButton(self.centralwidget)
        self.speaker.setGeometry(QtCore.QRect(1180, 700, 80, 80))
        self.speaker.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:/Users/elain/OneDrive/文件/大學資料/1112/機器學習/final project/pratice/image test/speak.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.speaker.setIcon(icon4)
        self.speaker.setIconSize(QtCore.QSize(70, 70))
        self.speaker.setObjectName("speaker")
        self.notice2 = QtWidgets.QLabel(self.centralwidget)
        self.notice2.setGeometry(QtCore.QRect(50, 440, 481, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.notice2.setFont(font)
        self.notice2.setObjectName("notice2")
        self.delete_2 = QtWidgets.QPushButton(self.centralwidget)
        self.delete_2.setGeometry(QtCore.QRect(1180, 790, 80, 80))
        self.delete_2.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("C:/Users/elain/OneDrive/文件/大學資料/1112/機器學習/final project/pratice/image test/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_2.setIcon(icon5)
        self.delete_2.setIconSize(QtCore.QSize(70, 70))
        self.delete_2.setObjectName("delete_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 25))
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
        self.Image1.setText(_translate("MainWindow", "[None]"))
        self.Image2.setText(_translate("MainWindow", "[None]"))
        self.Image3.setText(_translate("MainWindow", "[None]"))
        self.notice1.setText(_translate("MainWindow", "*Notice 1: Please click the number to select the photo"))
        self.style_happy.setText(_translate("MainWindow", "快樂"))
        self.style_horror.setText(_translate("MainWindow", "恐怖"))
        self.style_sad.setText(_translate("MainWindow", "悲傷"))
        self.style_heatwarming.setText(_translate("MainWindow", "勵志"))
        self.title.setText(_translate("MainWindow", "看圖說故事"))
        self.notice2.setText(_translate("MainWindow", "*Notice 2: The name of photo can not include Chinese"))
