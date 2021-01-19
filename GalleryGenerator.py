from SimpleCanvas import Canvas
from effects import Colors
from Photo import Photo
from errors import *
from urllib.request import urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup
from random import randint
from copy import deepcopy
from time import sleep
import numpy as np
import cv2


class GalleryGenerator:
    def __init__(self, width: int = 1500, height: int = 1000):
        self._width = width
        self._height = height
        self._canvas = np.zeros((height, width, 3), np.uint8)
        self._numeric_canvas = Canvas(width, height)
        self._main_page = "https://source.unsplash.com/featured/?"
        self._photos = []
        self._approved_photos = []
        self._photos_limit = 5


    def _create_canvas(self, background: str):
        """
        Creating a empty canvas.
        """
        if background in Colors.keys():
            self._canvas = np.zeros((self._height, self._width, 3), np.uint8)
            self._canvas[:,:] = Colors[background]
        else:
            background, response_code = self._download_photo(background)
            self._canvas = self._resize_photo(Photo(background), self._width, self._height).image()
        self._background = Photo(deepcopy(self._canvas), 0, 0, self._width, self._height, "background")


    def show_canvas(self):
        """
        Showing the canvas with photos.
        """
        cv2.imshow("gallery", self._canvas)


    def canvas(self):
        """
        Returning canvas as ndarray.
        """
        return self._canvas


    def set_canvas(self, new_canvas: np.ndarray):
        """
        Setting new canvas.
        """
        self._canvas = new_canvas


    def _check_difference(self, photo_1: np.ndarray, photo_2: np.ndarray):
        """
        Checking if is some difference between two photos.
        in:
        photo_1: NUMPY_ndarray
        photo_2: NUMPY_ndarray
        out:
        True if there are are a difference
        False if there are not a difference
        """
        difference = cv2.subtract(photo_1, photo_2)
        b, g, r = cv2.split(difference)
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            return True
        return False


    def _compare_photo(self, the_photo: np.ndarray):
        """
        Checking if the photo is not in the chosen photos.
        If it is in the photos:
            return True
        If it is not in the photos:
            return False
        """
        for photo in self._photos:
            if photo.image().shape != the_photo.shape:
                continue # another shapes => not the same
            
            difference = self._check_difference(photo.image(), the_photo)
            if difference:
                return False

        return True # there are differences


    def _download_photo(self, topic: str):
        """
        Downloading  photo on the topic.
        """
        response = urlopen(self._main_page+topic.replace(' ', '-'))
        code = response.status
        image = np.asarray(bytearray(response.read()), dtype = "uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        return image, code


    def _find_photo(self, topic: str):
        """
        Finding a new photo which is not in the chosen photos.
        """
        difference = False
        number_of_loop = 0
        while not difference:
            photo, response_code = self._download_photo(topic)
            difference = self._compare_photo(photo)
            if number_of_loop >= self._photos_limit:
                break
            number_of_loop += 1
        return Photo(photo, None, None, photo.shape[1], photo.shape[0], "photo")


    def _resize_shapes(self, photo: Photo, divider: int = 3):
        """
        Resizing shapes of photo.
        """
        width, height = photo.width()//divider, photo.height()//divider
        return width, height


    def _resize_photo(self, photo: Photo, new_width: int, new_height: int):
        """
        Returning resized photo.
        """
        resized_image = cv2.resize(photo.image(), (new_width, new_height))
        new_photo = Photo(resized_image, photo.x(), photo.y(), new_width, new_height, photo.name())
        return new_photo


    def resized_canvas(self, new_width: int, new_heigh: int):
        """
        Returning resized canvas
        """
        return cv2.resize(self._canvas, (new_width, new_height))


    def _add_photo(self, photo: Photo):
        """
        Adding the photo to the canvas if there are space for it.
        """
        width, height = self._resize_shapes(photo)
        
        cords = self._numeric_canvas.find_free_place(width, height)
        if not cords: # There are not free space for this photo :C
            return None
        
        x, y = cords
        photo.setx(x)
        photo.sety(y)
        resized_photo = self._resize_photo(photo, width, height)
        self._canvas[y:y+height, x:x+width] = resized_photo.image()
        self._approved_photos.append(resized_photo)


    def background(self):
        """
        Return background as Photo class.
        """
        return self._background


    def photos(self):
        """
        Return list with photos
        """
        return self._approved_photos


    def check_topic(self, topic: str):
        """
        Checking if the topic is correctly.
        If it is:
            return True
        else:
            return False
        """
        url = f"https://unsplash.com/s/photos/{topic.replace(' ', '-')}"
        try:
            request = urlopen(url)
        except URLError:
            assert UnsplashConnectError
            return False, -1
        soup = BeautifulSoup(request.read(), "html.parser")
        response = soup.findAll("span", {"class": "_3ruL8"})
        try:
            count = response[0].get_text()
            count = int(count) # count is a int number (<1000)
            return (count > 10, count)
        except ValueError: # count is bigger than 1000 (1.0k)
            return True, 300


    def cut_canvas(self):
        """
        Cutting the canvas to minimal possibility size.
        """
        new_width, new_height = self._numeric_canvas.cut_canvas()
        crop_canvas = self._canvas[0: new_height, 0: new_width]
        crop_canvas = cv2.cvtColor(crop_canvas, cv2.COLOR_BGR2RGB)
        self._canvas = crop_canvas


    def generate_gallery(self, topic: str, number_of_photos: int = 9, background: str = "Black"):
        """
        Generating new gallery with photos about given topic.
        """
        topic_bool, _ = self.check_topic(topic)
        number_of_loop = 0
        self._create_canvas(background)
        while topic_bool and (len(self._photos) < number_of_photos):
            if not self._numeric_canvas.is_free_space():
                break
            
            new_photo = self._find_photo(topic)
            self._add_photo(new_photo)
            
            self._photos.append(new_photo)

            number_of_loop += 1
            if number_of_loop >= self._photos_limit:
                break


    def save_gallery(self, file_name: str = "my_gallery.jpg"):
        """
        Saving the gallery as file_name
        """
        cv2.imwrite(file_name, self.canvas())


        

if __name__ == "__main__":
    gen = GalleryGenerator(1000, 800)

    gen.generate_gallery(topic = "new york", background = "Black")
    # gen.cut_canvas()
    gallery = gen.canvas()
    print(type(gallery))
    
    gen.show_canvas()
    
    gen._numeric_canvas.show()
