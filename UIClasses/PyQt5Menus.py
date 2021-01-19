from .PyQt5message import message
from PyQt5.QtWidgets import QAction
import sys
import os


def create_file_menu(self_):
    """
    Creating file menu bar
    """
    file = self_.bar.addMenu("File") # lepiej zwrócić niż nie

    self_.open = QAction("&Open...", self_)
    self_.open.setShortcut("Ctrl+O")
    self_.open.setToolTip("Open existing file")
    self_.open.triggered.connect(self_.open_file)
    file.addAction(self_.open)

    self_.save = QAction("&Save...", self_)
    self_.save.setShortcut("Ctrl+S")
    self_.save.setToolTip("Save generated gallery")
    self_.save.triggered.connect(self_.save_gallery)
    self_.save.setEnabled(False)
    file.addAction(self_.save)
    return file


def create_gallery_menu(self_):
    """
    Creating gallery menu bar
    """
    self_.gallery = self_.bar.addMenu("Gallery")
    
    self_.new = QAction("&New...", self_)
    self_.new.setShortcut("Ctrl+N")
    self_.new.setStatusTip("Create new gallery")
    self_.new.triggered.connect(self_.new_gallery)
    self_.gallery.addAction(self_.new)

    self_.cut = QAction("&Cut", self_)
    self_.cut.setShortcut("Ctrl+C")
    self_.cut.setStatusTip("Cut canvas to minimal size")
    self_.cut.triggered.connect(self_.cut_gallery)
    self_.cut.setEnabled(False)
    self_.gallery.addAction(self_.cut)

    self_.clear = QAction("Clear", self_)
    self_.clear.setStatusTip("Clear generated gallery")
    self_.clear.triggered.connect(self_.clear_gallery)
    self_.clear.setEnabled(False)
    self_.gallery.addAction(self_.clear)

    self_.exit_ = QAction("Exit", self_)
    self_.exit_.setStatusTip("Close program")
    self_.exit_.triggered.connect(sys.exit)
    self_.gallery.addAction(self_.exit_)


def create_effects_menu(self_):
    """
    Creating effects menu bar
    """
    self_.effects = self_.bar.addMenu("Effects")
    
    self_.blur = QAction("Blur", self_)
    self_.blur.setStatusTip("Blur all photos")
    self_.blur.triggered.connect(lambda: self_.put_effect("blur"))
    self_.blur.setEnabled(False)
    self_.effects.addAction(self_.blur)

    self_.canny = QAction("Edges", self_)
    self_.canny.setStatusTip("Edges of photos")
    self_.canny.triggered.connect(lambda: self_.put_effect("canny"))
    self_.canny.setEnabled(False)
    self_.effects.addAction(self_.canny)

    self_.bilateral = QAction("Mist", self_)
    self_.bilateral.setStatusTip("Mist all photos")
    self_.bilateral.triggered.connect(lambda: self_.put_effect("bilateral"))
    self_.bilateral.setEnabled(False)
    self_.effects.addAction(self_.bilateral)

    self_.sepia = QAction("Sepia")
    self_.sepia.setStatusTip("Put sepia on photos")
    self_.sepia.triggered.connect(lambda: self_.put_effect("sepia"))
    self_.sepia.setEnabled(False)
    self_.effects.addAction(self_.sepia)

    self_.cartoon = QAction("Cartoon")
    self_.cartoon.setStatusTip("cartoon effect on photos")
    self_.cartoon.triggered.connect(lambda: self_.put_effect("bitwise"))
    self_.cartoon.setEnabled(False)
    self_.effects.addAction(self_.cartoon)

    self_.pastel = QAction("Pastel")
    self_.pastel.setStatusTip("pastel effect on photos")
    self_.pastel.triggered.connect(lambda: self_.put_effect("pastel"))
    self_.pastel.setEnabled(False)
    self_.effects.addAction(self_.pastel)

    self_.old_cartoon = QAction("Old cartoon")
    self_.old_cartoon.setStatusTip("Old cartoon effect on photos")
    self_.old_cartoon.triggered.connect(lambda: self_.put_effect("old_cartoon"))
    self_.old_cartoon.setEnabled(False)
    self_.effects.addAction(self_.old_cartoon)

    self_.points = QAction("Points")
    self_.points.setStatusTip("Show points of photo")
    self_.points.triggered.connect(lambda: self_.put_effect("points"))
    self_.points.setEnabled(False)
    self_.effects.addAction(self_.points)


def how_to_start():
    message("To create new gallery select\n'Gallery' -> 'New...'\nenter topic and click Ok",
                "How to start", "Ok")

def open_docs():
    os.system("Dokumentacja.pdf")


def create_help_menu(self_):
    """
    Creating help menu bar
    """ 
    self_.help = self_.bar.addMenu("Help")
    
    self_.start = QAction("How to Start...", self_)
    self_.start.setStatusTip("Instruction how to start using program")
    self_.start.triggered.connect(how_to_start)
    self_.help.addAction(self_.start)

    self_.about = QAction("Documentation...", self_)
    self_.about.triggered.connect(open_docs)
    self_.help.addAction(self_.about)
