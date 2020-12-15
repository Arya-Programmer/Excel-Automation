from PyQt5.QtWidgets import QLabel, QFrame, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from PyQt5.QtGui import QFont
import os

from ..globals.colors import ColorsBackend
from ..globals.variables import font


class Card(QFrame):
    def __init__(self, id, workTitle, workImage, parent):
        super().__init__()
        self.setObjectName("card")
        self.parent = parent
        self.title = workTitle
        self.image = workImage
        self.id = id

        bg, text, hover = ColorsBackend().cards()

        children = QVBoxLayout(self)
        children.addWidget(Image(self.image))
        children.addWidget(Title(self.title))

        # children.setContentsMargins(30, 30, 30, 40)
        self.setMaximumSize(220, 300)
        self.setMinimumSize(215, 290)

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

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.parent.addResponseClick()



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
        if self.image == "Image3":
            return img.scaled(180, 130)
        else:
            return img.scaled(130, 100)


class Title(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(parent)

        self.setMaximumSize(QtCore.QSize(16777215, 80))
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setFont(QFont(font, 19, 100))
        self.setText(text)

