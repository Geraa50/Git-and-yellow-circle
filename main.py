import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5 import uic
import random


class Program(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.btn_generate.clicked.connect(self.paint)
        #  self.qp = QPainter(self)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()

            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        #  qp.setBrush(QColor(255, 255, 0))
        qp.setPen(QPen(Qt.yellow, 8, Qt.SolidLine))
        diametr = random.randrange(1, 1000)
        x, y = random.randrange(1, 800), random.randrange(1, 600)
        qp.drawEllipse(x, y, diametr, diametr)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Program()
    ex.show()
    sys.exit(app.exec_())
