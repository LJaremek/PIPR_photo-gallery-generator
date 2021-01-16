from PyQt5.QtWidgets import QMessageBox

def message(message, title, type_):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(message)
    if type_ == "Critical":
        msg.setIcon(QMessageBox.Critical)
    elif type_ == "Ok":
        msg.setIcon(QMessageBox.Information)
    msg.exec_()
