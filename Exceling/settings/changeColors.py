import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QIcon, QPixmap, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QColorDialog

from Exceling.globals.colors import ColorsBackend
from Exceling.globals.widgets import Label, LineEdit, DialogBox


class ChangeColors(QWidget):
    def __init__(self, function):
        super().__init__()
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.function = function
        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)
        windowColor = ColorsBackend().window()[0]
        self.setStyleSheet(f"background: {windowColor};")

        self.getColors(function)

    def rows(self, labels, colors):
        for label, color in zip(labels, colors):
            row = QHBoxLayout()
            colorLabel = Label(label)
            colorLabel.setText(label+":")
            row.addWidget(colorLabel)
            lineEdit = LineEditColor(color)
            row.addWidget(lineEdit)
            rowWidget = QWidget()
            rowWidget.setLayout(row)
            self.mainLayout.addWidget(rowWidget)
        self.addDialog()

    def addDialog(self):
        self.buttonBox = DialogBox()
        self.buttonBox.setGeometry(QRect(630, 530, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Save)
        self.mainLayout.addWidget(self.buttonBox)

        self.buttonBox.accepted.connect(lambda: self.getValues())
        self.buttonBox.rejected.connect(lambda: self.close())

    def getColors(self, widget):
        colors = eval("ColorsBackend()." + widget)
        labels = eval("ColorsBackend().insertInto" + widget[:-2].capitalize() + ".__code__.co_varnames")[1:]
        self.rows(labels, colors)

    def getValues(self):
        items = [self.mainLayout.itemAt(i).widget() for i in range(self.mainLayout.count())]
        tpl = ()
        for HLayout in items:
            if isinstance(HLayout, QWidget):
                HLayout = HLayout.layout()
                for count in range(HLayout.count()):
                    widget = HLayout.itemAt(count).widget()
                    if isinstance(widget, QLineEdit):
                        value = widget.text()
                        tpl += (value,)

        eval("ColorsBackend().insertInto" + self.function[:-2].capitalize() + f"(*{tpl})")
        self.close()



class LineEditColor(LineEdit):
    def __init__(self, color):
        super().__init__()
        self.setText(color)

        self.getIcon(color)

    def mouseDoubleClickEvent(self, event):
        color = self.showDialog()
        self.removeAction(self.action)
        self.getIcon(color)
        self.setText(color)

    def showDialog(self):
        color = QColorDialog()
        color = color.getColor().name()
        return color

    def getIcon(self, color):
        pixmap = QPixmap(100, 100)
        pixmap.fill(QColor(color))
        icon = QIcon(pixmap)
        self.action = self.addAction(icon, QLineEdit.TrailingPosition)
        self.action.triggered.connect(lambda: self.mouseDoubleClickEvent(""))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ChangeColors("labels()")
    ex.show()
    sys.exit(app.exec_())
