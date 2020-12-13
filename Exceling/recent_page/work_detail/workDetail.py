from PyQt5.QtWidgets import QTabWidget, QWidget, QVBoxLayout, QHBoxLayout, QFrame

from .add import Add
from .fields.fields import Fields

# from preview import Preview
from Exceling.backend.createExcel import CreateExcel
from .lastInput import LastInput
from .preview import Preview
from ...globals.widgets import TabWidget, Frame


class WorkDetail(Frame):
    def __init__(self, oid, parent=None):
        super().__init__(parent)
        self.main = parent
        self.oid = oid

        self.excel = CreateExcel()
        work = self.excel.getAllById("WORK", self.oid)
        self.title = work[0][1]
        self.limit = work[0][-1]

        self.cardDetailLayout = TabWidget(self)
        # self.cardDetailLayout.tabBar().setObjectName("cardTab")
        # self.cardDetailLayout.setObjectName("cardTabPane")
        self.setObjectName("cardWidget")

        self.initUI()

    def initUI(self):
        self.tab1 = self.previewClick()
        self.tab2 = self.lastInputClick()
        self.tab3 = self.fieldsClick()
        self.tab4 = self.addClick()

        self.cardDetailLayout.addTab(self.tab1, 'Preview')
        self.cardDetailLayout.addTab(self.tab2, 'Last Input')
        self.cardDetailLayout.addTab(self.tab3, 'Fields')
        self.cardDetailLayout.addTab(self.tab4, 'Add')
        self.cardDetailLayout.setCurrentIndex(0)

        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.cardDetailLayout)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)

        self.setLayout(mainLayout)

    def previewClick(self):
        return Preview(self.oid)

    def addClick(self):
        return Add(self.title, self.limit, self.oid, self.main, self)

    def fieldsClick(self):
        fields = self.excel.getTheLast(self.limit, "FIELDS", self.title)
        return Fields(fields, self.main, self)

    def lastInputClick(self):
        return LastInput(self.oid, self.title, self.limit, self)


    def updatePreview(self):
        self.tab1 = self.previewClick()
        self.cardDetailLayout.removeTab(0)
        self.cardDetailLayout.insertTab(0, self.tab1, "Preview")

    def updateAdd(self):
        self.tab4 = self.addClick()
        self.cardDetailLayout.removeTab(3)
        self.cardDetailLayout.insertTab(3, self.tab4, "Add")

    def updateLastInput(self):
        self.tab2 = self.addClick()
        self.cardDetailLayout.removeTab(1)
        self.cardDetailLayout.insertTab(1, self.tab2, "Last Input")
