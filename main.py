import sys
from random import randint as rnd

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtGui, QtCore, QtWidgets


class Ui_CirclesForm(object):
    def setupUi(self, CirclesForm):
        CirclesForm.setObjectName("CirclesForm")
        CirclesForm.resize(334, 364)
        self.gridLayout = QtWidgets.QGridLayout(CirclesForm)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pb_draw_circles = QtWidgets.QPushButton(CirclesForm)
        self.pb_draw_circles.setObjectName("pb_draw_circles")
        self.horizontalLayout.addWidget(self.pb_draw_circles)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(CirclesForm)
        QtCore.QMetaObject.connectSlotsByName(CirclesForm)

    def retranslateUi(self, CirclesForm):
        _translate = QtCore.QCoreApplication.translate
        CirclesForm.setWindowTitle(_translate("CirclesForm", "CirclesForm"))
        self.pb_draw_circles.setText(_translate("CirclesForm", "Draw circles"))


class Circle:
    def __init__(self, x, y, rad):
        self.x, self.y, self.r = x, y, rad


class YellowCirclesForm(QWidget, Ui_CirclesForm):
    def __init__(self):
        super().__init__()

        self.circles = []

        self.painter = QPainter()

        self.init_ui()
        self.generate_circles()

    def init_ui(self):
        self.pb_draw_circles.clicked.connect(self.generate_circles)

    def generate_circles(self):
        self.circles.clear()
        for _ in range(10):
            self.circles.append(Circle(rnd(0, self.width()),
                                       rnd(0, self.height()),
                                       rnd(10, 100)
                                       ))

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter.begin(self)
        self.draw_circles()
        self.painter.end()

    def draw_circles(self):
        self.painter.setPen(QColor(rnd(0, 255), rnd(0, 255), rnd(0, 255)))
        for circle in self.circles:
            self.draw_circle(circle)
        self.update()

    def draw_circle(self, circle: Circle):
        self.painter.drawEllipse(circle.x - circle.r, circle.y - circle.r,
                                 2 * circle.r, 2 * circle.r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = YellowCirclesForm()
    wnd.show()
    sys.exit(app.exec())
