import sys

from matplotlib.colors import is_color_like
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QIcon, QPixmap, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QColorDialog

from Exceling.globals.colors import ColorsBackend
from Exceling.globals.widgets import Label, LineEdit, DialogBox


class ChangeColors(QWidget):
    def __init__(self, function, parent=None):
        super().__init__()
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.function = function
        self.parent = parent

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
        if self.parent is not None:
            self.parent.setupUi(self.parent)
            self.parent.repaint()
            self.parent.update()
        self.close()



class LineEditColor(LineEdit):
    def __init__(self, color):
        super().__init__()
        self.setText(color)
        self.dialog = QColorDialog()
        self.dialog.setWindowModality(QtCore.Qt.ApplicationModal)

        self.textChanged.connect(lambda: self.textAltered())
        self.getIcon(color)

    def mouseDoubleClickEvent(self, event):
        self.showDialog()

    def changeColor(self, color):
        self.removeAction(self.action)
        self.getIcon(color)
        self.setText(color)

    def textAltered(self):
        newColor = self.text()
        if is_color_like(newColor):
            self.removeAction(self.action)
            self.getIcon(newColor)

    def showDialog(self):
        self.dialog.setCurrentColor(QColor(self.text()))
        self.dialog.show()
        self.dialog.accepted.connect(lambda: self.changeColor(self.dialog.selectedColor().name()))
        self.dialog.rejected.connect(lambda: self.dialog.close())

    def getIcon(self, color):
        pixmap = QPixmap(100, 100)
        pixmap.fill(QColor(color))
        icon = QIcon(pixmap)
        self.action = self.addAction(icon, QLineEdit.TrailingPosition)
        self.action.triggered.connect(lambda: self.mouseDoubleClickEvent(''))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ChangeColors("labels()")
    ex.show()
    sys.exit(app.exec_())
