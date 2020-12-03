from PyQt5.QtWidgets import QWidget, QLabel, QFrame, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QFont
import cv2
import os


class Card(QFrame):
    def __init__(self, workTitle, workImage, workType, parent):
        super().__init__()
        self.parent = parent
        self.title = workTitle
        self.image = workImage
        self.type = workType

        children = QVBoxLayout(self)
        children.addWidget(Image(self.image))
        children.addWidget(Title(self.title))
        children.addWidget(Type(self.type))

        # children.setContentsMargins(30, 30, 30, 40)
        self.setMaximumSize(220, 300)
        self.setMinimumSize(215, 290)

        self.setLayout(
            children
        )
        self.design()

    def design(self):
        self.setStyleSheet(
            "height: 210px;"
            "color: white;"
            "background: rgb(8, 8, 8);"
            "border-radius: 10px;"
        )

    def mousePressEvent(self, event):
        self.parent.cardResponseClick()


class Image(QLabel):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setPixmap(self.imageStyle())

    def imageStyle(self):
        folder = r"C:\Users\1234\Programming\python\pyqt\PYQT5_V2\Exceling\static\images"
        imgPath = os.path.join(folder, self.image + ".jpg")
        img = QPixmap(imgPath)
        return img.scaled(170, 110)


class Title(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.text = text

        self.constrainTextLength()

        self.setMaximumSize(QtCore.QSize(16777215, 80))
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setFont(QFont("Arial", 20, 100))
        self.setText(self.text)
        self.setToolTip(text)

    def constrainTextLength(self):
        if len(self.text) > 10:
            self.text = self.text[:8] + "..."

class Type(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.text = text


        self.setMaximumSize((QtCore.QSize(16777215, 40)))
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setFont(QFont("Arial", 15))
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

