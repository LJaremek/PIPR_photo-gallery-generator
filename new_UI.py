from GalerryGenerator import GalerryGenerator
from UIClasses.ConfigLayout import ConfigLayout
"""-----------------------------"""
from PyQt5.QtWidgets import (QApplication, QMainWindow, # Main App
                             QVBoxLayout, QHBoxLayout, QGridLayout, # Layouts
                             QLabel, QLineEdit, QPushButton, # Widgets
                             QSpacerItem, QSizePolicy,
                             QWidget) # Widget
from PyQt5.QtGui import QPainter, QPixmap, QImage, QIcon, QScreen # Canvas items
from urllib.request import urlopen
from PyQt5.QtCore import QSize
from random import choice
import cv2


class Window(QMainWindow):
    def __init__(self, screen_width, screen_height):
        super(Window, self).__init__()
        self.showMaximized() # animacja, pasek menu (help, save, format pliku)
                             # generate większy, reset
        self.screen_width = screen_width
        self.screen_height = screen_height
        self._create_options_layout()
        self._set_up_sizes() # protondb
        self._create_canvas_layout()
        self._create_main_layout()
        self.create_empty_canvas()

        self.setCentralWidget(self._widget_main)


    def _set_up_sizes(self): # qtgui qtscreen do wymiarów ekranu, generuj losowo, różne pakiety rozmiarów
        """
        Setting up canvas sizes.
        """
        ratio = self.get_width() / self.get_height()
        self.canvas_height = int(self.screen_height*(8/9))
        self.canvas_width = int(self.canvas_height*ratio)


    def _create_options_layout(self):
        """
        Creating left panel - panel with config options.
        """
        self._options = ConfigLayout()
        self._options.set_button_function("random topic", self._random_topic)
        self._options.set_button_function("generate", self.generate_gallery)


    def _create_canvas_layout(self):
        """
        Creating right panel - panel with canvas with photos.
        """
        self._widget_canvas = QLabel()
        self._canvas = QPixmap(self.canvas_width, self.canvas_height)
        self._widget_canvas.setPixmap(self._canvas)

# click, pysimplegui
    def _create_main_layout(self):
        """
        Creating main layout with left and right panels.
        """
        self._widget_main = QWidget()
        self._layout_main = QHBoxLayout()
        self._layout_main.addWidget(self._options.widget, 1)
        self._layout_main.addWidget(self._widget_canvas, 4)
        self._widget_main.setLayout(self._layout_main)


    def create_empty_canvas(self):
        """
        Creating empty canvas.
        """
        self._canvas = QPixmap(self.canvas_width, self.canvas_height)
        self._widget_canvas.setPixmap(self._canvas)


    def _random_topic(self):
        gen = GalerryGenerator()
        result = False
        while not result:
            request = urlopen("https://random-word-api.herokuapp.com/word?number=1")
            word = request.read().decode("utf-8")[2:-2]
            result, count = gen.check_topic(word)
            print(word, result, count)
        self._options._lineedit_topic.setText(word)


    def save_gallery(self, name = None):
        """
        Saving the gallery.
        """
        if name == None:
            name = f"{self.get_topic()}_gallery.png"
        cv2.imwrite(name, self.generator.canvas)


    def get_topic(self):
        """
        Returning topic from line edit widget.
        """
        return self._options.topic()


    def get_background(self):
        """
        Returning backround from line edit widget.
        """
        return self._options.background()


    def get_width(self):
        """
        Returning width from line edit widget.
        """
        return self._options.width()


    def get_height(self):
        """
        Returning height from line edit widget.
        """
        return self._options.height()


    def set_options_layout(self, status):
        if status:
            self._options.widget.setEnabled(True)
        else:
            self._options.widget.setEnabled(False)


    def generate_gallery(self):
        """
        Generating the gallery and setting it on the canvas
        """
        self._set_up_sizes()
        print("set up done")
        topic = self.get_topic()
        print(topic)
        background = self.get_background()
        width = self.get_width()
        height = self.get_height()
        self.set_options_layout(False)
        print(topic, background, width, height)
        
        
        self.generator = GalerryGenerator(width = width, height = height)
        print("creating generator")
        self.generator.generate_gallery(topic = topic, background = background)
        print("generate gallery")
        self.generator.cut_canvas()
        print("cut canvas")
        gallery = self.generator.canvas()
        small_gallery = self.generator.resized_canvas(self.canvas_width, self.canvas_height)
        print("generate small gallery")
        
        
        height, width = small_gallery.shape[0], small_gallery.shape[1]

        self._canvas = QImage(small_gallery.data, width, height, QImage.Format_RGB888)
        print("set canvas")

        self._widget_canvas.setPixmap(QPixmap.fromImage(self._canvas))
        self.set_options_layout(True)
         

    



app = QApplication([])
##if __name__ == "__main__":
##    screen = app.primaryScreen()
##    screen_width = screen.size().width()
##    screen_height = screen.size().height()
##    win = Window(screen_width, screen_height)
##    win.show()

from GalerryGenerator import GalerryGenerator
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsPixmapItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.scene = QGraphicsScene(self)
        
        self.view = QGraphicsView(self.scene, self)
        self.view.setGeometry(0, 0, 0, 0)
        
        self.setCentralWidget(self.view)


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
        q_image = QImage(numpy_image, numpy_image.shape[1], numpy_image.shape[0],
                         numpy_image.shape[1]*3, QImage.Format_RGB888)
        
        item = QPixmap(q_image)
        item = self.resize_item_to(item, width = 200)
        self.set_qpixmap_on_scene(item, x, y)
        

        
window = MainWindow()

gen = GalerryGenerator()
gen._photos_limit = 5
back = gen._find_photo("coal")
bird1 = gen._find_photo("bird").image()

window.set_background(back)
window.set_numpy_image_on_scene(bird1, 100, 100)
window.show()

app.exec_()
        
