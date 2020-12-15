from PyQt5.QtWidgets import QMessageBox

from Exceling.globals.colors import ColorsBackend


class MessageBox(QMessageBox):
    def __init__(self, iconType, text, title):
        super().__init__()
        self.setIcon(eval("QMessageBox." + iconType.capitalize()))
        self.setText(text)
        self.setWindowTitle(title)
        self.setStandardButtons(QMessageBox.Ok)
        bg = ColorsBackend().window()
        bgbtn, text, hover = ColorsBackend().buttons()
        self.setStyleSheet("""
                #messageBox{{
                    background: {};
                }}
                #messageBox *[text="Ok"]{{
                    background: {};
                    color: {};
                }}
                #messageBox *[text="Ok"]:hover{{
                    background: {};
                }}
        """.format(bg, bgbtn, text, hover))
