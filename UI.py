from GalleryGenerator import GalleryGenerator
from UIClasses.PyQt5InputDialog import InputDialog
from UIClasses.PyQt5Menus import (create_file_menu, create_gallery_menu,
                                  create_effects_menu, create_help_menu)
from UIClasses.PyQt5message import message
from effects import *
from errors import *
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
        self.setWindowTitle("GalleryGenerator")
        self._gen = GalleryGenerator()
        self.scene = QGraphicsScene(self)
        self.statusBar()
        
        self._config_bar()
        
        self.view = QGraphicsView(self.scene, self)
        self.view.setGeometry(0, 0, 0, 0)
        
        self.setCentralWidget(self.view)

        self.new_gallery = cv2.imread("Images/new_gallery.png")
        self.wait_for_gallery = cv2.imread("Images/wait_for_gallery.png")
        self.set_numpy_image_on_scene(self.new_gallery, 0, 0)


    def _config_bar(self):
        """
        Configure menus and toolbars
        """
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
        effects_options.addAction(self.points)


    def set_effects(self, bool_value):
        """
        Setting up effects enbaled
        """
        self.blur.setEnabled(bool_value)
        self.canny.setEnabled(bool_value)
        self.bilateral.setEnabled(bool_value)
        self.sepia.setEnabled(bool_value)
        self.cartoon.setEnabled(bool_value)
        self.pastel.setEnabled(bool_value)
        self.old_cartoon.setEnabled(bool_value)
        self.points.setEnabled(bool_value)


    def set_edit_options(self, bool_value):
        """
        Setting up enable of options connected with gallery
        """
        self.save.setEnabled(bool_value)
        self.cut.setEnabled(bool_value)
        self.clear.setEnabled(bool_value)


    def open_file(self):
        """
        Function opens file with photo
        """
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "c\\",
                                                  "Image files (*.jpg *.png)")
        if file_name:
            loaded_file = cv2.imread(file_name)
            loaded_file = cv2.cvtColor(loaded_file, cv2.COLOR_RGB2BGR, loaded_file)
            self.set_new_canvas(loaded_file)
            self.set_effects(True)
            self.set_edit_options(True)


    def put_effect(self, effect):
        """
        Function puts the effect on the gallery
        """
        selected_effect = effects_dict[effect]
        new_canvas = selected_effect( self._gen.canvas() )
        self.set_new_canvas(new_canvas)
        


    def new_gallery(self):
        """
        Function makes new gallery
        """
        ex = InputDialog()
        

        if ex.exec():
            result = ex.getInputs()
            if result == None:
                return None
            self.scene.clear()
            self.set_numpy_image_on_scene(self.wait_for_gallery, 0, 0)
            message("Please wait!\nYour gallery is generating!", "Stand by", "Ok")

            self._gen = GalleryGenerator(result[2], result[3])

            self._gen.generate_gallery(topic = result[0], background = result[1])
            
            canvas = self._gen.canvas()
            canvas = cv2.cvtColor(canvas, cv2.COLOR_RGB2BGR, canvas)
            self.set_numpy_image_on_scene(canvas, 0, 0)
            
            self.set_edit_options(True)
            self.set_effects(True)


    def cut_gallery(self):
        """
        Function cuts out unnecessary empty gallery borders
        """
        self.scene.clear()
        self._gen.cut_canvas()
        canvas = self._gen.canvas()
        canvas = cv2.cvtColor(canvas, cv2.COLOR_RGB2BGR, canvas)
        self.set_numpy_image_on_scene(canvas, 0, 0)
        self.cut.setEnabled(False)


    def set_new_canvas(self, new_canvas):
        """
        Setting up the new canvas
        """
        self.scene.clear()
        self.set_numpy_image_on_scene(new_canvas, 0, 0)


    def clear_gallery(self):
        """
        Clearing canvas
        """
        self.scene.clear()
        self.set_numpy_image_on_scene(self.new_gallery, 0, 0)
        self.set_edit_options(False)
        self.set_effects(False)


    def save_gallery(self):
        """
        Saving gallery as file
        """
        text, okPressed = QInputDialog.getText(self, "Input file name","File name:", QLineEdit.Normal, "my_gallery.png",)
        if okPressed and text != '':
            
            canvas = self._gen.canvas()
            numpy_image = cv2.cvtColor(canvas, cv2.COLOR_RGB2BGR, canvas)
            cv2.imwrite(text.strip(), numpy_image)
            
            if len(text.strip().split(".")) == 2:
                cv2.imwrite(text.strip(), numpy_image)
            else:
                cv2.imwrite(text.strip()+".jpg", numpy_image)
                

    def set_qpixmap_on_scene(self, qpixmap, x, y):
        """
        Setting the qpixmap object on the canvas
        """
        item = QGraphicsPixmapItem(qpixmap)
        item.setPos(x, y)
        self.scene.addItem(item)


    def resize_item_to(self, item, width=False, height=False):
        """
        Scaling Qitem based on width / height
        """
        if width:
            return item.scaledToWidth(width)
        elif height:
            return item.scaledToHeight(height)
    

    def set_background(self, background):
        """
        Setting background on canvas
        """
        width, height = background.width(), background.height()
        bytesPerLine = width*3
        format_ = QImage.Format_RGB888
        
        background = QPixmap(QImage(background.image(), width, height, bytesPerLine, format_))
        self.set_qpixmap_on_scene(background, 0, 0)        
        

    def set_numpy_image_on_scene(self, numpy_image, x, y):
        """
        Setting numpy image on canvas
        """
        self._gen.set_canvas(numpy_image)
        q_image = QImage(numpy_image.data, numpy_image.shape[1], numpy_image.shape[0],
                         numpy_image.shape[1]*numpy_image.shape[2], QImage.Format_RGB888)
        item = QPixmap(q_image)
        self.set_qpixmap_on_scene(item, x, y)


def run():
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec_()


if __name__ == "__main__":
    run()
