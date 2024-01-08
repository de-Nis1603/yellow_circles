import random
import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QPointF
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_file import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.activated = 'nothing'
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.activated = "circle"
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.activated == 'circle':
            painter = QPainter(self)
            r = random.randrange(256)
            g = random.randrange(256)
            b = random.randrange(256)
            painter.setBrush(QColor(r, g, b))
            radius = random.randrange(300)
            center_x = random.randrange(radius, self.width() - radius)
            center_y = random.randrange(radius, self.height() - radius)
            center = QPointF(center_x, center_y)
            painter.drawEllipse(center, radius, radius)
            self.activated = 'nothing'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())