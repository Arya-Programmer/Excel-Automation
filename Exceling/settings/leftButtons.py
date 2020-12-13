from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton

from Exceling.globals.colors import ColorsBackend
from Exceling.logo.Logo import Frame
from Exceling.settings.changeColors import ChangeColors


class LeftButtons(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        mainLayout = QVBoxLayout()
        colors = ColorsBackend().sidebar()
        btn1 = Button(self, parent, colors, "Recent")
        btn2 = Button(self, parent, colors, "Add")
        btn3 = Button(self, parent, colors, "About")
        self.buttons = [btn1, btn2, btn3]
        mainLayout.addWidget(Frame("Image1", 80, 80, 5, 5, 5, 10), alignment=QtCore.Qt.AlignHCenter)
        mainLayout.addWidget(btn1)
        mainLayout.addWidget(btn2)
        mainLayout.addWidget(btn3)
        mainLayout.setSpacing(0)
        mainLayout.addStretch(5)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setContentsMargins(0, 0, 0, 0)

        self.setLayout(mainLayout)


class Button(QPushButton):
    def __init__(self, parent, grandparent, color, text):
        super().__init__(parent)
        self.grandparent = grandparent
        bg, textC, focused, hover = color
        self.setObjectName("rightButtons")
        self.setText(text)
        self.bg = bg
        self.textC = textC
        self.hover = hover
        self.focused = focused
        self.parent = parent
        self.change = ChangeColors("sidebar()")
        self.setFont(QFont("Arial", 17))
        self.setMinimumSize(90, 30)

        self.setContentsMargins(0, 0, 0, 0)
        if text != "Recent":
            self.setStyleSheet(
                self.getStyle(bg, textC, hover)
            )
        else:
            self.setStyleSheet(self.getStyle(focused, textC, focused))

    def getStyle(self, bg, text, hover):
        return """
            #rightButtons {{
                border: none;
                background: {};
                color: {};
            }}
            #rightButtons:hover {{
                background: {};
            }}
            """.format(bg, text, hover)

    def mousePressEvent(self, e):
        super().mousePressEvent(e)
        for button in self.parent.buttons:
            button.setStyleSheet(self.getStyle(self.bg, self.textC, self.hover))
        self.setStyleSheet(self.getStyle(self.focused, self.textC, self.focused))
        if self.text() == "Recent":
            self.grandparent.firstTab()

    def mouseDoubleClickEvent(self, event):
        if not self.change.isVisible():
            self.change.show()
