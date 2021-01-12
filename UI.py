from GalerryGenerator import GalerryGenerator
from UIClasses.PyQt5InputDialog import InputDialog
from UIClasses.PyQt5message import message
from errors import *
"""-----------------------------"""
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QVBoxLayout, QGridLayout, QFormLayout, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtWidgets import QDialogButtonBox, QDialog, QAction
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView
from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QSize

from random import choice
import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.scene = QGraphicsScene(self)
        self._config_bar()
        
        self.view = QGraphicsView(self.scene, self)
        self.view.setGeometry(0, 0, 0, 0)
        
        self.setCentralWidget(self.view)


    def _config_bar(self):
        self.bar = self.menuBar()

        self.gallery = self.bar.addMenu("Gallery")
        self.new = QAction("&New", self)
        self.new.setShortcut("Ctrl+N")
        self.new.setStatusTip("Create new gallery")
        self.new.triggered.connect(self.new_gallery)
        self.gallery.addAction(self.new)

        self.save = QAction("&Save", self)
        self.save.setShortcut("Ctrl+S")
        self.save.setStatusTip("Save generated gallery")
        self.save.setEnabled(False)
        self.gallery.addAction(self.save)

        self.clear = QAction("&Clear", self)
        self.clear.setShortcut("Ctrl+C")
        self.clear.setStatusTip("Clear generated gallery")
        self.clear.setEnabled(False)
        self.gallery.addAction(self.clear)

        self.exit = QAction("Exit", self)
        self.exit.setStatusTip("Close program")
        self.exit.triggered.connect(sys.exit)
        self.gallery.addAction(self.exit)


    def new_gallery(self):
        ex = InputDialog()
        ex.exec()
        result = ex.getInputs()
        if result != None:
            print(1)
            self._gen = GalerryGenerator(result[2], result[3])
            print(2)
            self._gen.generate_gallery(topic = result[0], background = result[1])
            print(3)
            photos = self._gen.photos()
            print(photos)
            background = self._gen.background()
            print(background)
            self.set_background(background)
            for photo in photos:
                window.set_numpy_image_on_scene(photo.image(), photo.x(), photo.y())
            self.save.setEnabled(True)
            self.clear.setEnabled(True)


    def set_qpixmap_on_scene(self, qpixmap, x, y):
        item = QGraphicsPixmapItem(qpixmap)
        item.setPos(x, y)
        self.scene.addItem(item)


    def resize_item_to(self, item, width=False, height=False):
        if width:
            return item.scaledToWidth(width)
        elif height:
            return item.scaledToHeight(height)
    

    def set_background(self, background):
        width, height = background.width(), background.height()
        bytesPerLine = width*3
        format_ = QImage.Format_RGB888
        
        background = QPixmap(QImage(background.image(), width, height, bytesPerLine, format_))
        self.set_qpixmap_on_scene(background, 0, 0)        
        

    def set_numpy_image_on_scene(self, numpy_image, x, y):
        q_image = QImage(numpy_image.data, numpy_image.shape[1], numpy_image.shape[0],
                         numpy_image.shape[1]*numpy_image.shape[2], QImage.Format_RGB888)
        
        item = QPixmap(q_image)
        #item = self.resize_item_to(item, width = 200)
        self.set_qpixmap_on_scene(item, x, y)


app = QApplication([])

window = MainWindow()
window.show()

app.exec_()
