from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QHBoxLayout, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont
from random import randint
##app = QApplication([])
##window = QWidget()
##window.resize(500, 400)
##
##label = QLabel("Choose a language")
##main_layout = QVBoxLayout()
##main_layout.addWidget(label)
##
##layout_with_buttons = QHBoxLayout()
##button_polish_language = QPushButton("PL")
##button_english_language = QPushButton("EN")
##layout_with_buttons.addWidget(button_polish_language)
##layout_with_buttons.addWidget(button_english_language)
##
##main_layout.addWidget(layout_with_buttons)
##
##window.setLayout(main_layout)
##window.show()
##label.show()
##app.exec_()

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(800, 300, 600, 400)
        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)
        self.initUI()
        

    def initUI(self):
        self.buttons_widget = QWidget(self)
        self.h_box = QHBoxLayout(self.buttons_widget)

        self.b1 = QPushButton("", self)
        self.b1.clicked.connect(lambda state, x = "PL": self.select_language(x))
        self.b1.setStyleSheet("background-image : url(PL_flag.png);"
                              "border : 2px solid;"
                              "border-color : black;")
        self.b1.setFixedSize(QSize(200, 125)) 
        self.b2 = QPushButton("", self)
        self.b2.clicked.connect(lambda state, x = "EN": self.select_language(x))
        self.b2.setStyleSheet("background-image : url(EN_flag.png);"
                              "border : 2px solid;"
                              "border-color : black;")
        self.b2.setFixedSize(QSize(200, 125)) 

        self.h_box.addWidget(self.b1)
        self.h_box.addWidget(self.b2)

        self.v_box = QVBoxLayout(self.widget)
        self.lb = QLabel(self)
        text = ["Choose a language", "Wybierz język"][randint(0, 1)]
        self.lb.setText(text)
        self.lb.setFont(QFont('Arial', 25)) 
        self.lb.setAlignment(Qt.AlignCenter)
        self.v_box.addWidget(self.lb, 3)
        self.v_box.addWidget(self.buttons_widget, 6)

        self.setLayout(self.v_box)
        

    def select_language(self, language=""):
        print(language)


app = QApplication([])
if __name__ == "__main__":
    win = Window()
    win.show()
