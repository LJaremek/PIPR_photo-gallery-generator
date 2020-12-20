from QWidgets import PushButton
"""--------------------"""
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QHBoxLayout, QWidget, QVBoxLayout, QLineEdit, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont
from random import randint


class UIGenerateGallery(QWidget):
    def __init__(self, parent = None, language = "EN"):
        super(UIGenerateGallery, self).__init__(parent)
        self.language = language
        verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)
        HorizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)


        self.topic_widget = QWidget(self)
        self.box_topic = QVBoxLayout()#self.topic_widget)

        self.label_topic = QLabel(self)

        text = "Temat kolażu" if self.language == "PL" else "Collage topic"
        self.label_topic.setText(text)
        self.label_topic.setFont(QFont('Arial', 25))
        self.label_topic.setAlignment(Qt.AlignCenter)

        

        
        self.lineedit_topic = QLineEdit()
        self.lineedit_topic.setFixedWidth(240)
        self.lineedit_topic.setFont(QFont("Arial",15))
        self.lineedit_topic.frameGeometry().center() # ? nic nie robi ###########################

        text = "Generuj!" if self.language == "PL" else "Generate!"
        self.button_generate = QPushButton(text)
        self.button_generate.setFixedSize(QSize(120, 40))
        self.button_generate.setFont(QFont('Arial', 15))
        #self.button_generate.frameGeometry().center() ###########################
        
        #text = self.lineedit_topic.text()
        self.box_topic.addWidget(self.label_topic)
        self.box_topic.addWidget(self.lineedit_topic)
        self.box_topic.addWidget(self.button_generate)
        self.topic_widget.setLayout(self.box_topic)



        self.widget_buttons = QWidget(self)
        self.h_box = QHBoxLayout()#self.widget_buttons)
        
        self.back_button = QPushButton('Back', self)
        self.h_box.addWidget(self.back_button)
        self.h_box.addItem(HorizontalSpacer)
        self.widget_buttons.setLayout(self.h_box)


        self.widget_main = QWidget(self)
        self.main = QVBoxLayout(self.widget_main)
        
        self.main.addSpacerItem(verticalSpacer)
        self.main.addWidget(self.topic_widget)
        self.main.addSpacerItem(verticalSpacer)
        self.main.addWidget(self.widget_buttons)
        
        self.setLayout(self.main)





class UISelectLanguage(QWidget):
    def __init__(self, parent = None):
        super(UISelectLanguage, self).__init__(parent)
        self.widget = QWidget(self)
        
        self.buttons_widget = QWidget(self)
        self.h_box = QHBoxLayout(self.buttons_widget)

##        self.button_PL = PushButton("", self, "PL", self.select_language, "PL_flag.png", size = (200, 125)) # nie działa :C
        self.button_PL = QPushButton("", self)
        self.button_PL.setFixedSize(QSize(200, 125)) 
        self.button_PL.setStyleSheet("background-image : url(PL_flag.png);"
                              "border : 2px solid;"
                              "border-color : black;")
         
        self.button_EN = QPushButton("", self)
        self.button_EN.setFixedSize(QSize(200, 125))
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



class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(800, 300, 600, 400)
        self.startSelectLanguage()


    def startSelectLanguage(self):
        self.SelectLanguage = UISelectLanguage(self) # przypisuję okno do zmiennej
        self.setCentralWidget(self.SelectLanguage) # ustawiam zmienną za główne okno
        self.SelectLanguage.button_EN.clicked.connect(lambda state, x = "EN": self.startGenerateGallery(x))
        self.SelectLanguage.button_PL.clicked.connect(lambda state, x = "PL": self.startGenerateGallery(x))
        self.show()


    def startGenerateGallery(self, language):
        self.GenerateGallery = UIGenerateGallery(self, language) # przypisuję okno do zmiennej
        self.setCentralWidget(self.GenerateGallery) # ustawiam zmienną za główne okno
        self.GenerateGallery.back_button.clicked.connect(self.startSelectLanguage)
        self.show()
        
        

        



app = QApplication([])
if __name__ == "__main__":
    win = Window()
    win.show()
