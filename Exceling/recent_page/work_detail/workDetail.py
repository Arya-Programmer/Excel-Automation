from PyQt5.QtWidgets import QLabel, QTabWidget, QWidget, QVBoxLayout, QHBoxLayout, QFrame
from .fields.fields import Fields

# from preview import Preview


class WorkDetail(QFrame):
    def __init__(self, parent=None, index=0):
        super().__init__(parent)
        self.parent = parent
        self.index = index
        self.cardDetailLayout = QTabWidget(self)
        self.cardDetailLayout.tabBar().setObjectName("cardTab")
        self.cardDetailLayout.setObjectName("cardTabPane")
        self.setObjectName("cardWidget")

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
            QWidget#cardWidget *{
                background: #141518;
            }
            #cardTabPane::pane{
                padding: 0;
            }
            #cardTab{
                font-family: Arial, sans-serif;
                font-weight: bold;
                font-size: 12px;
            }
            #cardTab::tab{
                background: #e4e6e8;
                height: 50px;
                width: 150px;
                color: white;
            }
            #cardTab::tab:selected{
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
        return Fields([
            ("hello", "Hi", "DropDown"),
            ("hello", "Hi", "DropDown"),
            ("hello", "Hi", "DropDown"),
            ("hello", "Hi", "DropDown"),
            ("hello", "Hi", "DropDown"),
            ("hello", "Hi", "DropDown"),
            ("hello", "Hi", "DropDown"),
            ("hello", "Hi", "DropDown"),
            ("hello", "Hi", "DropDown"),
            ("hello", "Hi", "DropDown"),
            ("hello", "Hi", "DropDown"),
            ("hello", "Hi", "DropDown"),
            ("hello", "Hi", "DropDown"),
            ("hello", "Hi", "DropDown"),
            ("hello", "Hi", "DropDown"),
            ("hello", "Hi", "DropDown"),
            ("hello", "Hi", "DropDown"),
            ("hello", "Hi", "DropDown"),
            ("hello", "Hi", "DropDown"),
            ("hello", "Hi", "DropDown"),
            ("hello", "Hi", "Text"),
            ("hello", "Hi", "DropDown"),
            ("hello", "Hi", "DropDown"),
            ("hello", "Hi", "DropDown"),
            ("hello", "Hi", "DropDown"),
            ("hello", "Hi", "DropDown"),
            ("hello", "Hi", "DropDown"),
            ("hello", "Hi", "DropDown"),
            ("hello", "Hi", "DropDown"),
            ("hello", "Hi", "DropDown"),
        ], self.parent)

    def lastInputClick(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('page 3'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main
