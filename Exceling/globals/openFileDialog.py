from PyQt5.QtWidgets import QFileDialog
from pathlib import Path

from Exceling.globals.widgets import PushButton


class OpenFileDialog(QFileDialog):
    def __init__(self):
        super().__init__()
        self.fileName = ''

    def getFileName(self):
        homeDir = str(Path.home())
        fileName, fileType = self.getOpenFileName(self, "Choose Excel File", homeDir, "Excel Files (*.xla *.xlam *.xls *.xlsb *.xlsx *.xlt *.xltm)")
        self.fileName = fileName

    def getFolderName(self):
        homeDir = str(Path.home())
        fileName = self.getExistingDirectory(self, "Select Directory To Make Excel File", homeDir)
        self.fileName = fileName


class FileDialogButton(PushButton):
        def __init__(self, dialogType):
            super().__init__()
            self.setText("Choose")
            self.dialogType = dialogType

        def mousePressEvent(self, event):
            super().mousePressEvent(event)
            self.dialog = OpenFileDialog()
            if self.dialogType == "directory":
                self.dialog.getFolderName()
            elif self.dialogType == "file":
                self.dialog.getFileName()

        def getText(self):
            return self.dialog.fileName



