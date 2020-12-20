from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont

def PushButton(text = "", _self = None, arg = None, function = None, image = None, size = None, border = 2, border_color = "black"):
    button = QPushButton(text, _self)

    if size != None:
        button.setFixedSize(QSize(size[0], size[1]))
        
    if arg != None:
        button.clicked.connect(lambda state, x = arg: function(x))
    else:
        button.clicked.connect(function)

    if image != None:
        button.setStyleSheet(f"background-image : url({image});"
                             f"border : {border}px solid;"
                             f"border-color : {border_color};")
    else:
        button.setStyleSheet(f"border : {border}px solid;"
                             f"border-color : {border_color};") 
