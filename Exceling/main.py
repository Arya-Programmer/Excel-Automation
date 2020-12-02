from PyQt5.QtWidgets import *
import sys
from recentPage.recentWidget import RecentView
from leftSidebar.SideBar import SideWidget
from leftSidebar.LeftSideWidget import LeftWidget
from addPage.addWidget import AddView


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # set the title of main window
        self.setWindowTitle('Exceling')

        # set the size of window
        self.screenWidth = 800
        self.screenHeight = int(0.618 * self.screenWidth)
        self.resize(self.screenWidth, self.screenHeight)

        # add all widgets
        self.recentMenuButton = LeftWidget("Recent", self)
        self.addMenuButton = LeftWidget("Add", self)
        self.aboutMenuButton = LeftWidget("About", self)

        self.recentMenuButton.clicked.connect(self.recentClick)
        self.addMenuButton.clicked.connect(self.addClick)
        self.aboutMenuButton.clicked.connect(self.aboutClick)

        # add tabs
        self.tab1 = self.ui1()
        self.tab2 = self.ui2()
        self.tab3 = self.ui3()

        self.initUI()

    def initUI(self):
        self.setStyleSheet(
            """
            background: #2a292e;
            """
        )

        self.leftWidget = SideWidget()
        self.leftWidget.appendWidget(self.recentMenuButton)
        self.leftWidget.appendWidget(self.addMenuButton)
        self.leftWidget.appendWidget(self.aboutMenuButton)
        self.leftWidget.setAsLayout()

        self.rightSidebar = QTabWidget()
        self.rightSidebar.tabBar().setObjectName("mainTab")

        self.rightSidebar.addTab(self.tab1, '')
        self.rightSidebar.addTab(self.tab2, '')
        self.rightSidebar.addTab(self.tab3, '')

        self.rightSidebar.setCurrentIndex(0)
        self.rightSidebar.setStyleSheet('''
            QTabBar::tab{
                width: 0;
                height: 0; margin: 0; padding: 0; border: none;
            }
            QTabWidget::pane { 
                 margin: 0px,1px,1px,1px;
                 border: 2px solid #141518;
                 padding: 0px;
            }
            ''')

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.leftWidget)
        main_layout.addWidget(self.rightSidebar)
        main_layout.setStretch(0, 40)
        main_layout.setStretch(1, 200)
        main_layout.setSpacing(0)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    # -----------------
    # buttons

    def recentClick(self):
        self.rightSidebar.setCurrentIndex(0)

    def addClick(self):
        self.rightSidebar.setCurrentIndex(1)

    def aboutClick(self):
        self.rightSidebar.setCurrentIndex(2)

    # -----------------
    # pages

    def ui1(self):
        return RecentView()

    def ui2(self):
        return AddView()

    def ui3(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('page 3'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())