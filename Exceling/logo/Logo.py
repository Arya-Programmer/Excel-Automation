import os

from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QPainterPath, QPainter
from PyQt5.QtWidgets import QLabel, QFrame, QVBoxLayout


class Frame(QFrame):
    def __init__(self, image, height, width, left=10, top=10, right=10, bottom=45, antialiasing=True, parent=None):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(Logo(image, height, width, antialiasing, parent))
        self.setLayout(layout)

        self.setContentsMargins(left, top, right, bottom)


class Logo(QLabel):
    def __init__(self, image, height, width, antialiasing=True, parent=None):
        super().__init__(parent)
        self.image = image
        self.parent = parent
        self.Antialiasing = antialiasing
        self.heightInput = height
        self.widthInput = width
        self.setMaximumSize(self.widthInput, self.heightInput)
        self.setMinimumSize(self.widthInput, self.heightInput)
        self.radius = 850

        folder = r"C:\Users\1234\Programming\python\pyqt\PYQT5_V2\Exceling\static\images"
        imgPath = os.path.join(folder, self.image + ".jpg")

        self.target = QPixmap(self.size())
        self.target.fill(QtCore.Qt.transparent)

        p = QPixmap(imgPath).scaled(
            self.widthInput, self.heightInput, QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.SmoothTransformation)

        painter = QPainter(self.target)
        if self.Antialiasing:
            painter.setRenderHint(QPainter.Antialiasing, True)
            painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
            painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

        path = QPainterPath()
        path.addRoundedRect(
            0, 0, self.width(), self.height(), self.radius, self.radius)

        painter.setClipPath(path)
        painter.drawPixmap(0, 0, p)
        self.setPixmap(self.target)
        self.setAlignment(QtCore.Qt.AlignCenter)


