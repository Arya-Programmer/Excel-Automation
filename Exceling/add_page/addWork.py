from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QSpinBox, QLineEdit, QLabel, QWidget, QComboBox, \
    QPushButton, QScrollArea, QCheckBox

from Exceling.globals.comboBoxType import ComboBoxType, AnswerCombo

from Exceling.globals.variables import options


class AddWork(QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setObjectName("mainScrollWidget")
        self.questions = [
            ("Labels Number:", "QSpinBox()"),
            ("Make First Column:", ["QComboBox()", ["Date", "Number", "Formula"]]),
            ("Work With:", ["QComboBox()", ["Excel", "Word"]]),
        ]
        self.generateButton = QPushButton()
        self.generateButton.setText("Generate")
        self.generateButton.pressed.connect(self.generate)

        self.mainLayout = QVBoxLayout()
        self.addQuestions(self.questions)
        self.mainLayout.addWidget(self.generateButton)

        mainWidget = QWidget()
        mainWidget.setLayout(self.mainLayout)

        mainWidget.setStyleSheet(self.getStyle())
        mainWidget.setObjectName("addWork")
        self.setStyleSheet(self.getStyle())
        # Scroll Area Properties
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)
        self.setWidget(mainWidget)

        self.saveButtonExist = False
        self.saveButton = QPushButton()
        self.saveButton.setText("Save")
        self.saveButton.setGeometry(QtCore.QRect(630, 530, 156, 23))
        self.saveButton.clicked.connect(self.parent.addWork)

    def getStyle(self):
        return ("""
            QComboBox *,
            QComboBox,
            QLineEdit,
            QSpinBox,
            QCheckBox,
            QPushButton{
                background: white;
            }
            #addWork > QPushButton {
                background: white;
            }
            QLabel{
                color: white;
                background: #141518;
            }
            #addWork > *, #addWork, #addWork > * > *{
                background: #141518;
            }
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

            label = QLabel(labelStr)

            layout.addWidget(label)
            layout.addWidget(widget)

            layoutWidget = QWidget()
            layoutWidget.setLayout(layout)

            self.mainLayout.addWidget(layoutWidget)

    def getValues(self):
        items = [self.mainLayout.itemAt(index) for index in range(self.mainLayout.count() - 1)]

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
                elif isinstance(widget, QCheckBox):
                    value = widget.isChecked()

                answers.append(value)
        return answers

    def generate(self):
        answers = self.getValues()
        if answers[1] == 0:
            if not self.saveButtonExist:
                self.saveButtonExist = True
                self.mainLayout.insertWidget(len(self.questions)+1, self.saveButton)

            for _ in range(answers[0]):
                layout = QHBoxLayout()
                layout.addWidget(QLabel("Label Name:"))

                lineEdit = QLineEdit()
                layout.addWidget(lineEdit)

                layout.addWidget(QLabel("Field:"))
                lineEdit = QLineEdit()
                layout.addWidget(lineEdit)

                types = ["DropDown", "Text", "Check"]
                comboBox = ComboBoxType([], 3, 7, 6, layout)
                for dataType in types:
                    comboBox.addItem(dataType)

                layout.addWidget(QLabel("Type:"))
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
        secondRow.addWidget(QLabel("Formula:"))
        secondRow.addWidget(QLineEdit())

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

        return values

    def getRowValues(self, items, values):
        items = [items[0].itemAt(i) for i in range(items[0].count())]
        tpl = tuple()
        for item in items:
            item = item.widget().children()
            for widget in item[2::2]:
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

