from PyQt5 import sip
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QFrame, QGridLayout, QScrollArea, QWidget
from .workCard import Card
from Exceling.backend.createExcel import CreateExcel
from Exceling.globals.flowLayout import FlowLayout

# container = QWidget()
# container_layout = QVBoxLayout()
# for i in range(2):
#     groupBox = QGroupBox(f'Group {i}')
#
#     flowLayout = FlowLayout(margin=10)
#     flowLayout.heightChanged.connect(container.setMinimumHeight)
#
#     groupBox.setLayout(flowLayout)
#
#     flowLayout.addWidget(QPushButton('Short'))
#     flowLayout.addWidget(QPushButton('Longer'))
#     flowLayout.addWidget(QPushButton('Different text'))
#     flowLayout.addWidget(QPushButton('More text'))
#     flowLayout.addWidget(QPushButton('Even longer button text'))
#     container_layout.addWidget(groupBox)
# container_layout.addStretch()
# container.setLayout(container_layout)
#
# w = QScrollArea()
# w.setWindowTitle('Flow Layout')
# w.setWidgetResizable(True)
# w.setWidget(container)
# w.show()
from ..globals.widgets import Frame


class RecentView(QScrollArea):
    def __init__(self, num=2, parent=None):
        super().__init__(parent)
        self.parent = parent

        self.mainWidget = Frame()

        self.cardLayout = FlowLayout(self, margin=10)
        # self.cardLayout.heightChanged.connect(self.mainWidget.setMinimumHeight)
        self.repeat = num


        self.setStyleSheet(
            "border: none;"
        )
        self.reSetLayout()
        self.mainWidget.setLayout(self.cardLayout)

        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)


        self.setWidget(self.mainWidget)

    def deleteLayout(self):
        if self.cardLayout is not None:
            while self.cardLayout.count():
                item = self.cardLayout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.deleteLayout(item.layout())
            sip.delete(self.cardLayout)

    def reSetLayout(self):
        excel = CreateExcel()
        ids = excel.getAll("WORK")
        # ['Hello', 'C:/Users/1234/Desktop', 1, 'Month Name', 'Date', 'Excel']
        for num, work in enumerate(ids):
            oid, title, type, loc, sheetName, firstcol, rowNum = work
            oid = int(oid)
            self.cardLayout.addWidget(Card(oid, num, title, title, type, self, self.parent))
