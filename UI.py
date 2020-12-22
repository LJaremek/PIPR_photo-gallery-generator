from GalerryGenerator import GalerryGenerator
"""-----------------------------"""
from PyQt5.QtWidgets import (QApplication, QMainWindow, # Main App
                             QVBoxLayout, QHBoxLayout, QGridLayout, # Layouts
                             QLabel, QLineEdit, QPushButton, # Widgets
                             QWidget) # Widget
from PyQt5.QtGui import QPainter, QPixmap, QImage # Canvas items
import tkinter
import cv2


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.showMaximized() # animacja, pasek menu (help, save, format pliku)
        self._set_up_sizes() # generate większy, reset

        self._create_options_layout()
        self._create_canvas_layout()
        self._create_main_layout()
        self.create_empty_canvas()

        self.setCentralWidget(self._widget_main)


    def _set_up_sizes(self):
        tk = tkinter.Tk()
        self.screen_width  = tk.winfo_screenwidth() # generuj losowo
        self.screen_height = tk.winfo_screenheight() # różne pakiety rozmiarów
        tk.destroy()
        self.canvas_width = int(self.screen_height*(2/3))
        self.canvas_height = int(self.screen_height*(8/9))


    def _create_options_layout(self):
        """
        Creating left panel - panel with config options.
        """
        self._widget_options = QWidget(self)
        self._gbox_options = QGridLayout()

        
        self._label_topic = QLabel("Topic:*")
        self._gbox_options.addWidget(self._label_topic, 0, 0)
        self._lineedit_topic = QLineEdit()
        self._lineedit_topic.setText("water")
        self._gbox_options.addWidget(self._lineedit_topic, 0, 1)

        self._label_background = QLabel("Background:")
        self._gbox_options.addWidget(self._label_background, 1, 0)
        self._lineedit_background = QLineEdit()
        self._lineedit_background.setText("sky")
        self._gbox_options.addWidget(self._lineedit_background, 1, 1)

        self._label_width = QLabel("Width:*")
        self._gbox_options.addWidget(self._label_width, 2, 0)
        self._lineedit_width = QLineEdit()
        self._lineedit_width.setText("1000")
        self._gbox_options.addWidget(self._lineedit_width, 2, 1)

        self._label_height = QLabel("Height:*")
        self._gbox_options.addWidget(self._label_height, 3, 0)
        self._lineedit_height = QLineEdit()
        self._lineedit_height.setText("1500")
        self._gbox_options.addWidget(self._lineedit_height, 3, 1)

        self._button_generate = QPushButton("Generate")
        self._button_generate.clicked.connect(self.generate_gallery)
        self._gbox_options.addWidget(self._button_generate, 4, 0)
        
        
        self._widget_options.setLayout(self._gbox_options)


    def _create_canvas_layout(self):
        """
        Creating right panel - panel with canvas with photos.
        """
        self._widget_canvas = QLabel()
        self._canvas = QPixmap(self.canvas_width, self.canvas_height)#QPixmap.fromImage(self.background)
        self._widget_canvas.setPixmap(self._canvas)

# click, pysimplegui
    def _create_main_layout(self):
        """
        Creating main layout with left and right panels.
        """
        self._widget_main = QWidget()
        self._layout_main = QHBoxLayout()
        self._layout_main.addWidget(self._widget_options, 1)
        self._layout_main.addWidget(self._widget_canvas, 4)
        self._widget_main.setLayout(self._layout_main)


    def create_empty_canvas(self):
        """
        Creating empty canvas.
        """
        self._canvas = QPixmap(self.canvas_width, self.canvas_height)#self._canvas = QPixmap.fromImage(self.background)
        self._widget_canvas.setPixmap(self._canvas)


    def add_photo(self):
        self._canvas = QImage("source-404.jpg") # some background in QImage
        
        photo = cv2.imread("left_arrow.png", cv2.IMREAD_GRAYSCALE)  # some photo in cv2
        
        photo = QImage(photo.data, photo.shape[1], photo.shape[0], QImage.Format_Grayscale8)#QImage("left_arrow.png")
        
        self.painter = QPainter()
        self.painter.begin(self._canvas)
        self.painter.drawImage(0, 0, photo)
        self.painter.end()

        self._widget_canvas.setPixmap(QPixmap.fromImage(self._canvas))


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
        return self._lineedit_topic.text()


    def get_background(self):
        """
        Returning backround from line edit widget.
        """
        return self._lineedit_background.text()


    def get_width(self):
        """
        Returning width from line edit widget.
        """
        return int(self._lineedit_width.text())


    def get_height(self):
        """
        Returning height from line edit widget.
        """
        return int(self._lineedit_height.text())


    def generate_gallery(self):
        """
        Generating the gallery and setting it on the canvas
        """
        topic = self.get_topic()
        background = self.get_background()
        width = self.get_width()
        height = self.get_height()
        
        self.generator = GalerryGenerator(width = width, height = height)
        self.generator.generate_gallery(topic = topic, background = background)
        self.generator.cut_canvas()
        cv2.imwrite("new_gallery1.jpg", self.generator.canvas())
        gallery = self.generator.canvas()
        small_gallery = self.generator.resized_canvas(self.canvas_width, self.canvas_height)
        
        
        height, width = small_gallery.shape[0], small_gallery.shape[1]

        self._canvas = QImage(small_gallery.data, width, height, QImage.Format_RGB888)

        self._widget_canvas.setPixmap(QPixmap.fromImage(self._canvas)) # zmienić wymiar?
         

    



app = QApplication([])
if __name__ == "__main__":
    win = Window()
    win.show()
