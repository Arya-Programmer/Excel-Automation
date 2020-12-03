from PyQt5.QtWidgets import QLabel, QTabWidget, QWidget, QVBoxLayout, QHBoxLayout


# from preview import Preview


class WorkDetail(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cardDetailLayout = QTabWidget(self)
        self.cardDetailLayout.tabBar().setObjectName("cardTab")

        self.initUI()

    def initUI(self):
        tab1 = self.previewClick()
        tab2 = self.addClick()
        tab3 = self.fieldsClick()
        tab4 = self.lastInputClick()

        self.cardDetailLayout.addTab(tab1, 'Preview')
        self.cardDetailLayout.addTab(tab2, 'Last Input')
        self.cardDetailLayout.addTab(tab3, 'Fields')
        self.cardDetailLayout.addTab(tab4, 'Add')
        self.cardDetailLayout.setCurrentIndex(0)

        self.setStyleSheet("""
            #cardTab::pane{
                background: #141518;
            }
            #cardTab::tab{
                background: #141518;
            }
        """)

        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.cardDetailLayout)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)

        self.setLayout(mainLayout)

    def previewClick(self):
        return QWidget()

    def addClick(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('page 3'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def fieldsClick(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('page 3'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def lastInputClick(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('page 3'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main
