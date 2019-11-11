import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic


class Circle:
    def __init__(self, x, y, rad):
        self.x, self.y, self.r = x, y, rad


class YellowCirclesForm(QWidget):
    def __init__(self):
        super().__init__()
        uic.load('UI.ui', self)



        self.init_ui()

    def init_ui(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = YellowCirclesForm()
    wnd.show()
    sys.exit(app.exec())
