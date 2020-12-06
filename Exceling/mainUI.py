from PyQt5 import QtCore
from PyQt5.QtWidgets import *
import sys
from recent_page.recentWidget import RecentView
from left_sidebar.sideWidget import SideWidget
from left_sidebar.leftWidget import LeftWidget
from add_page.addWidget import AddView
from recent_page.work_detail.workDetail import WorkDetail
from Exceling.logo.Logo import Frame

from Exceling.add_page.addWork import AddWork


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # set the title of main window
        self.setWindowTitle('Exceling')

        # set the size of window
        self.screenWidth = 800
        self.screenHeight = int(0.618 * self.screenWidth)
        self.resize(self.screenWidth, self.screenHeight)

        # add all left side widgets, LeftWidget defined in left_sidebar
        self.recentMenuButton = LeftWidget("Recent", self)
        self.addMenuButton = LeftWidget("Add", self)
        self.aboutMenuButton = LeftWidget("About", self)
        # the logo of in the right side
        self.logo = Frame("image1", 150, 150, parent=self)

        # on button click change the tabs
        self.recentMenuButton.clicked.connect(self.recentClick)
        self.addMenuButton.clicked.connect(self.addClick)
        self.aboutMenuButton.clicked.connect(self.aboutClick)

        # add tabs
        self.addTabs()

        # done means: the design already fixed for for the defined number
        self.done = None

        self.initUI()

    def initUI(self):
        self.setStyleSheet(
            """
            background: #2a292e;
            """
        )

        # SideWidget is the left side horizontal layout
        # SideWidget is a QWidget appendWidget adds widget to the
        # layout that is initialized in SideWidget
        self.leftWidget = SideWidget()
        # appendWidget is a alternative of addWidget
        self.leftWidget.appendWidget(self.logo, "center")
        self.leftWidget.appendWidget(self.recentMenuButton)
        self.leftWidget.appendWidget(self.addMenuButton)
        self.leftWidget.appendWidget(self.aboutMenuButton)
        # setAsLayout = setLayout
        self.leftWidget.setAsLayout()

        # the right side horizontal bar
        self.rightSidebarInit()

        # put both layout on a vertical layout in the main layout
        self.mainLayoutInit()

    def addTabs(self):
        self.tab1 = self.ui1(3)
        self.tab2 = self.ui2()
        self.tab3 = self.ui3()
        self.tab4 = self.cardResponse(1)
        self.tab5 = self.addResponse()

    # UI
    def rightSidebarInit(self):
        self.rightSidebar = QTabWidget()
        self.rightSidebar.tabBar().setObjectName("mainTab")
        self.rightSidebar.setObjectName("mainTabWidget")

        self.rightSidebar.addTab(self.tab1, '')
        self.rightSidebar.addTab(self.tab2, '')
        self.rightSidebar.addTab(self.tab3, '')
        self.rightSidebar.addTab(self.tab4, '')
        self.rightSidebar.addTab(self.tab5, '')

        self.rightSidebar.setCurrentIndex(0)
        self.rightSidebar.setStyleSheet('''
                       #mainTab::tab {
                           width: 0; height: 0; margin: 0; padding: 0; border: none;
                       }
                       #mainTabWidget::pane {
                            padding: 0px;
                       }
                       ''')

    def mainLayoutInit(self):
        self.main_layout = QHBoxLayout()
        # main_layout.addWidget(self.logo, QtCore.Qt.AlignCenter)
        self.main_layout.addWidget(self.leftWidget)
        self.main_layout.addWidget(self.rightSidebar)
        self.main_layout.setStretch(0, 40)
        self.main_layout.setStretch(1, 200)
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        main_widget = QWidget()
        main_widget.setLayout(self.main_layout)
        self.setCentralWidget(main_widget)

    # -----------------
    # buttons

    def recentClick(self):
        self.rightSidebar.setCurrentIndex(0)
        self.resizeEvent("NO Event")

    def addClick(self):
        self.rightSidebar.setCurrentIndex(1)

    def aboutClick(self):
        self.rightSidebar.setCurrentIndex(2)

    def cardResponseClick(self):
        self.rightSidebar.setCurrentIndex(3)

    def addResponseClick(self):
        self.rightSidebar.setCurrentIndex(4)

    # -----------------
    # pages

    def addResponse(self):
        return AddWork(self)

    def cardResponse(self, id):
        return WorkDetail(self, id)

    def ui1(self, num):
        return RecentView(num, self)

    def ui2(self):
        return AddView(self)

    def ui3(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('page 3'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def resizing(self, num):
        if self.tab1.layout():
            self.tab1.deleteLayout()
        self.addTabs()
        self.tab1 = self.ui1(num)
        self.tab1.reSetLayout()
        self.rightSidebarInit()
        self.mainLayoutInit()

    def resizeEvent(self, event):
        try:
            super().resizeEvent(event);
        except Exception:
            "do nothing";
        if self.rightSidebar.currentIndex() == 0:
            if self.width() > 1315 and self.done != 1315:
                self.resizing(5)
                self.update()
                self.tab1.update()
                self.done = 1315
            elif 1315 > self.width() > 1100 and self.done != 1000:
                self.resizing(4)
                self.update()
                self.tab1.update()
                self.done = 1000
            elif 1100 > self.width() > 870 and self.done != 900:
                self.resizing(3)
                self.update()
                self.tab1.update()
                self.done = 900
            elif 870 > self.width() > 800 and self.done != 800:
                self.resizing(2)
                self.update()
                self.tab1.update()
                self.done = 800



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
