from PyQt5.QtWidgets import QWidget, QVBoxLayout
from .LeftSideWidget import LeftWidget


class SideWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.leftLayout = QVBoxLayout()

    def appendWidget(self, widget):
        self.leftLayout.addWidget(widget)

    def setAsLayout(self):
        self.leftLayout.setSpacing(0)
        self.leftLayout.addStretch(5)
        self.leftLayout.setContentsMargins(0, 10, 0, 0)
        self.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.leftLayout)
