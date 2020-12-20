from SimpleCanvas import Canvas
from Colors import Colors
from Photo import Photo
from errors import *
"""-----------------------------"""
from urllib.request import urlopen
from random import randint
from time import sleep
import numpy as np
import cv2


class GalerryGenerator:
    def __init__(self, width = 1500, height = 1000):
        self._width = width
        self._height = height
        self._numeric_canvas = Canvas(width, height)
        self._main_page = "https://source.unsplash.com/featured/?"
        self._photos = []
        self._approved_photos = []


    def _create_canvas(self, background):
        """
        Creating a empty canvas.
        """
        if background in Colors.keys():
            self._canvas = np.zeros((self._height, self._width, 3), np.uint8)
            self._canvas[:,:] = Colors[background]
            return None
        background = self._download_photo(background)
        self._canvas = self._resize_photo(background, self._width, self._height)
        #self._canvas = np.zeros((self._height, self._width, 3), np.uint8)


    def show_canvas(self):
        """
        Showing the canvas with photos.
        """
        cv2.imshow("canvas", self._canvas)


    def canvas(self):
        """
        Returning canvas as cv2 image.
        """
        return self._canvas


    def _check_difference(self, photo_1, photo_2):
        """
        Checking if is some difference between two photos.
        """
        difference = cv2.subtract(photo_1, photo_2)
        b, g, r = cv2.split(difference)
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            return True
        return False


    def _compare_photo(self, the_photo):
        """
        Checking if the photo is not in the chosen photos.
        If it is in the photos:
            return True
        If it is not in the photos:
            return False
        """
        for photo in self._photos:
            if photo.shape != the_photo.shape:
                continue # another shapes => not the same
            
            difference = self._check_difference(photo, the_photo)
            if difference:
                return False

        return True # there are differences


    def _download_photo(self, topic):
        """
        Downloading  photo on the topic.
        """
        response = urlopen(self._main_page+topic)
        image = np.asarray(bytearray(response.read()), dtype = "uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        return image


    def _find_photo(self, topic):
        """
        Finding a new photo which is not in the chosen photos.
        """
        difference = False
        while not difference:
            photo = self._download_photo(topic)
            difference = self._compare_photo(photo)
        return photo


    def _find_photos(self, topic, count = 5):
        """
        Finding different photos about the topic.
        """
        for photo_nr in range(count):
            self._find_photo(topic)
            sleep(2)


    def _resize_shapes(self, photo, divider = 3):
        """
        Resizing shapes of photo.
        """
        width, height = photo.shape[1]//3, photo.shape[0]//3
        return width, height


    def _resize_photo(self, photo, new_width, new_height):
        """
        Returning resized photo.
        """
        return cv2.resize(photo, (new_width, new_height))


    def resized_canvas(self, new_width, new_height):
        """
        Returning resized canvas
        """
        return cv2.resize(self._canvas, (new_width, new_height))


    def _add_photo(self, photo):
        """
        Adding the photo to the canvas if there are space for it.
        """
        width, height = self._resize_shapes(photo)
        
        cords = self._numeric_canvas.find_free_place(width, height)
        if not cords: # There are not free space for this photo :C
            return None
        
        x, y = cords
        resized_photo = self._resize_photo(photo, width, height)
        self._canvas[y:y+height, x:x+width] = resized_photo
        self._approved_photos.append(resized_photo)


    def _check_topic(self, topic):
        random_photo = self._download_photo(topic) # sprawdzić odpowiedź servera
        error_photo = cv2.imread("source-404.jpg")
        try:
            difference = self._check_difference(random_photo, error_photo)
        except cv2.error:
            return True # corect topic
        return not difference


    def cut_canvas(self):
        """
        Cutting the canvas to minimal possibility size.
        """
        new_width, new_height = self._numeric_canvas.cut_canvas()
        crop_canvas = self._canvas[0: new_height, 0: new_width]
        crop_canvas = cv2.cvtColor(crop_canvas, cv2.COLOR_BGR2RGB)
        self._canvas = crop_canvas


    def generate_gallery(self, topic, number_of_photos = 9, background = "Black"):
        """
        Generating new gallery with photos about given topic.
        """
        self._create_canvas(background)
        while len(self._photos) < number_of_photos:
            if not self._numeric_canvas.is_free_space():
                break        
            new_photo = self._find_photo(topic)
            self._add_photo(new_photo)
            sleep(1.5)
            self._photos.append(new_photo)

        
# min photo shape: 1080, 607 -> 360, 202 - > 8x5

if __name__ == "__main__":
    gen = GalerryGenerator(1000, 1500)

    gen.generate_gallery(topic = "turkey", background = "Black")
    gen.cut_canvas()
    gallery = gen.canvas()
    #cv2.imwrite("new_gallery.jpg", gallery)

    
    gen.show_canvas()
    
    gen._numeric_canvas.show()
