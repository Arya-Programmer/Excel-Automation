from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QTabWidget

from Exceling.globals.colors import ColorsBackend
from Exceling.globals.messageBox import MessageBox
from Exceling.globals.widgets import Label, LineEdit, ComboBox, TabWidget, Frame, PushButton, DialogBox
from Exceling.settings.CardColor import CardColor
from Exceling.settings.changeColors import ChangeColors
from Exceling.settings.leftButtons import LeftButtons


class WindowColor(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.change = ChangeColors("window()")

    def mouseDoubleClickEvent(self, e):
        if not self.change.isVisible():
            self.change.show()


class ColorChanger(WindowColor):
    def __init__(self):
        super().__init__()
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        bg = ColorsBackend().window()[0]
        Form.setStyleSheet(f"background: {bg};")

        horizontal = QHBoxLayout()

        buttonsLayout = QVBoxLayout()
        buttonsLayout.setSpacing(0)
        buttonsLayout.setContentsMargins(0, 0, 0, 0)

        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(100, 0, 301, 301))
        self.tabWidget.setStyleSheet("""::tab{
                                            border: none; width: 0; height: 0;
                                        }
                                        ::pane{
                                            border: none;
                                        }""")

        self.tab = Frame()

        self.card = CardColor(self.tab, self)
        self.card.setGeometry(QtCore.QRect(10, 10, 71, 101))
        self.card1 = CardColor(self.tab, "dont work")
        self.card1.setGeometry(QtCore.QRect(130, 10, 71, 101))

        self.tabWidget.addTab(self.tab, "")
        subTab = FrameColor(self, self)

        self.tab_2 = TabWidgetColor(None, 30, 90, self)
        self.tab_2.addTab(subTab, "Title")
        self.tab_2.addTab(FrameColor(self, self), "Title")

        self.label = LabelColor("Line Edit", subTab, self)
        self.label.setGeometry(QtCore.QRect(10, 50, self.label.width(), self.label.height()))

        self.lineEdit = LineEditColor(subTab, self)
        self.lineEdit.setGeometry(QtCore.QRect(90, 55, self.lineEdit.width(), 20))

        self.label2 = LabelColor("Combo Box", subTab, self)
        self.label2.setGeometry(QtCore.QRect(10, 90, self.label2.width(), self.label2.height()))

        self.comboBox = ComboBoxColor(subTab, self)
        self.comboBox.addItem("1")
        self.comboBox.addItem("2")
        self.comboBox.addItem("3")
        self.comboBox.setGeometry(QtCore.QRect(90, 95, self.comboBox.width(), 20))

        self.button = PushButtonColor(subTab, self)
        self.button.setText("Button")
        self.button.setGeometry(QtCore.QRect(10, 120, self.button.width(), self.button.height()))

        self.buttonBox = DialogBoxColor(subTab, self)
        self.buttonBox.setGeometry(QtCore.QRect(5, 160, 160, 30))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Save)

        self.tabWidget.addTab(self.tab_2, "")

        sideButtons = LeftButtons(self)
        horizontal.addWidget(sideButtons)
        horizontal.addWidget(self.tabWidget)
        horizontal.setSpacing(0)
        horizontal.setContentsMargins(0, 0, 0, 0)

        self.setLayout(horizontal)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Tab 1"))
        self.label.setText(_translate("Form", "Line Edit:"))
        self.label2.setText(_translate("Form", "Combo Box:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Tab 2"))

    def secondTab(self):
        self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.tab_2))

    def firstTab(self):
        self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.tab))

    def closeEvent(self, e):
        super().closeEvent(e)
        msg = MessageBox("information", "You Need To Restart The App To See The Affects!", "Reboot App")
        msg.exec_()


class ComboBoxColor(ComboBox):
    def __init__(self, parent, main):
        super().__init__(parent)
        self.change = ChangeColors("inputfields()", main)

    def mouseDoubleClickEvent(self, e):
        if not self.change.isVisible():
            self.change.show()


class LineEditColor(LineEdit):
    def __init__(self, parent, main):
        super().__init__(parent)
        self.change = ChangeColors("inputfields()", main)

    def mouseDoubleClickEvent(self, e):
        if not self.change.isVisible():
            self.change.show()


class LabelColor(Label):
    def __init__(self, text, parent, main):
        super().__init__(text, parent)
        self.change = ChangeColors("labels()", main)

    def mouseDoubleClickEvent(self, e):
        if not self.change.isVisible():
            self.change.show()


class PushButtonColor(PushButton):
    def __init__(self, parent, main):
        super().__init__(parent)
        self.change = ChangeColors("buttons()", main)

    def mouseDoubleClickEvent(self, e):
        if not self.change.isVisible():
            self.change.show()


class TabWidgetColor(TabWidget):
    def __init__(self, parent, width, height, main):
        super().__init__(parent, width, height)
        self.change = ChangeColors("tabs()", main)

    def mouseDoubleClickEvent(self, e):
        if not self.change.isVisible():
            self.change.show()


class DialogBoxColor(DialogBox):
    def __init__(self, parent, main):
        super().__init__(parent)
        self.change = ChangeColors("dialogboxes()", main)
        self.clicked.connect(lambda: self.mouseDoubleClickEvent(""))

    def mouseDoubleClickEvent(self, e):
        if not self.change.isVisible():
            self.change.show()


class FrameColor(Frame):
    def __init__(self, parent, main):
        super().__init__(parent)
        self.change = ChangeColors("tabs()", main)

    def mouseDoubleClickEvent(self, e):
        if not self.change.isVisible():
            self.change.show()
