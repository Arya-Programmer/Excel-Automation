from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit, QComboBox, QVBoxLayout, QScrollArea, QShortcut, \
    QWidgetItem


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

        #Scroll Area Properties
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)
        self.setWidget(mainWidget)

    def column(self, field, data, types):
        layout = QHBoxLayout()
        layout.addWidget(QLabel(field + ":"))

        lineEdit = QLineEdit()
        lineEdit.setText(data)
        layout.addWidget(lineEdit)

        layout.addWidget(QLabel("Type:"))

        comboBox = ComboBox(data, layout)
        for dataType in types:
            comboBox.addItem(dataType)

        layout.addWidget(comboBox)
        return layout

    def getStyle(self):
        return ("""
            #dialogBox *,
            #scrollBar QComboBox,
            #scrollBar QLineEdit,
            #scrollBar QCheckBox{
                background: #e4e6e8;
            }
            #scrollBar QLabel{
                color: white;
            }
            
        """)


class ComboBox(QComboBox):
    def __init__(self, choice, parent=None):
        super().__init__()
        self.parent = parent
        choices = list()
        if choice is list():
            choices = choice
        else:
            choices.append(choice)
        choices.append("add")
        self.choices = choices
        self.currentIndexChanged.connect(self.indexEvent)

    def indexEvent(self, value):
        if value == 0:
            item = self.parent.takeAt(1)
            widget = item.widget()
            widget.deleteLater()
            combo = ChoiceCombo(self.parent)
            for item in self.choices:
                combo.addItem(str(item))
            self.parent.insertWidget(1, combo)

        if value == 1:
            item = self.parent.takeAt(1)
            widget = item.widget()
            widget.deleteLater()
            lineEdit = QLineEdit()
            lineEdit.setText(self.choices[0])
            self.parent.insertWidget(1, lineEdit)


class ChoiceCombo(QComboBox):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setCurrentIndex(0)
        self.num = 0
        self.currentIndexChanged.connect(lambda x: self.indexEvent(x))

    def indexEvent(self, value):
        if self.num > 0:
            if value+1 == self.count() and self.parent.count() < 5:
                lineEdit = AddToChoiceCombo(self)
                self.parent.addWidget(lineEdit)

            elif value+1 != self.count() and self.parent.count() > 4:
                item = self.parent.takeAt(4)
                widget = item.widget()
                widget.deleteLater()

        self.num += 1

class AddToChoiceCombo(QLineEdit):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setToolTip("Press Enter When Finished")
        self.returnPressed.connect(self.onEnter)

    def onEnter(self):
        if self.text().strip() != "":
            countWidget = self.parent.parent.count()
            countOptions = self.parent.count()
            self.parent.removeItem(countOptions-1)
            self.parent.addItem(self.text())
            self.parent.addItem("Add")
            item = self.parent.parent.takeAt(countWidget-1)
            widget = item.widget()
            widget.deleteLater()


class FieldsChanges:
    def __init__(self, main):
        self.main = main
        self.layout = self.main.mainLayout
        print(self.getChange())

    def getChange(self):
        items = [self.layout.itemAt(i) for i in range(self.layout.count())]

        lst = []
        for item in items[:-1]:
            layout = item.widget().children()
            tpl = tuple()
            tpl += (layout[1].text()[:-1], )

            if isinstance(layout[2], QComboBox):
                tpl += (self.getCombo(layout[2]), )
            elif isinstance(layout[2], QLineEdit):
                tpl += (self.getLineEdit(layout[2]), )

            if isinstance(layout[4], QComboBox):
                tpl += (self.getCombo(layout[4]), )
            elif isinstance(layout[4], QLineEdit):
                tpl += (self.getLineEdit(layout[4]), )

            lst.append(tpl)

        return lst

    def getCombo(self, combo):
        return [combo.itemText(item) for item in range(combo.count()-1)]

    def getLineEdit(self, lineEdit):
        return lineEdit.text()

    def getCheckButton(self, checkBtn):
        if checkBtn.isChecked():
            return "False"
        elif checkBtn.isChecked == False:
            return "True"