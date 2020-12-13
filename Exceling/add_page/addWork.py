from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QSpinBox, QLineEdit, QWidget, QComboBox, QScrollArea, QCheckBox, \
    QPushButton

from Exceling.globals.widgets import ComboBox, Frame
from Exceling.globals.comboBoxType import ComboBoxType, AnswerCombo
from Exceling.backend.createExcel import CreateExcel
from Exceling.globals.openFileDialog import FileDialogButton
from Exceling.globals.variables import options
from Exceling.globals.widgets import Label, PushButton, LineEdit


class AddWork(QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setObjectName("mainScrollWidget")
        self.questions = [
            ("Work Title:", "LineEdit()"),
            ("Choose Folder:", "FileDialogButton('directory')"),
            ("Labels Number:", "QSpinBox()"),
            ("Name WorkSheet:", ["ComboBox()", ["Month Name", "Date", "WeekDay", "Increment"]]),
            ("Make First Column:", ["ComboBox()", ["Date", "Number", "Formula", "None"]]),
            ("Work With:", ["ComboBox()", ["Excel", "Word"]]),
        ]
        self.generateButton = PushButton()
        self.generateButton.setText("Generate")
        self.generateButton.pressed.connect(self.generate)

        self.mainLayout = QVBoxLayout()
        self.addQuestions(self.questions)
        self.mainLayout.addWidget(self.generateButton)

        mainWidget = Frame()
        mainWidget.setLayout(self.mainLayout)
        # Scroll Area Properties
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)
        self.setWidget(mainWidget)
        self.setStyleSheet("border: none;")

        self.saveButtonExist = False
        self.saveButton = PushButton()
        self.saveButton.setText("Save")
        self.saveButton.clicked.connect(self.getFields)

    def getStyle(self):
        return ("""
            #mainScrollWidget {
                border: none;
            }
        """)

    def addQuestions(self, questions):
        for labelStr, widgetStr in questions:
            layout = QHBoxLayout()
            layout.setSpacing(0)

            if type(widgetStr) is list:
                widget = eval(widgetStr[0])
                for item in widgetStr[1]:
                    widget.addItem(item)
            else:
                widget = eval(widgetStr)

            label = Label(labelStr)

            layout.addWidget(label)
            layout.addWidget(widget)

            layoutWidget = QWidget()
            layoutWidget.setLayout(layout)

            self.mainLayout.addWidget(layoutWidget)

    def getValues(self):
        items = [self.mainLayout.itemAt(index) for index in range(len(self.questions))]

        answers = list()
        for item in items:
            widget = item.widget()
            horLayoutItems = widget.children()
            if horLayoutItems:
                widget = horLayoutItems[2]
                if isinstance(widget, QSpinBox):
                    value = widget.value()
                elif isinstance(widget, QLineEdit):
                    value = widget.text()
                elif isinstance(widget, QComboBox):
                    value = widget.currentIndex()
                    value = self.questions[items.index(item)][1][1][value]
                elif isinstance(widget, QCheckBox):
                    value = widget.isChecked()
                elif isinstance(widget, QPushButton):
                    value = widget.getText()

                answers.append(value)
        return answers

    def generate(self):
        answers = self.getValues()

        if answers[5] == "Excel":
            if not self.saveButtonExist:
                self.saveButtonExist = True
                self.mainLayout.insertWidget(len(self.questions)+1, self.saveButton)

            for _ in range(answers[2]):
                layout = QHBoxLayout()
                layout.addWidget(Label("Label Name:"))

                lineEdit = LineEdit()
                layout.addWidget(lineEdit)

                layout.addWidget(Label("Field:"))
                lineEdit = LineEdit()
                layout.addWidget(lineEdit)

                types = ["DropDown", "Text", "Check"]
                comboBox = ComboBoxType([], 3, 7, 6, layout)
                for dataType in types:
                    comboBox.addItem(dataType)

                layout.addWidget(Label("Type:"))
                layout.addWidget(comboBox)

                self.secondRow(layout)

        else:
            return "Not Finished Command! Currently Working On!"

    def secondRow(self, layout):
        # making two horizontal layouts in one vertical layout
        # but layouts should be put in a widget first
        firstRowWidget = QWidget()
        firstRowWidget.setLayout(layout)

        secondRow = QHBoxLayout()
        secondRow.addWidget(Label("Formula:"))
        secondRow.addWidget(LineEdit())

        secondRowWidget = QWidget()
        secondRowWidget.setLayout(secondRow)

        VerticalMain = QVBoxLayout()
        VerticalMain.addWidget(firstRowWidget)
        VerticalMain.addWidget(secondRowWidget)

        mainWidget = QWidget()
        mainWidget.setLayout(VerticalMain)

        self.mainLayout.addWidget(mainWidget)

    def getFields(self):
        items = [self.mainLayout.itemAt(item) for item in range(self.mainLayout.count())]
        firstQuestions = len(self.questions) + 2
        items = items[firstQuestions:]
        values = list()
        for widget in items:
            item = widget.widget()
            item = item.children()
            self.getRowValues(item, values)

        excel = CreateExcel()
        excel.addWork(values, self.getValues())
        # the function runs on import, so I did this as solution
        excel.createExcelFile()

    def getRowValues(self, items, values):
        items = [items[0].itemAt(i) for i in range(items[0].count())]
        tpl = tuple()
        for item in items:
            item = item.widget().children()
            item = [item[0].itemAt(i).widget() for i in range(item[0].count())]
            for widget in item:
                if isinstance(widget, QSpinBox):
                    value = widget.value()
                    tpl += (value, )
                elif isinstance(widget, QLineEdit):
                    value = widget.text()
                    tpl += (value, )
                elif isinstance(widget, AnswerCombo):
                    value = [widget.itemText(option) for option in range(widget.count()-1)]
                    tpl += (tuple(value), )
                elif isinstance(widget, QComboBox):
                    value = widget.currentIndex()
                    tpl += (list(options.keys())[value], )
                elif isinstance(widget, QCheckBox):
                    value = widget.isChecked()
                    tpl += (value, )

        values.append(tpl)

