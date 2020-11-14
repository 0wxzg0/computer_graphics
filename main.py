# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from mainWindow import *
from WindowBresenham import *
from WindowDDA import *
from WindowCircle import *
from WindowEllipse import *
import numpy as np
import matplotlib.pyplot as plt


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setupUi(self)
        self.pushButton_DDA.clicked.connect(self.to_DDA)
        self.pushButton_Bresenham.clicked.connect(self.to_bresenham)
        self.pushButton_circle.clicked.connect(self.to_circle)
        self.pushButton_ellipse.clicked.connect(self.to_ellipse)

    def to_DDA(self):
        self.hide()
        self.s = DDA()
        self.s.show()

    def to_bresenham(self):
        self.hide()
        self.s = Bresenham()
        self.s.show()

    def to_circle(self):
        self.hide()
        self.s = Circle()
        self.s.show()

    def to_ellipse(self):
        self.hide()
        self.s = Ellipse()
        self.s.show()


class Bresenham(QtWidgets.QWidget, Ui_WindowBre):
    def __init__(self, parent=None):
        super(Bresenham, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setupUi(self)
        self.pushButton_start.clicked.connect(self.start_draw)
        self.pushButton_clear.clicked.connect(self.clear_graph)
        self.pushButton_return.clicked.connect(self.back_to_select_page)

    def clear_graph(self):
        self.lineEdit_x1.clear()
        self.lineEdit_x2.clear()
        self.lineEdit_y1.clear()
        self.lineEdit_y2.clear()
        plt.close()

    def back_to_select_page(self):
        self.hide()
        self.f = MyWindow()
        self.f.show()

    def change_spines(self):
        plt.figure(figsize=(6, 6))
        self.set_ax()
        self.ax = plt.gca()
        self.ax.spines['left'].set_position('center')
        self.ax.spines['left'].set_color('red')
        self.ax.spines['left'].set_linewidth(2)
        self.ax.tick_params(axis='y', colors='red')
        self.ax.spines['left'].set_position(('data', 0))
        self.ax.annotate('', (0, self.tmp - 2), xytext=(0, self.tmp + 2),
                         arrowprops={'arrowstyle': '<-', 'color': 'red', 'linewidth': 2})

        self.ax.spines['right'].set_color('none')

        self.ax.spines['bottom'].set_position('center')
        self.ax.spines['bottom'].set_color('blue')
        self.ax.spines['bottom'].set_linewidth(2)
        self.ax.tick_params(axis='x', colors='blue')
        self.ax.spines['bottom'].set_position(('data', 0))
        self.ax.annotate('', (self.tmp - 2, 0), xytext=(self.tmp + 2, 0),
                         arrowprops={'arrowstyle': '<-', 'color': 'blue', 'linewidth': 2})
        self.ax.spines['top'].set_color('none')

    def set_ax(self):
        self.tmp = max(abs(self.x1), abs(self.x2), abs(self.y1), abs(self.y2))
        self.tmp2 = int(self.tmp / 100) + 1
        self.tmp = self.tmp2 * 100
        plt.xlim(-1 * self.tmp, self.tmp)
        plt.ylim(-1 * self.tmp, self.tmp)
        plt.xticks(np.linspace(-1 * self.tmp, self.tmp, self.tmp2 * 2 + 1))
        plt.yticks(np.linspace(-1 * self.tmp, self.tmp, self.tmp2 * 2 + 1))

    def start_draw(self):
        self.x1 = int(self.lineEdit_x1.text())
        self.x2 = int(self.lineEdit_x2.text())
        self.y1 = int(self.lineEdit_y1.text())
        self.y2 = int(self.lineEdit_y2.text())
        self.y_neg = False
        self.dx = self.x2 - self.x1
        if self.dx < 0:
            self.x1, self.x2 = self.x2, self.x1
            self.y1, self.y2 = self.y2, self.y1
            self.dx = -self.dx
        self.dy = self.y2 - self.y1

        if self.dy < 0:
            self.y_neg = True
            self.dy = -self.dy

        self.x = []
        self.y = []
        self.xk = self.x1
        self.yk = self.y1

        self.change_spines()

        if self.dx == 0:  # 竖线
            self.yk = min(self.y1, self.y2)
            self.y_end = max(self.y1, self.y2)
            while self.yk <= self.y_end:
                self.y.append(self.yk)
                self.x.append(self.xk)
                self.yk += 1
                plt.pause(0.01)
                plt.scatter(self.x, self.y, s=1, color='black', marker='.')
            plt.show()

        elif self.dy == 0:  # 横线
            while self.xk <= self.x2:
                self.y.append(self.yk)
                self.x.append(self.xk)
                self.xk += 1
                plt.pause(0.01)
                plt.scatter(self.x, self.y, s=1, color='black', marker='.')
            plt.show()

        else:
            self.k = self.dy / (1.0 * self.dx)

            if self.k <= 1:
                self.k_flag = True
            else:
                self.k_flag = False
                self.dx = self.y2 - self.y1
                self.x1, self.y1 = self.y1, self.x1
                self.x2, self.y2 = self.y2, self.x2
                if self.dx < 0:
                    self.x1, self.x2 = self.x2, self.x1
                    self.y1, self.y2 = self.y2, self.y1
                    self.dx = -self.dx
                self.dy = abs(self.y2 - self.y1)
                self.k = self.dy / (1.0 * self.dx)
                self.xk = self.x1
                self.yk = self.y1

            self.p = 2 * self.dy - self.dx
            self.u = 2 * self.dy
            self.v = 2 * self.dy - 2 * self.dx

            while self.xk <= self.x2:
                if self.y_neg and self.k_flag:
                    self.y.append(self.y1 * 2 - self.yk)
                else:
                    self.y.append(self.yk)

                if self.p > 0:
                    self.yk += 1
                    self.p += self.v
                else:
                    self.p += self.u
                if self.y_neg and self.k_flag is False:
                    self.x.append(self.x1 * 2 - self.xk)
                else:
                    self.x.append(self.xk)
                self.xk += 1
                plt.pause(0.01)
                if self.k_flag:
                    plt.scatter(self.x, self.y, s=1, color='black', marker='.')
                else:
                    plt.scatter(self.y, self.x, s=1, color='black', marker='.')

            plt.show()


class DDA(QtWidgets.QWidget, Ui_WindowDDA):
    def __init__(self, parent=None):
        super(DDA, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setupUi(self)
        self.pushButton_start.clicked.connect(self.start_draw)
        self.pushButton_clear.clicked.connect(self.clear_graph)
        self.pushButton_return.clicked.connect(self.back_to_select_page)

    def clear_graph(self):
        self.lineEdit_x1.clear()
        self.lineEdit_x2.clear()
        self.lineEdit_y1.clear()
        self.lineEdit_y2.clear()
        plt.close()

    def back_to_select_page(self):
        self.hide()
        self.f = MyWindow()
        self.f.show()

    def change_spines(self):
        plt.figure(figsize=(6, 6))
        self.set_ax()
        self.ax = plt.gca()
        self.ax.spines['left'].set_position('center')
        self.ax.spines['left'].set_color('red')
        self.ax.spines['left'].set_linewidth(2)
        self.ax.tick_params(axis='y', colors='red')
        self.ax.spines['left'].set_position(('data', 0))
        self.ax.annotate('', (0, self.tmp - 2), xytext=(0, self.tmp + 2),
                         arrowprops={'arrowstyle': '<-', 'color': 'red', 'linewidth': 2})

        self.ax.spines['right'].set_color('none')

        self.ax.spines['bottom'].set_position('center')
        self.ax.spines['bottom'].set_color('blue')
        self.ax.spines['bottom'].set_linewidth(2)
        self.ax.tick_params(axis='x', colors='blue')
        self.ax.spines['bottom'].set_position(('data', 0))
        self.ax.annotate('', (self.tmp - 2, 0), xytext=(self.tmp + 2, 0),
                         arrowprops={'arrowstyle': '<-', 'color': 'blue', 'linewidth': 2})
        self.ax.spines['top'].set_color('none')

    def set_ax(self):
        self.tmp = max(abs(self.x1), abs(self.x2), abs(self.y1), abs(self.y2))
        self.tmp2 = int(self.tmp / 100) + 1
        self.tmp = self.tmp2 * 100
        plt.xlim(-1 * self.tmp, self.tmp)
        plt.ylim(-1 * self.tmp, self.tmp)
        plt.xticks(np.linspace(-1 * self.tmp, self.tmp, self.tmp2 * 2 + 1))
        plt.yticks(np.linspace(-1 * self.tmp, self.tmp, self.tmp2 * 2 + 1))

    def start_draw(self):
        self.x1 = int(self.lineEdit_x1.text())
        self.x2 = int(self.lineEdit_x2.text())
        self.y1 = int(self.lineEdit_y1.text())
        self.y2 = int(self.lineEdit_y2.text())
        self.change_spines()
        if abs(self.x2 - self.x1) >= abs(self.y2 - self.y1):
            self.len = abs(self.x2 - self.x1)
        else:
            self.len = abs(self.y2 - self.y1)
        self.dx = float((self.x2 - self.x1) / self.len)
        self.dy = float((self.y2 - self.y1) / self.len)
        self.x = []
        self.y = []
        self.xk = self.x1
        self.yk = self.y1
        i = 1
        while i <= self.len:
            self.y.append(int(self.yk))
            self.x.append(int(self.xk))
            self.xk = self.dx + self.xk
            self.yk = self.dy + self.yk
            i += 1
            plt.pause(0.01)
            plt.scatter(self.x, self.y, s=1, color='black', marker='.')
        plt.show()


class Circle(QtWidgets.QWidget, Ui_WindowCircle):
    def __init__(self, parent=None):
        super(Circle, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setupUi(self)
        self.pushButton_start.clicked.connect(self.start_draw)
        self.pushButton_clear.clicked.connect(self.clear_graph)
        self.pushButton_return.clicked.connect(self.back_to_select_page)

    def clear_graph(self):
        self.lineEdit_x.clear()
        self.lineEdit_y.clear()
        self.lineEdit_r.clear()
        plt.close()

    def back_to_select_page(self):
        self.hide()
        self.f = MyWindow()
        self.f.show()

    def change_spines(self):
        plt.figure(figsize=(6, 6))
        self.set_ax()
        self.ax = plt.gca()
        self.ax.spines['left'].set_position('center')
        self.ax.spines['left'].set_color('red')
        self.ax.spines['left'].set_linewidth(2)
        self.ax.tick_params(axis='y', colors='red')
        self.ax.spines['left'].set_position(('data', 0))
        self.ax.annotate('', (0, self.tmp - 2), xytext=(0, self.tmp + 2),
                         arrowprops={'arrowstyle': '<-', 'color': 'red', 'linewidth': 2})

        self.ax.spines['right'].set_color('none')

        self.ax.spines['bottom'].set_position('center')
        self.ax.spines['bottom'].set_color('blue')
        self.ax.spines['bottom'].set_linewidth(2)
        self.ax.tick_params(axis='x', colors='blue')
        self.ax.spines['bottom'].set_position(('data', 0))
        self.ax.annotate('', (self.tmp - 2, 0), xytext=(self.tmp + 2, 0),
                         arrowprops={'arrowstyle': '<-', 'color': 'blue', 'linewidth': 2})
        self.ax.spines['top'].set_color('none')

    def set_ax(self):
        self.tmp = max(abs(self.x0 + self.r), abs(self.x0 - self.r), abs(self.y0 + self.r), abs(self.y0 - self.r))
        self.tmp2 = int(self.tmp / 100) + 1
        self.tmp = self.tmp2 * 100
        plt.xlim(-1 * self.tmp, self.tmp)
        plt.ylim(-1 * self.tmp, self.tmp)
        plt.xticks(np.linspace(-1 * self.tmp, self.tmp, self.tmp2 * 2 + 1))
        plt.yticks(np.linspace(-1 * self.tmp, self.tmp, self.tmp2 * 2 + 1))

    def eight_point(self):
        self.x.append(self.x0 + self.xk)
        self.y.append(self.y0 + self.yk)
        self.x.append(self.x0 - self.xk)
        self.y.append(self.y0 + self.yk)
        self.x.append(self.x0 + self.xk)
        self.y.append(self.y0 - self.yk)
        self.x.append(self.x0 - self.xk)
        self.y.append(self.y0 - self.yk)
        self.x.append(self.x0 + self.yk)
        self.y.append(self.y0 + self.xk)
        self.x.append(self.x0 - self.yk)
        self.y.append(self.y0 + self.xk)
        self.x.append(self.x0 + self.yk)
        self.y.append(self.y0 - self.xk)
        self.x.append(self.x0 - self.yk)
        self.y.append(self.y0 - self.xk)

    def start_draw(self):
        self.x0 = int(self.lineEdit_x.text())
        self.y0 = int(self.lineEdit_y.text())
        self.r = int(self.lineEdit_r.text())
        self.change_spines()
        self.x = []
        self.y = []
        self.xk = 0
        self.yk = self.r
        self.eight_point()
        self.d = 1 - self.r
        while self.xk < self.yk:
            if self.d < 0:
                self.d = self.d + 2 * self.xk + 3
            else:
                self.d = self.d + 2 * (self.xk - self.yk) + 5
                self.yk -= 1
            self.xk += 1
            self.eight_point()
            plt.pause(0.01)
            plt.scatter(self.x, self.y, s=1, color='black', marker='.')
        plt.show()


class Ellipse(QtWidgets.QWidget, Ui_WindowEllipse):
    def __init__(self, parent=None):
        super(Ellipse, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setupUi(self)
        self.pushButton_start.clicked.connect(self.start_draw)
        self.pushButton_clear.clicked.connect(self.clear_graph)
        self.pushButton_return.clicked.connect(self.back_to_select_page)

    def clear_graph(self):
        self.lineEdit_x.clear()
        self.lineEdit_rx.clear()
        self.lineEdit_y.clear()
        self.lineEdit_ry.clear()
        plt.close()

    def back_to_select_page(self):
        self.hide()
        self.f = MyWindow()
        self.f.show()

    def change_spines(self):
        plt.figure(figsize=(6, 6))
        self.set_ax()
        self.ax = plt.gca()
        self.ax.spines['left'].set_position('center')
        self.ax.spines['left'].set_color('red')
        self.ax.spines['left'].set_linewidth(2)
        self.ax.tick_params(axis='y', colors='red')
        self.ax.spines['left'].set_position(('data', 0))
        self.ax.annotate('', (0, self.tmp - 2), xytext=(0, self.tmp + 2),
                         arrowprops={'arrowstyle': '<-', 'color': 'red', 'linewidth': 2})

        self.ax.spines['right'].set_color('none')

        self.ax.spines['bottom'].set_position('center')
        self.ax.spines['bottom'].set_color('blue')
        self.ax.spines['bottom'].set_linewidth(2)
        self.ax.tick_params(axis='x', colors='blue')
        self.ax.spines['bottom'].set_position(('data', 0))
        self.ax.annotate('', (self.tmp - 2, 0), xytext=(self.tmp + 2, 0),
                         arrowprops={'arrowstyle': '<-', 'color': 'blue', 'linewidth': 2})
        self.ax.spines['top'].set_color('none')

    def set_ax(self):
        self.tmp = max(abs(self.x0 + self.rx), abs(self.x0 - self.rx), abs(self.y0 + self.ry), abs(self.y0 - self.ry))
        self.tmp2 = int(self.tmp / 100) + 1
        self.tmp = self.tmp2 * 100
        plt.xlim(-1 * self.tmp, self.tmp)
        plt.ylim(-1 * self.tmp, self.tmp)
        plt.xticks(np.linspace(-1 * self.tmp, self.tmp, self.tmp2 * 2 + 1))
        plt.yticks(np.linspace(-1 * self.tmp, self.tmp, self.tmp2 * 2 + 1))

    def four_point(self):
        self.x.append(self.x0 + self.xk)
        self.y.append(self.y0 + self.yk)
        self.x.append(self.x0 - self.xk)
        self.y.append(self.y0 + self.yk)
        self.x.append(self.x0 + self.xk)
        self.y.append(self.y0 - self.yk)
        self.x.append(self.x0 - self.xk)
        self.y.append(self.y0 - self.yk)
        plt.pause(0.01)
        plt.scatter(self.x, self.y, s=1, color='black', marker='.')

    def start_draw(self):
        self.x0 = int(self.lineEdit_x.text())
        self.rx = int(self.lineEdit_rx.text())
        self.y0 = int(self.lineEdit_y.text())
        self.ry = int(self.lineEdit_ry.text())
        self.change_spines()
        self.rx2 = self.rx * self.rx
        self.ry2 = self.ry * self.ry
        self.x = []
        self.y = []
        self.xk = 0
        self.yk = self.ry

        self.d = 4 * self.ry2 - 4 * self.rx2 * self.ry + self.rx2
        while self.rx2 * (2 * self.yk - 1) >= 2 * self.ry2 * (self.xk + 1):
            self.four_point()
            if self.d < 0:
                self.d += 4 * self.ry2 * (2 * self.xk + 3)
            else:
                self.d = self.d + 4 * self.ry2 * (2 * self.xk + 3) - 8 * self.rx2 * (self.yk - 1)
                self.yk -= 1
            self.xk += 1
        self.four_point()

        self.xk = self.rx
        self.yk = 0
        self.d = 4 * self.rx2 - 4 * self.rx * self.ry2 + self.ry2
        while self.ry2 * (2 * self.xk - 1) > 2 * (self.rx2 * (self.yk - 1)):
            self.four_point()
            if self.d < 0:
                self.d += 4 * self.rx2 * (2 * self.yk + 3)
            else:
                self.d = self.d + 4 * self.rx2 * (2 * self.yk + 3) - 8 * self.ry2 * (self.xk - 1)
                self.xk -= 1
            self.yk += 1
        self.four_point()

        plt.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
