import random
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt, QPointF


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.activated = 'nothing'
        self.pushButton.clicked.connect(self.run)
        self.resize(900, 700)

    def run(self):
        self.activated = "circle"
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.activated == 'circle':
            painter = QPainter(self)
            painter.setBrush(Qt.yellow)
            radius = random.randrange(300)
            center_x = random.randrange(radius, self.width() - radius)
            center_y = random.randrange(radius, self.height() - radius)
            print(0)
            center = QPointF(center_x, center_y)
            print(radius, center_x, center_y)
            painter.drawEllipse(center, radius, radius)
            self.activated = 'nothing'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())