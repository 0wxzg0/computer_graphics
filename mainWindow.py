# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 220)
        MainWindow.setMaximumSize(QtCore.QSize(300, 220))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 301, 151))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_circle = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_circle.setMaximumSize(QtCore.QSize(80, 27))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.pushButton_circle.setFont(font)
        self.pushButton_circle.setObjectName("pushButton_circle")
        self.gridLayout.addWidget(self.pushButton_circle, 3, 0, 1, 1)
        self.pushButton_DDA = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_DDA.setMaximumSize(QtCore.QSize(80, 27))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.pushButton_DDA.setFont(font)
        self.pushButton_DDA.setObjectName("pushButton_DDA")
        self.gridLayout.addWidget(self.pushButton_DDA, 1, 0, 1, 1)
        self.pushButton_Bresenham = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_Bresenham.setMaximumSize(QtCore.QSize(80, 27))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.pushButton_Bresenham.setFont(font)
        self.pushButton_Bresenham.setObjectName("pushButton_Bresenham")
        self.gridLayout.addWidget(self.pushButton_Bresenham, 1, 1, 1, 1)
        self.pushButton_ellipse = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_ellipse.setMaximumSize(QtCore.QSize(80, 27))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.pushButton_ellipse.setFont(font)
        self.pushButton_ellipse.setObjectName("pushButton_ellipse")
        self.gridLayout.addWidget(self.pushButton_ellipse, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "简单绘图"))
        self.pushButton_circle.setText(_translate("MainWindow", "中点圆"))
        self.pushButton_DDA.setText(_translate("MainWindow", "DDA"))
        self.pushButton_Bresenham.setText(_translate("MainWindow", "Bresenham"))
        self.pushButton_ellipse.setText(_translate("MainWindow", "中点椭圆"))
