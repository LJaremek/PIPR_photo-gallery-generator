from PyQt5.QtWidgets import QMessageBox

def message(message, title, type_):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(message)
    if type_ == "Critical":
        msg.setIcon(QMessageBox.Critical)
    msg.exec_()
