from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QLabel

class cQlabel(QLabel):

    clicked = pyqtSignal()
    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.clicked.emit()

