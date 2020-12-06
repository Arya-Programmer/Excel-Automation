from PyQt5.QtWidgets import QComboBox, QLineEdit
from Exceling.globals.variables import options


class ComboBoxType(QComboBox):
    def __init__(self, choice, itemToChange, mostWidgetNum, leastWidgetNum, parent=None):
        super().__init__()
        self.parent = parent
        self.itemToChange = itemToChange
        self.mostWidgetNum = mostWidgetNum
        self.leastWidgetNum = leastWidgetNum
        choices = list()
        if type(choice) is list:
            choices = choice
        else:
            choices.append(choice)
        choices.append("add")
        self.choices = choices
        self.currentIndexChanged.connect(self.indexEvent)

    def indexEvent(self, value):
        if value == options["DropDown"]:
            item = self.parent.takeAt(self.itemToChange)
            widget = item.widget()
            widget.deleteLater()
            combo = AnswerCombo(self.currentIndex(), self.itemToChange, self.mostWidgetNum, self.leastWidgetNum, self, self.parent)
            for item in self.choices:
                combo.addItem(str(item))
            self.parent.insertWidget(self.itemToChange, combo)

        if value == options["Text"]:
            item = self.parent.takeAt(self.itemToChange)
            widget = item.widget()
            widget.deleteLater()
            lineEdit = QLineEdit()
            lineEdit.setText(self.choices[0])
            self.parent.insertWidget(self.itemToChange, lineEdit)


class AnswerCombo(QComboBox):
    def __init__(self, currentIndex, itemToChange, mostWidgetNum, leastWidgetNum, comboBox, parent):
        super().__init__()
        self.typeCombo = comboBox
        self.itemToChange = itemToChange
        self.mostWidgetNum = mostWidgetNum
        self.leastWidgetNum = leastWidgetNum
        self.parent = parent
        self.setCurrentIndex(currentIndex)
        self.num = 0
        self.currentIndexChanged.connect(lambda x: self.indexEvent(x))

    def indexEvent(self, value):
        if self.num > 0:
            if value+1 == self.count() and self.parent.count() <= self.leastWidgetNum:
                self.typeCombo.setEnabled(False)
                lineEdit = AddToChoiceCombo(self, self.typeCombo)
                self.parent.addWidget(lineEdit)

            elif value+1 != self.count() and self.parent.count() >= self.mostWidgetNum:
                item = self.parent.takeAt(self.mostWidgetNum - 1)
                widget = item.widget()
                widget.deleteLater()
                self.typeCombo.setEnabled(True)

        self.num += 1

    # this is added because when fields first created there is only one choice, that is: add
    # when there is one choice currentIndexChanged cant be triggered so this is alternative
    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        if self.num > 0:
            value = self.currentIndex()
            if value+1 == self.count() and self.parent.count() <= self.leastWidgetNum:
                self.typeCombo.setEnabled(False)
                lineEdit = AddToChoiceCombo(self, self.typeCombo)
                self.parent.addWidget(lineEdit)

            elif value+1 != self.count() and self.parent.count() >= self.mostWidgetNum:
                item = self.parent.takeAt(self.mostWidgetNum)
                widget = item.widget()
                widget.deleteLater()

        self.num += 1


class AddToChoiceCombo(QLineEdit):
    def __init__(self, parent, typeCombo):
        super().__init__()
        self.parent = parent
        self.typeCombo = typeCombo
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
            self.typeCombo.setEnabled(True)

