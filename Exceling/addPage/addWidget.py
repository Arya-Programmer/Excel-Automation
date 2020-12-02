from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QLabel
from .addCard import Card


class AddView(QFrame):
    def __init__(self):
        super().__init__()
        main_layout = QHBoxLayout(self)
        main_layout.addWidget(Card("Add New Work", "image2", self))
        main_layout.addWidget(Title("OR"))
        main_layout.addWidget(Card("Automate Work", "Image3", self))
        self.setLayout(main_layout)

        self.setStyleSheet(
            "background-color: #141518;"
        )


class Title(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(parent)

        self.setMaximumSize(QtCore.QSize(16777215, 80))
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setFont(QFont("Arial", 40, 200))
        self.setText(text)

