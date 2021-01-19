from .check_topic import check_topic
from .PyQt5message import message
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QDialogButtonBox, QDialog
from random import choice


class InputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.topics = []

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        layout = QGridLayout(self)
        
        layout.addWidget(QLabel("Topic: "), 0, 0)
        self.topic = QLineEdit(self)
        self.topic.setPlaceholderText("topic")
        layout.addWidget(self.topic, 0, 1)
        self.random_topic = QPushButton("random")
        self.random_topic.clicked.connect(self.random_word)
        layout.addWidget(self.random_topic, 0, 2)
        
        layout.addWidget(QLabel("Background: "), 1, 0)
        self.background = QLineEdit(self)
        self.background.setPlaceholderText("background")
        layout.addWidget(self.background, 1, 1)
        
        layout.addWidget(QLabel("Width: "), 2, 0)
        self.width = QLineEdit(self)
        self.width.setPlaceholderText("width")
        self.width.setText("1000")
        layout.addWidget(self.width, 2, 1)
        
        layout.addWidget(QLabel("Height: "), 3, 0)
        self.height = QLineEdit(self)
        self.height.setPlaceholderText("height")
        self.height.setText("1000")
        layout.addWidget(self.height, 3, 1)
        
        layout.addWidget(buttonBox, 4, 0)
        buttonBox.accepted.connect(self.accept)
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


    def random_word(self):
        if self.topics == []:
            try:
                file = open("topics_base.txt")
            except FileNotFoundError:
                message("There is no topics_base.txt in the main folder!\nTry use Generators.py",
                        "No topics_base.txt", "Critical")
                return None
            for topic in file:
                self.topics.append(topic.strip())
            file.close()
        self.topic.setText(choice(self.topics))
        
