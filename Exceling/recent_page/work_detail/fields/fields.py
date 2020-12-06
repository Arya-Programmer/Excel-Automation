from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit, QComboBox, QVBoxLayout, QScrollArea

from Exceling.globals.variables import options
from Exceling.globals.comboBoxType import ComboBoxType


class Fields(QScrollArea):
    def __init__(self, datas, parent=None):
        super().__init__(parent)
        self.setObjectName("scrollBar")
        self.setStyleSheet(self.getStyle())
        mainWidget = QWidget()

        self.mainLayout = QVBoxLayout()
        for field, data, types in datas:
            widget = QWidget()
            widget.setLayout(self.column(field, data, types))
            self.mainLayout.addWidget(widget)

        self.buttonBox = QtWidgets.QDialogButtonBox()
        self.buttonBox.setGeometry(QtCore.QRect(630, 530, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("dialogBox")
        self.mainLayout.addWidget(self.buttonBox)

        self.buttonBox.accepted.connect(lambda: FieldsChanges(self))
        self.buttonBox.rejected.connect(lambda: parent.recentClick())

        mainWidget.setLayout(self.mainLayout)

        # Scroll Area Properties
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)
        self.setWidget(mainWidget)

    def column(self, field, data, type):
        layout = QHBoxLayout()
        layout.addWidget(QLabel(field + ":"))

        lineEdit = QLineEdit()
        lineEdit.setText(data)
        layout.addWidget(lineEdit)

        layout.addWidget(QLabel("Type:"))

        comboBox = ComboBoxType(data, 1, 5, 4, layout)
        for dataType in list(options.keys()):
            comboBox.addItem(dataType)
        comboBox.setCurrentIndex(options[type])

        layout.addWidget(comboBox)
        return layout

    def getStyle(self):
        return ("""
            #dialogBox *,
            #scrollBar QComboBox *,
            #scrollBar QComboBox,
            #scrollBar QLineEdit,
            #scrollBar QCheckBox{
                background: #e4e6e8;
            }
            QLabel {
                color: white;
            }
            #scrollBar{
                border: none;
            }
        """)


class FieldsChanges:
    def __init__(self, main):
        self.main = main
        self.layout = self.main.mainLayout
        print(self.getChange())

    def getChange(self):
        items = [self.layout.itemAt(i) for i in range(self.layout.count() - 1)]

        lst = []
        for item in items:
            layout = item.widget().children()
            tpl = tuple()
            tpl += (layout[1].text()[:-1],)

            if isinstance(layout[2], QComboBox):
                tpl += (self.getCombo(layout[2], "choice"),)
            elif isinstance(layout[2], QLineEdit):
                tpl += (self.getLineEdit(layout[2]),)

            if isinstance(layout[4], QComboBox):
                tpl += (self.getCombo(layout[4], "type"),)
            elif isinstance(layout[4], QLineEdit):
                tpl += (self.getLineEdit(layout[4]),)

            lst.append(tpl)

        return lst

    def getCombo(self, widget, skip):
        if skip == "choice":
            return [widget.itemText(item) for item in range(widget.count() - 1)]
        if skip == "type":
            return [widget.itemText(item) for item in range(widget.count())]

    def getLineEdit(self, lineEdit):
        return lineEdit.text()

    def getCheckButton(self, checkBtn):
        if checkBtn.isChecked():
            return "False"
        elif not checkBtn.isChecked:
            return "True"
