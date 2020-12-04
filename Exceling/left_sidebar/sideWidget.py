from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout


class SideWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.leftLayout = QVBoxLayout()

    def appendWidget(self, widget, align="nocenter"):
        if align == "center":
            self.leftLayout.addWidget(widget, alignment=QtCore.Qt.AlignHCenter)
        else:
            self.leftLayout.addWidget(widget)

    def setAsLayout(self):
        self.leftLayout.setSpacing(0)
        self.leftLayout.addStretch(5)
        self.leftLayout.setContentsMargins(0, 0, 0, 0)
        self.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.leftLayout)
