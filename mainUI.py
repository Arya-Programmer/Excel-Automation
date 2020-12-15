from PyQt5.QtWidgets import *
import sys

from Exceling.add_page.addWidget import AddView
from Exceling.backend.createExcel import CreateExcel
from Exceling.globals.colors import ColorsBackend
from Exceling.globals.widgets import Label, PushButton
from Exceling.left_sidebar.leftWidget import LeftWidget
from Exceling.left_sidebar.sideWidget import SideWidget
from Exceling.logo.Logo import Frame

from Exceling.add_page.addWork import AddWork
from Exceling.recent_page.recentWidget import RecentView
from Exceling.recent_page.work_detail.workDetail import WorkDetail
from Exceling.settings.colorChanger import ColorChanger


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

        self.colorChanger = ColorChanger()
        # add tabs
        self.addTabs()

        # done means: the design already fixed for for the defined number
        self.done = None

        self.initUI()

    def initUI(self):
        background = ColorsBackend().window()
        self.setStyleSheet(
            "background: {};".format(background[0])
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
        self.tab1 = self.recentWidgetResponse(3)
        self.tab2 = self.ui2()
        self.tab3 = self.ui3()
        self.tab4 = self.addResponse()

    # UI
    def rightSidebarInit(self):
        self.rightSidebar = QTabWidget()
        self.rightSidebar.tabBar().setObjectName("mainTab")
        self.rightSidebar.setObjectName("mainTabWidget")

        self.rightSidebar.addTab(self.tab1, '')
        self.rightSidebar.addTab(self.tab2, '')
        self.rightSidebar.addTab(self.tab3, '')
        self.rightSidebar.addTab(self.tab4, '')

        excel = CreateExcel()
        ids = excel.getId("WORK")
        for id in list(ids):
            widget = self.cardResponse(int(id[0]))
            self.rightSidebar.addTab(widget, str(id[0]))

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

    def addClick(self):
        self.rightSidebar.setCurrentIndex(1)

    def aboutClick(self):
        self.rightSidebar.setCurrentIndex(2)

    def addResponseClick(self):
        self.rightSidebar.setCurrentIndex(3)

    def cardResponseClick(self, widget):
        self.rightSidebar.setCurrentIndex(widget + 4)

    # -----------------
    # pages

    def addResponse(self):
        return AddWork(self)

    def cardResponse(self, id):
        return WorkDetail(id, self)

    def recentWidgetResponse(self, num):
        return RecentView(2, self)

    def ui2(self):
        return AddView(self)

    def ui3(self):
        self.button = PushButton()
        self.button.setText("Click!")
        self.button.clicked.connect(self.showWidget)
        return self.button

    def showWidget(self):
        if not self.colorChanger.isVisible():
            self.colorChanger.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
