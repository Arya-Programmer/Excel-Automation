from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QFrame, QTabWidget, QHBoxLayout

from Exceling.globals.widgets import Frame
from Exceling.settings.LeftButtons import LeftButtons


class ColorWidgets(Frame):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.tabWidget = QTabWidget(self)
        self.tabWidget.setObjectName("tb")
        self.tabWidget.tabBar().setObjectName("tbt")
        self.buttons = LeftButtons()
        self.tabWidget.addTab(self.buttons, '')
        self.tabWidget.setStyleSheet('''
                       #tbt::tab {
                           width: 0; height: 0; margin: 0; padding: 0; border: none;
                       }
                       #tb::pane {
                            padding: 0px;
                       }
                       ''')

        layout.addWidget(self.tabWidget)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
