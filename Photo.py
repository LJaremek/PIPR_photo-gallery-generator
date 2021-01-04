class Photo:
    def __init__(self, image, x, y, width, height, name):
        self._image = image
        self._x = x
        self._y = x
        self._width = width
        self._height = height
        self._name = name


    def image(self):
        """
        Return image
        """
        return self._image


    def x(self):
        """
        Return x
        """
        return self._x


    def y(self):
        """
        Return y
        """
        return self._y


    def width(self):
        """
        Return width
        """
        return self._width


    def height(self):
        """
        Return height
        """
        return self._height


    def width(self):
        """
        Return width
        """
        return self._width


    def name(self):
        """
        Return name
        """
        return self._name
