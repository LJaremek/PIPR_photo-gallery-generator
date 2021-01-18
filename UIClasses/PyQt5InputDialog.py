from .check_topic import check_topic
from .PyQt5message import message
"""-----------------------------"""
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtWidgets import QDialogButtonBox, QDialog


class InputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        layout = QGridLayout(self)
        
        layout.addWidget(QLabel("Topic: "), 0, 0)
        self.topic = QLineEdit(self)
        layout.addWidget(self.topic, 0, 1)
        
        layout.addWidget(QLabel("Background: "), 1, 0)
        self.background = QLineEdit(self)
        layout.addWidget(self.background, 1, 1)
        
        layout.addWidget(QLabel("Width: "), 2, 0)
        self.width = QLineEdit(self)
        layout.addWidget(self.width, 2, 1)
        
        layout.addWidget(QLabel("Height: "), 3, 0)
        self.height = QLineEdit(self)
        layout.addWidget(self.height, 3, 1)
        
        layout.addWidget(buttonBox)
        buttonBox.accepted.connect(self.accept)
        self.accepted.connect(self.getInputs)
        buttonBox.rejected.connect(self.reject)


    def getInputs(self):
        """
        Getting the inputs from user
        """
        topic = self.topic.text().strip()
        if topic == "":
            message("The topic can't be empty.", "Invalid topic", "Critical")
            return None
        background = self.background.text().strip()

        try:
            width = int(self.width.text())
            if width < 500:
                message("Width have to be bigger than 500.", "Invalid width", "Critical")
                return None
        except TypeError:
            message("Width have to be integer bigger than 500.", "Invalid width", "Critical")
            return None
        
        try:
            height = int(self.height.text())
            if width < 500:
                message("Height have to be bigger than 500.", "Invalid height", "Critical")
                return None
        except TypeError:
            message("Geight have to be integer bigger than 500.", "Invalid height", "Critical")
            return None
        
        try:
            result, count = check_topic(topic)
        except:
            message("There are a problem with connection to unsplash.com.\nCheck your internet connection", "No connection", "Critical")
            return None
        
        if count < 15:
            message("The topic is not very popular. Choose another one.", "Invalid topic", "Critical")
            return None
        if background == "":
            return topic, "Black", width, height
        return topic, background, width, height
