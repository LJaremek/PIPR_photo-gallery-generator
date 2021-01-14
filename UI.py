from GalerryGenerator import GalerryGenerator
from UIClasses.PyQt5InputDialog import InputDialog
from UIClasses.PyQt5Menus import (create_file_menu, create_gallery_menu,
                                  create_effects_menu, create_help_menu)
from UIClasses.PyQt5message import message
from efects import *
from errors import *
"""-----------------------------"""
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QInputDialog, QFileDialog
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView
from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap, QImage
import cv2


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self._gen = GalerryGenerator()
        self.scene = QGraphicsScene(self)
        self.statusBar() # pasek narzędziowy
        
        self._config_bar()
        
        self.view = QGraphicsView(self.scene, self)
        self.view.setGeometry(0, 0, 0, 0)
        
        self.setCentralWidget(self.view)


    def _config_bar(self):
        self.bar = self.menuBar()

        self.file = create_file_menu(self)
        self.gallery = create_gallery_menu(self)
        self.effects = create_effects_menu(self)
        self.help = create_help_menu(self)

        main_options = self.addToolBar("Main options")
        main_options.addAction(self.open)
        main_options.addAction(self.save)
        main_options.addAction(self.new)

        effects_options = self.addToolBar("Effects")
        effects_options.addAction(self.blur)
        effects_options.addAction(self.canny)
        effects_options.addAction(self.bilateral)
        effects_options.addAction(self.sepia)
        effects_options.addAction(self.cartoon)
        effects_options.addAction(self.pastel)
        effects_options.addAction(self.old_cartoon)


    def set_effects(self, bool_value):
        self.blur.setEnabled(bool_value)
        self.canny.setEnabled(bool_value)
        self.bilateral.setEnabled(bool_value)
        self.sepia.setEnabled(bool_value)
        self.cartoon.setEnabled(bool_value)
        self.pastel.setEnabled(bool_value)
        self.old_cartoon.setEnabled(bool_value)


    def set_edit_options(self, bool_value):
        self.save.setEnabled(bool_value)
        self.cut.setEnabled(bool_value)
        self.clear.setEnabled(bool_value)


    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "c\\",
                                                  "Image files (*.jpg *.png)")
        if file_name:
            loaded_file = cv2.imread(file_name)
            self.set_new_canvas(loaded_file)
            self.set_effects(True)
            self.set_edit_options(True)


    def put_effect(self, effect):
        selected_effect = effects_dict[effect]
        new_canvas = selected_effect( self._gen.canvas() )

        self.set_new_canvas(new_canvas)
        


    def new_gallery(self):
        ex = InputDialog()
        ex.exec()
        result = ex.getInputs()
        if result != None:
            self._gen = GalerryGenerator(result[2], result[3])
            self._gen.generate_gallery(topic = result[0], background = result[1])
            canvas = self._gen.canvas()
            self.set_numpy_image_on_scene(canvas, 0, 0)
            #photos = self._gen.photos()
            #background = self._gen.background()
            #self.set_background(background)
            #for photo in photos:
            #    window.set_numpy_image_on_scene(photo.image(), photo.x(), photo.y())
            self.set_edit_options(True)
            self.set_effects(True)
            self._gen.show_canvas()


    def cut_gallery(self):
        self.scene.clear()
        self._gen.cut_canvas()
        canvas = self._gen.canvas()
        self.set_numpy_image_on_scene(canvas, 0, 0)
        self.cut.setEnabled(False)


    def set_new_canvas(self, new_canvas):
        self._gen.set_canvas(new_canvas)
        
        self.scene.clear()
        self.set_numpy_image_on_scene(new_canvas, 0, 0)


    def clear_gallery(self):
        self.scene.clear()
        self.set_edit_options(False)
        self.set_effects(False)


    def save_gallery(self):
        text, okPressed = QInputDialog.getText(self, "Input file name","File name:", QLineEdit.Normal, "my_gallery.png",)
        if okPressed and text != '':
            if len(text.strip().split(".")) == 2:
                self._gen.save_gallery(text.strip())
            else:
                self._gen.save_gallery(text.strip()+".jpg")
                

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

        numpy_image = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR, numpy_image)
        
        
        q_image = QImage(numpy_image.data, numpy_image.shape[1], numpy_image.shape[0],
                         numpy_image.shape[1]*numpy_image.shape[2], QImage.Format_RGB888)
        
        item = QPixmap(q_image)
        #item = self.resize_item_to(item, width = 200)
        self.set_qpixmap_on_scene(item, x, y)


app = QApplication([])

window = MainWindow()
window.show()

app.exec_()
