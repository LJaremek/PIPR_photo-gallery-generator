class Photo:
    def __init__(self, image, x=None, y=None, width=None, height=None, name=None):
        self._image = image
        self._x = x
        self._y = y
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


    def setx(self, x):
        """
        Setting up a x
        """
        self._x = x


    def y(self):
        """
        Return y
        """
        return self._y


    def sety(self, y):
        """
        Setting up a y
        """
        self._y = y


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
