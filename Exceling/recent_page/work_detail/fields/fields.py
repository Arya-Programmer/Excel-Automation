from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QComboBox, QVBoxLayout, QScrollArea, QCheckBox, QSpinBox

from Exceling.backend.createExcel import CreateExcel
from Exceling.globals.variables import options
from Exceling.globals.comboBoxType import ComboBoxType, AnswerCombo
from Exceling.globals.widgets import Label, LineEdit, DialogBox


class Fields(QScrollArea):
    def __init__(self, datas, main, parent):
        super().__init__()
        self.main = main
        mainWidget = QWidget()

        self.mainLayout = QVBoxLayout()
        for oid, workTitle, fieldName, type, fieldData, formula in datas:
            widget = QWidget()
            widget.setLayout(self.column(fieldName, fieldData, type, formula))
            self.mainLayout.addWidget(widget)

        self.title = workTitle

        self.buttonBox = DialogBox()
        self.buttonBox.setGeometry(QtCore.QRect(630, 530, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Save)
        self.mainLayout.addWidget(self.buttonBox)

        self.buttonBox.accepted.connect(lambda: self.getChanges(parent))
        self.buttonBox.rejected.connect(lambda: self.main.recentClick())

        mainWidget.setLayout(self.mainLayout)

        # Scroll Area Properties
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)
        self.setWidget(mainWidget)
        self.setStyleSheet("border: none;")
        
    def getChanges(self, parent):
        FieldsChanges(self, parent)


    def column(self, field, data, type, formula):
        verticalLayout = QVBoxLayout()
        firstRow = QHBoxLayout()
        firstRow.addWidget(Label(field + ":"))
        lineEdit = LineEdit()
        lineEdit.setText(data)
        firstRow.addWidget(lineEdit)

        firstRow.addWidget(Label("Type:"))

        # turn "('1', '2', '3', '4', '4')" into actual list, its a string
        try:
            data = list(eval(data))
        except Exception:
            "Nothing"

        comboBox = ComboBoxType(data, 1, 5, 4, firstRow)
        for dataType in list(options.keys()):
            comboBox.addItem(dataType)
        comboBox.setCurrentIndex(options[type])

        firstRowWidget = QWidget()
        firstRowWidget.setLayout(firstRow)

        firstRow.addWidget(comboBox)
        verticalLayout.addWidget(firstRowWidget)

        secondRowWidget = self.secondRow(formula)
        verticalLayout.addWidget(secondRowWidget)
        return verticalLayout

    def secondRow(self, formula):
        secondRow = QHBoxLayout()
        label = Label("Formula:")
        secondRow.addWidget(label)

        lineEdit = LineEdit()
        lineEdit.setText(formula)
        secondRow.addWidget(lineEdit)

        secondRowWidget = QWidget()
        secondRowWidget.setLayout(secondRow)

        return secondRowWidget


class FieldsChanges:
    def __init__(self, parent, grandparent):
        self.grandparent = grandparent
        self.parent = parent
        self.layout = self.parent.mainLayout
        fields = self.getChange()
        excel = CreateExcel()
        for name, option, type, formula in fields:
            excel.insertField(self.parent.title, name, option, type, formula)
        self.grandparent.updateAdd()

    def getChange(self):
        items = [self.layout.itemAt(i).widget().children()[0] for i in range(self.layout.count() - 1)]

        fields = list()
        for item in items:
            fields.append(self.getAllChanges(item))

        return fields

    def getCombo(self, widget):
        return str(tuple([widget.itemText(item) for item in range(widget.count() - 1)]))

    def getLineEdit(self, lineEdit):
        return str(lineEdit.text())

    def getCheckButton(self, checkBtn):
        return str(checkBtn.isChecked())

    def getAllChanges(self, items):
        items = [items.itemAt(i).widget().children()[0] for i in range(items.count())]
        tpl = tuple()
        for item in items:
            for index in range(item.count()):
                widget = item.itemAt(index).widget()
                if isinstance(widget, Label) and index <= 1 and item.count() > 2:
                    tpl += (widget.text()[:-1],)
                elif isinstance(widget, QSpinBox):
                    value = widget.value()
                    tpl += (value,)
                elif isinstance(widget, LineEdit):
                    value = widget.text()
                    tpl += (value,)
                elif isinstance(widget, AnswerCombo):
                    value = [widget.itemText(option) for option in range(widget.count() - 1)]
                    tpl += (str(tuple(value)),)
                elif isinstance(widget, QComboBox):
                    value = widget.currentIndex()
                    tpl += (list(options.keys())[value],)
                elif isinstance(widget, QCheckBox):
                    value = widget.isChecked()
                    tpl += (value,)

        return tpl
