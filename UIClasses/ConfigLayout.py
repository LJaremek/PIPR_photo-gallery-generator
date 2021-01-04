from PyQt5.QtWidgets import (QApplication, QMainWindow, # Main App
                             QVBoxLayout, QHBoxLayout, QGridLayout, # Layouts
                             QLabel, QLineEdit, QPushButton, # Widgets
                             QSpacerItem, QSizePolicy,
                             QWidget) # Widget
from PyQt5.QtGui import QPainter, QPixmap, QImage, QIcon, QScreen # Canvas items
from urllib.request import urlopen
from PyQt5.QtCore import QSize
from random import choice
import tkinter
import cv2



class ConfigLayout:
    def __init__(self):
        self._verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.widget = QWidget()
        self._gbox_options = QGridLayout()

        # jeden widget
        self._label_topic = QLabel("Topic:*")
        self._gbox_options.addWidget(self._label_topic, 0, 0) # katalog UI -> config, ... SOLID
        self._lineedit_topic = QLineEdit()
        self._lineedit_topic.setText("water")
        self._gbox_options.addWidget(self._lineedit_topic, 0, 1)
        self._button_random_topic = QPushButton(QIcon(QPixmap("dice.png")), "")
        self._button_random_topic.setIconSize(QSize(25, 25))
        self._button_random_topic.setFixedSize(QSize(25, 25))
        self._button_random_topic.setToolTip("Random topic")
        self._gbox_options.addWidget(self._button_random_topic, 0, 2) # okno dialogowe z
        #

        self._label_background = QLabel("Background:") # funkcja numer wiersza, nazwa etykiety, tekst
        self._gbox_options.addWidget(self._label_background, 1, 0)
        self._lineedit_background = QLineEdit() # funkcja do tego
        self._lineedit_background.setText("sky")
        self._gbox_options.addWidget(self._lineedit_background, 1, 1)
        self._button_random_background = QPushButton()
        self._gbox_options.addWidget(self._button_random_background, 1, 2)

        label_width = QLabel("Width:*") # funkcje # qformlayout addrow
        self._gbox_options.addWidget(label_width, 2, 0)
        self._lineedit_width = QLineEdit()
        self._lineedit_width.setText("1000")
        self._gbox_options.addWidget(self._lineedit_width, 2, 1)

        self._label_height = QLabel("Height:*")
        self._gbox_options.addWidget(self._label_height, 3, 0)
        self._lineedit_height = QLineEdit()
        self._lineedit_height.setText("1000")
        self._gbox_options.addWidget(self._lineedit_height, 3, 1)

        self._button_generate = QPushButton("Generate")
        self._gbox_options.addWidget(self._button_generate, 4, 0)
        self._gbox_options.addItem(self._verticalSpacer, 5, 0)
        
        
        self.widget.setLayout(self._gbox_options)


    def set_button_function(self, button, function):
        if button == "random topic":
            self._button_random_topic.clicked.connect(function)
        elif button == "generate":
            self._button_generate.clicked.connect(function)


    def topic(self):
        return self._lineedit_topic.text()


    def background(self):
        return self._lineedit_background.text()


    def width(self):
        return int(self._lineedit_width.text())


    def height(self):
        return int(self._lineedit_height.text())
