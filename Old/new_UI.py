from QWidgets import PushButton
"""--------------------"""
from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel, QPushButton, QHBoxLayout,
                             QWidget, QVBoxLayout, QWizardPage, QWizard)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont
from random import randint


class UIGenerateGallery(QWizardPage):
    def __init__(self, parent=None):
        super(UIGenerateGallery, self).__init__(parent)
        self.setGeometry(800, 300, 600, 400)
        self.back_button = QPushButton('Back', self)
        self.back_button.clicked.connect(self.back_to_select_language)

    def back_to_select_language():
        pass



class UISelectLanguage(QWizardPage):
    def __init__(self, parent=None):
        super(UISelectLanguage, self).__init__(parent)
        self.setGeometry(800, 300, 600, 400)
        self.widget = QWidget(self)
        
        self.buttons_widget = QWidget(self)
        self.h_box = QHBoxLayout(self.buttons_widget)

##        self.button_PL = PushButton("", self, "PL", self.select_language, "PL_flag.png", size = (200, 125)) # nie działa :C
        self.button_PL = QPushButton("", self)
        self.button_PL.setFixedSize(QSize(200, 125)) 
        self.button_PL.clicked.connect(lambda state, x = "PL": self.select_language(x))
        self.button_PL.setStyleSheet("background-image : url(PL_flag.png);"
                              "border : 2px solid;"
                              "border-color : black;")
         
        self.button_EN = QPushButton("", self)
        self.button_EN.setFixedSize(QSize(200, 125))
        self.button_EN.clicked.connect(lambda state, x = "EN": self.select_language(x))
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
        print(language)



class Wizard(QWizard):
    def __init__(self, parent=None):
        super(Wizard, self).__init__(parent)
        self.setOption(QWizard.NoCancelButton, on = True)
        self.setOption(QWizard.NoBackButtonOnStartPage, on = True)
        self.addPage(UISelectLanguage(self))
        self.addPage(UIGenerateGallery(self))
        self.button(QWizard.NextButton).setDefault(False)
        self.button(QWizard.BackButton).setEnabled(False)
        



app = QApplication([])
if __name__ == "__main__":
##    wizard = QWizard()
##    wizard.addPage(UISelectLanguage())
##    wizard.addPage(UIGenerateGallery())
    wizard = Wizard()
    wizard.show()
