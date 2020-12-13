from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QComboBox, QCheckBox, QScrollArea, \
    QSpinBox, QApplication

from Exceling.backend.createExcel import CreateExcel
from Exceling.globals.variables import optionsWidgets
from Exceling.globals.widgets import Label, PushButton, DialogBox, LineEdit, ComboBox


class Add(QScrollArea):
    def __init__(self, title, limit, oid, main, parent):
        super().__init__()
        self.main = main
        self.parent = parent
        self.limit = limit
        self.title = title
        self.oid = oid

        self.mainLayout = QVBoxLayout()

        fields = self.getFieldsInput()
        for field, data, widget in fields:
            self.mainLayout.addWidget(self.getFields(field, data, widget))

        self.buttonBox = DialogBox()
        self.buttonBox.setGeometry(QtCore.QRect(630, 530, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Save)

        self.mainLayout.addWidget(self.buttonBox)

        self.buttonBox.accepted.connect(lambda: self.fieldValues())
        self.buttonBox.rejected.connect(lambda: self.main.recentClick())

        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.mainLayout)

        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)
        self.setWidget(self.mainWidget)
        self.setStyleSheet("border: none;")

    def getFields(self, field, data, widget):
        layout = QHBoxLayout()
        label = Label(field + ":")
        layout.addWidget(label)

        if isinstance(widget, QLineEdit):
            widget = LineEdit()
            widget.setText(data)
        elif isinstance(widget, QComboBox):
            widget = ComboBox()
            for item in eval(data):
                widget.addItem(item)
        elif isinstance(widget, QCheckBox):
            widget = QCheckBox()
        layout.addWidget(widget)

        mainWidget = QWidget()
        mainWidget.setLayout(layout)

        return mainWidget

    def getFieldsInput(self):
        excel = CreateExcel()
        data = excel.getTheLast(self.limit, "FIELDS", self.title)

        fields = list()
        for oid, title, labelName, labelType, labelData, formula in data:
            tpl = (labelName, labelData)
            widget = optionsWidgets[labelType]
            tpl += (eval(widget),)
            fields.append(tpl)

        return fields

    def fieldValues(self):
        items = [self.mainLayout.itemAt(item) for item in range(self.mainLayout.count())]
        # go through mainLayout widgets and get their first children(QHBoxLayout)
        # inside there get second index which is the widget
        items = [items[i].widget().children()[0] for i in range(len(items) - 1)]
        values = list()
        for item in items:
            value = tuple()
            widget = item.itemAt(1).widget()
            if isinstance(widget, QSpinBox):
                value += (widget.value(),)

            elif isinstance(widget, QLineEdit):
                value += (widget.text(),)

            elif isinstance(widget, QComboBox):
                value += (widget.itemText(widget.currentIndex()),)

            elif isinstance(widget, QCheckBox):
                value += (widget.isChecked(),)

            label = item.itemAt(0).widget()
            value += (label.text()[:-1],)

            values.append(value)

        excel = CreateExcel()
        excel.addToExcel(values, self.oid)
        self.parent.updatePreview()
        self.parent.updateLastInput()
