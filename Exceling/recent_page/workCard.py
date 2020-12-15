from PyQt5.QtWidgets import QLabel, QFrame, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from PyQt5.QtGui import QFont
import os

from Exceling.globals.colors import ColorsBackend
from Exceling.globals.variables import imageFolder, font


class Card(QFrame):
    def __init__(self, oid, id, workTitle, workImage, workType, parent, main):
        super().__init__()
        self.setObjectName("card")
        self.oid = oid
        self.id = id
        self.main = main
        self.parent = parent
        self.title = workTitle
        self.image = workImage
        self.type = workType

        bg, text, hover = ColorsBackend().cards()

        children = QVBoxLayout(self)
        children.addWidget(Image(self.image))
        children.addWidget(Title(self.title, text))
        children.addWidget(Type(self.type))

        # children.setContentsMargins(30, 30, 30, 40)
        self.setMaximumSize(220, 300)
        self.setMinimumSize(215, 290)

        self.setLayout(
            children
        )

        self.setStyleSheet("""
            #card, #card>*{{
                height: 210px;
                color: {};
                background: {};
                border-radius: 10px;
            }}
        """.format(text, bg))

    def mousePressEvent(self, event):
        # print(self.oid)
        # page = self.main.rightSidebar.children()[0].children()[self.oid]
        # print(self.main.rightSidebar.indexOf(page))
        self.main.cardResponseClick(self.id)


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
        return img.scaled(170, 110)


class Title(QLabel):
    def __init__(self, text, color, parent=None):
        super().__init__(parent)
        self.text = text

        self.constrainTextLength()

        self.setMaximumSize(QtCore.QSize(16777215, 80))
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setFont(QFont(font, 20, 100))
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
        self.setFont(QFont(font, 15))
        self.setText(text)

        self.changeColor()

    def changeColor(self):

        color = "orange"
        if self.text.lower() == "excel":
            color = "green"
        elif self.text.lower() == "word":
            color = "#1553b5"
        elif self.text.lower() == "access":
            color = "#a01a29"
        self.setStyleSheet(f"color: {color};")
