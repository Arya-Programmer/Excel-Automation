from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton


class LeftWidget(QPushButton):
    def __init__(self, text, parent):
        super().__init__()
        self.text = text
        self.parent = parent

        self.setText(self.text)
        self.setFont(QFont("Arial", 17))
        self.setMinimumSize(150, 50)
        if text.lower() == "recent":
            self.setStyleSheet(self.getStyle("#141518"))
        else:
            self.setStyleSheet(self.getStyle("#e4e6e8"))

    def getStyle(self, color):
        return (
            "color: white;"
            "border: none;"
            f"background: {color};"
        )

    def getDefinedButtons(self):
        definedButtons = [self.parent.recentMenuButton, self.parent.addMenuButton, self.parent.aboutMenuButton]
        return definedButtons

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        for button in (self.getDefinedButtons()):
            button.setStyleSheet(self.getStyle("#e4e6e8"))
        self.setStyleSheet(self.getStyle("#141518"))

