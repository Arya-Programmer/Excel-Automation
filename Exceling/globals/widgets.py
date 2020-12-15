from PyQt5 import QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QDialogButtonBox, QComboBox, QTabWidget, QFrame
from .colors import ColorsBackend
from .variables import font


class Label(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text=text, parent=parent)
        self.setStyleSheet("")
        self.setFont(QFont(font, 10))

    def setStyleSheet(self, style):
        text = ColorsBackend().labels()[0]
        style += f"color: {text};"
        super().setStyleSheet(style)


class LineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("lineEdit")
        self.setFont(QFont(font, 10))
        bg, text, focused, line, hover = ColorsBackend().inputfields()
        self.setStyleSheet("""
            #lineEdit{{
                background: {};
                color: {};
                padding: 2px;
                border-top: none;
                border-right: none;
                border-left: none;
                border-bottom: 1.5px solid {};
            }}
            #lineEdit:focus{{
                background: {};
            }}
            #lineEdit:hover{{
                background: {};
            }}""".format(bg, text, line, focused, hover))


class PushButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("pushButton")
        self.setFont(QFont(font, 10))
        bg, text, hover = ColorsBackend().buttons()
        style = """
            #pushButton{{
                background: {};
                color: {};
                border: none;
                padding-top: 10px;
                padding-bottom: 10px;
            }}
            #pushButton:hover{{
                background: {};
            }}""".format(bg, text, hover)
        self.setStyleSheet(style)


class DialogBox(QDialogButtonBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("dialogBox")
        bg1, bg2, t1, t2, h1, h2 = ColorsBackend().dialogboxes()
        self.setStyleSheet("""
            #dialogBox *[text="Save"]{{
                background: {};
                color: {};
                padding: 8px 20px 8px 20px;
                border: none;
            }}
            #dialogBox *[text="Save"]:hover{{
                background: {};
            }}
            #dialogBox *[text="Cancel"]{{
                background: {};
                color: {};
                padding: 8px 20px 8px 20px;
                border: none;
            }}
            #dialogBox *[text="Cancel"]:hover{{
                background: {};
            }}
        """.format(bg1, t1, h1, bg2, t2, h2))


class ComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("comboBox")
        self.setFont(QFont(font, 10))
        bg, text, focused, line, hover = ColorsBackend().inputfields()
        self.setStyleSheet("""
            #comboBox::down-arrow{{
                image: url(globals/arrow.png);
                width: 10px;
                height: 10px;
            }}
            #comboBox::drop-down{{
                border: none;  
            }}
            #comboBox {{
                background: {};
                color: {};
                padding: 3px;
                border: none;
            }}
            #comboBox:hover {{
                background: {};
            }}
        """.format(bg, text, hover))


class TabWidget(QTabWidget):
    def __init__(self, parent=None, height=50, width=150):
        super().__init__(parent)
        self.height = height
        self.width = width
        self.setObjectName("tabWidget")
        self.tabBar().setObjectName("tabBar")

        bg, text, focused, hover = ColorsBackend().tabs()
        self.setStyleSheet("""
            #tabWidget::pane {{
                padding: 0;
            }}
            #tabBar::tab {{
                background: {};
                color: {};
                height: {};
                width: {};
                font-family: {}, sans-serif;
                font-weight: bold;
                font-size: 12px;
            }}
            #tabBar::tab:selected{{
                background: {};
            }}
            #tabBar::tab:selected:hover{{
                background: {};
            }}
            #tabBar::tab:hover {{
                background: {};
            }}
            #tabWidget::pane *{{
                color: {};
                background: {};
            }}
        """.format(bg, text, self.height, self.width, font, focused, focused, hover, focused, focused))


class Frame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("frame")
        bg, text, focused, hover = ColorsBackend().tabs()
        self.setStyleSheet("""
            #frame, #frame *{{
                background: {}
            }}
        """.format(focused))
