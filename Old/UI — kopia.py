from QWidgets import PushButton
"""--------------------"""
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QHBoxLayout, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont
from random import randint


class UIGenerateGallery(QWidget):
    def __init__(self, parent = None):
        print("init się nawet nie włącza :F")
        super(UIGenerateGallery, self).__init__(parent)
        print("To też się nie wykona (:")
        self.setGeometry(800, 300, 600, 400)
        self.back_button = QPushButton('Back', self)
        self.back_button.clicked.connect(self.back_to_select_language)


    def back_to_select_language(self):
        print("A")



class UISelectLanguage(QWidget):
    def __init__(self, parent = None):
        super(UISelectLanguage, self).__init__(parent)
        self.setGeometry(800, 300, 600, 400)
        self.widget = QWidget(self)
        
        self.buttons_widget = QWidget(self)
        self.h_box = QHBoxLayout(self.buttons_widget)

##        self.button_PL = PushButton("", self, "PL", self.select_language, "PL_flag.png", size = (200, 125)) # nie działa :C
        self.button_PL = QPushButton("", self)
        self.button_PL.setFixedSize(QSize(200, 125)) 
        #self.button_PL.clicked.connect(lambda state, x = "PL": self.select_language(x))
        self.button_PL.setStyleSheet("background-image : url(PL_flag.png);"
                              "border : 2px solid;"
                              "border-color : black;")
         
        self.button_EN = QPushButton("", self)
        self.button_EN.setFixedSize(QSize(200, 125))
        #self.button_EN.clicked.connect(lambda state, x = "EN": self.select_language(x))
        self.button_EN.setStyleSheet("background-image : url(EN_flag.png);"
                              "border : 2px solid;"
                              "border-color : black;")
        self.h_box.addWidget(self.button_PL)
        self.h_box.addWidget(self.button_EN)

        self.v_box = QVBoxLayout(self.widget)
        self.lb = QLabel(self)
        text = ["Choose a language", "Wybierz język"][randint(0, 1)]
        self.lb.setText(text)
        self.lb.setFont(QFont('Arial', 25)) 
        self.lb.setAlignment(Qt.AlignCenter)
        self.v_box.addWidget(self.lb, 3)
        self.v_box.addWidget(self.buttons_widget, 6)

        self.setLayout(self.v_box)

    def select_language(self, language):
        self.Window2 = UIGenerateGallery(self)
        print(1)
        #self.setCentralWidget(self.Window2)
        print(2)
        self.show()



class Window(QWidget):
    def __init__(self):
        super(self).__init__()
        self.setGeometry(800, 300, 600, 400)
        
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(UISelectLanguage()) # index 0
        self.stackedWidget.addWidget(UIGenerateGallery()) # index 1


    def startSelectLanguage(self):
        self.SelectLanguage = UISelectLanguage(self)
        self.setCentralWidget(self.SelectLanguage)
        self.SelectLanguage.button_EN.clicked.connect(lambda state, x = "EN": self.startGenerateGallery(x))
        self.SelectLanguage.button_PL.clicked.connect(lambda state, x = "PL": self.startGenerateGallery(x))
        self.show()


    def startGenerateGallery(self, language):
        print("start")
        self.startGenerateGallery = UIstartGenerateGallery(self)
        print("koniec? xD no niekoniecznie")
        self.setCentralWidget(self.SelectLanguage)
        self.show()
        
        

        



app = QApplication([])
if __name__ == "__main__":
    win = Window()
    win.show()
