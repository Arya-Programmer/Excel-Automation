from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton

from Exceling.globals.colors import ColorsBackend


class LeftWidget(QPushButton):
    def __init__(self, text, parent):
        super().__init__()
        bg, textC, focused, hover = ColorsBackend().sidebar()
        self.textColor = textC
        self.focused = focused
        self.bg = bg
        self.hover = hover
        self.text = text
        self.parent = parent

        self.setObjectName("leftWidget")
        self.setText(self.text)
        self.setFont(QFont("Arial", 17))
        self.setMinimumSize(150, 50)
        if text.lower() == "recent":
            self.setStyleSheet(self.getStyle(focused, self.focused))
        else:
            self.setStyleSheet(self.getStyle(bg, self.hover))

    def getStyle(self, color, color2):
        return (
            """
            #leftWidget{{
            color: {};
            background: {};
            border: none;
            }}
            #leftWidget:hover{{
                background: {}
            }}
            """.format(self.textColor, color, color2)
        )

    def getDefinedButtons(self):
        definedButtons = [self.parent.recentMenuButton, self.parent.addMenuButton, self.parent.aboutMenuButton]
        return definedButtons

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        for button in (self.getDefinedButtons()):
            button.setStyleSheet(self.getStyle(self.bg, self.hover))
        self.setStyleSheet(self.getStyle(self.focused, self.focused))

