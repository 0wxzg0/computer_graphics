# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WindowEllipse.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WindowEllipse(object):
    def setupUi(self, WindowEllipse):
        WindowEllipse.setObjectName("WindowEllipse")
        WindowEllipse.resize(300, 220)
        WindowEllipse.setMaximumSize(QtCore.QSize(300, 220))
        self.layoutWidget = QtWidgets.QWidget(WindowEllipse)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 309, 221))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_rx = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_rx.setMaximumSize(QtCore.QSize(80, 20))
        self.lineEdit_rx.setObjectName("lineEdit_rx")
        self.gridLayout.addWidget(self.lineEdit_rx, 3, 2, 1, 1)
        self.pushButton_start = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_start.setMaximumSize(QtCore.QSize(80, 27))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")
        self.gridLayout.addWidget(self.pushButton_start, 0, 1, 1, 1)
        self.pushButton_clear = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_clear.setMaximumSize(QtCore.QSize(80, 27))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.gridLayout.addWidget(self.pushButton_clear, 0, 2, 1, 1)
        self.lineEdit_ry = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_ry.setMaximumSize(QtCore.QSize(80, 20))
        self.lineEdit_ry.setObjectName("lineEdit_ry")
        self.gridLayout.addWidget(self.lineEdit_ry, 4, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 1, 1, 1)
        self.lineEdit_y = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_y.setMaximumSize(QtCore.QSize(80, 20))
        self.lineEdit_y.setObjectName("lineEdit_y")
        self.gridLayout.addWidget(self.lineEdit_y, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.lineEdit_x = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_x.setMaximumSize(QtCore.QSize(80, 20))
        self.lineEdit_x.setObjectName("lineEdit_x")
        self.gridLayout.addWidget(self.lineEdit_x, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMaximumSize(QtCore.QSize(82, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton_return = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_return.setMaximumSize(QtCore.QSize(80, 27))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.pushButton_return.setFont(font)
        self.pushButton_return.setObjectName("pushButton_return")
        self.gridLayout.addWidget(self.pushButton_return, 5, 2, 1, 1)

        self.retranslateUi(WindowEllipse)
        QtCore.QMetaObject.connectSlotsByName(WindowEllipse)

    def retranslateUi(self, WindowEllipse):
        _translate = QtCore.QCoreApplication.translate
        WindowEllipse.setWindowTitle(_translate("WindowEllipse", "中点椭圆"))
        self.pushButton_start.setText(_translate("WindowEllipse", "开始绘制"))
        self.pushButton_clear.setText(_translate("WindowEllipse", "清空绘图"))
        self.label_2.setText(_translate("WindowEllipse", "x"))
        self.label_7.setText(_translate("WindowEllipse", "ry"))
        self.label_3.setText(_translate("WindowEllipse", "y"))
        self.label_6.setText(_translate("WindowEllipse", "rx"))
        self.label_4.setText(_translate("WindowEllipse", "圆心"))
        self.label_5.setText(_translate("WindowEllipse", "半轴"))
        self.label.setText(_translate("WindowEllipse", "请输入坐标"))
        self.pushButton_return.setText(_translate("WindowEllipse", "返回"))
