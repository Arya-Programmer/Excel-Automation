from asyncio import sleep

from Exceling.settings.changeColors import ChangeColors

from PyQt5.QtWidgets import QLabel, QFrame, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QFont
import os

from Exceling.globals.colors import ColorsBackend
from Exceling.globals.variables import imageFolder, font


class CardColor(QFrame):
    def __init__(self, parent, main):
        super().__init__(parent)
        self.setObjectName("card")
        self.main = main
        self.title = "Title"
        self.image = "Image1"
        self.type = "Excel"

        bg, text, hover = ColorsBackend().cards()
        print(bg, text)

        children = QVBoxLayout(self)
        children.addWidget(Image(self.image))
        children.addWidget(Title(self.title, text))
        children.addWidget(Type(self.type))

        self.setMaximumSize(220, 300)
        self.setMinimumSize(110, 130)
        self.change = ChangeColors("cards()")

        self.setLayout(
            children
        )

        self.setStyleSheet("""
            #card, #card>*{{
                color: {};
                background: {};
                border-radius: 10px;
            }}
        """.format(text, bg))

    def mouseReleaseEvent(self, event):
        if self.main != "dont work":
            self.main.secondTab()

    def mouseDoubleClickEvent(self, e):
        if not self.change.isVisible():
            self.change.show()

class Image(QLabel):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setPixmap(self.imageStyle())

    def imageStyle(self):
        folder = imageFolder
        imgPath = os.path.join(folder, self.image + ".png")
        img = QPixmap(imgPath)
        return img.scaled(120, 70)


class Title(QLabel):
    def __init__(self, text, color, parent=None):
        super().__init__(parent)
        self.text = text

        self.constrainTextLength()

        self.setMaximumSize(QtCore.QSize(16777215, 80))
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setFont(QFont(font, 15, 100))
        self.setText(self.text)
        self.setToolTip(text)
        self.setStyleSheet(f"color: {color}")

    def constrainTextLength(self):
        if len(self.text) > 10:
            self.text = self.text[:8] + "..."

class Type(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.text = text

        self.setMaximumSize((QtCore.QSize(16777215, 40)))
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setFont(QFont(font, 10))
        self.setText(text)

        self.changeColor()

    def changeColor(self):
        palette = QtGui.QPalette()
        color = "orange"
        if self.text.lower() == "excel":
            color = "green"
        elif self.text.lower() == "word":
            color = "#1553b5"
        elif self.text.lower() == "access":
            color = "#a01a29"
        self.setStyleSheet(f"color: {color};")

