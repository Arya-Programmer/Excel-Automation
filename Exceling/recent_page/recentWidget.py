from PyQt5 import sip
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QFrame, QGridLayout, QLabel
from .workCard import Card


class RecentView(QFrame):
    def __init__(self, num, parent=None):
        super().__init__(parent)
        self.parent = parent

        self.cardLayout = QGridLayout(self)
        self.repeat = num

        self.reSetLayout()

        self.setLayout(self.cardLayout)

        self.setStyleSheet(
            "background-color: #141518;"
        )

    def deleteLayout(self):
        if self.cardLayout is not None:
            while self.cardLayout.count():
                item = self.cardLayout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.deleteLayout(item.layout())
            sip.delete(self.cardLayout)

    def reSetLayout(self):
        for i in range(2):
            for j in range(self.repeat):
                self.cardLayout.addWidget(Card("WorkNamea", "image1", "Excel", self.parent), i, j)
        self.setLayout(self.cardLayout)
