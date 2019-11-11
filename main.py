import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic


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
