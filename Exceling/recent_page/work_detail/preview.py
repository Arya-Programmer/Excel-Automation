import os

from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QHBoxLayout

from Exceling.backend.createExcel import CreateExcel
from Exceling.globals.variables import imageFolder


class Preview(QWidget):
    def __init__(self, id):
        super().__init__()
        excel = CreateExcel()
        work = excel.getAllById("WORK", id)
        oid, title, type, folderPath, sheetName, firstCol, rowNum = work[0]

        self.mainLayout = QVBoxLayout()
        self.header(title, type, "blue")
        self.mainLayout.addWidget(Image(title, self))

        self.setLayout(self.mainLayout)

    def header(self, title, type, color):
        horizontalLay = QHBoxLayout()
        horizontalLay.addWidget(Title(title, color))
        horizontalLay.addWidget(Type(type))

        horLayWidget = QWidget()
        horLayWidget.setLayout(horizontalLay)

        self.mainLayout.addWidget(horLayWidget)


class Image(QLabel):
    def __init__(self, image, parent):
        super().__init__()
        self.image = image
        self.parent = parent
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setPixmap(self.imageStyle())

    def imageStyle(self):
        folder = imageFolder
        imgPath = os.path.join(folder, self.image + ".png")
        img = QPixmap(imgPath)
        return img


class Title(QLabel):
    def __init__(self, text, color, parent=None):
        super().__init__(parent)
        self.text = text

        self.setMaximumSize(QtCore.QSize(16777215, 80))
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setFont(QFont("Arial", 30, 100))
        self.setText(self.text)
        self.setStyleSheet(
            f"color: {color}"
        )


class Type(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.text = text

        # self.setMaximumSize((QtCore.QSize(30, 40)))
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setFont(QFont("Arial", 25))
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
