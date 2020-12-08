class Canvas:
    def __init__(self, width = 1500, height = 1000):
        self._width = width
        self._height = height
        self._photos = 0
        self._map = {}
        for x in range(0, width+1, 50):
            for y in range(0, height+1, 50):
                self._map[(x, y)] = "None"


    def _add_spaces(self, word):
        word = list(str(word))
        while len(word) < 4:
            word.insert(0, " ")
        return "".join(word)


    def show(self):
        print("     "+" ".join(list(map(self._add_spaces, range(0, self._width+1, 50)))))
        for y in range(0, self._height+1, 50):
            row = [self._add_spaces(y)]
            for x in range(0, self._width+1, 50):
                row.append(self._map[(x, y)])
            print(" ".join(row))


    def _align_the_number(self, number, max_value):
        """
        Alligning the number.
        """
        _range = max_value
        for r in range(0, _range, 50):
            if r <= number < r+50:
                return r
        return _range


    def _align_cords(self, cords):
        """
        Alligning the cords.
        """
        if type(cords) not in (tuple, list):
            return ValueError(f"cords ({type(cords)}) is not a tuple or a list")
        cords = [self._align_the_number(cords[0], self._width),
                 self._align_the_number(cords[1], self._height)]
        return cords


    def _possibility(self, cords_1, cords_2):
        """
        Checking if is a possibility to insert a photo in the place.
        """
        if cords_1[0] >= self._width or cords_1[1] >= self._height or cords_2[0] >= self._width or cords_2[1] >= self._height:
            return False
        cords_1 = self._align_cords(cords_1)
        cords_2 = self._align_cords(cords_2)
        for cords in self._map:
            x, y = cords
            if (cords_1[0] <= x <= cords_2[0]) and (cords_1[1] <= y <= cords_2[1]):
                if self._map[(x,y)] != "None":
                    return False
        return True


    def is_free_place(self, min_width = 360, min_height = 202):
        """
        Checking if there is a free space of the given dimensions.
        """
        for x in range(0, self._width, 50):
            for y in range(0, self._height, 50):
                if self._possibility((x, y), (x + min_width, y + min_height)):
                    return True
        return False


    def cut_canvas(self):
        empty_row = self._width//50
        for row in range(0, self._width+1, 50):
            good_row = True
            for column in range(0, self._height+1, 50):
                if self._map[(row, column)] != "None":
                    good_row = False
                    break
            if good_row:
                empty_row = row
                break
        empty_column = self._height//50
        for column in range(0, self._height+1, 50):
            good_column = True
            for row in range(0, self._width+1, 50):
                if self._map[(row, column)] != "None":
                    good_column = False
                    break
            if good_column:
                empty_column = column
                break
        return empty_row, empty_column
# vim do vs -norm,
# jupiter notebook
# ipython /\
# temux
# pytest html
    def add_photo(self, cords_1, cords_2, image_name):
        cords_1 = self._align_cords(cords_1)
        cords_2 = self._align_cords(cords_2)
        for cords in self._map:
            x, y = cords
            if (cords_1[0] <= x <= cords_2[0]) and (cords_1[1] <= y <= cords_2[1]):
                self._map[(x,y)] = image_name
        self._photos += 1


    def _gen_name(self):
        if len(str(self._photos)) == 1:
            return f"P_0{self._photos}"
        return f"P_{self._photos}"


    def find_free_place(self, width, height):
        for x in range(20, self._width, 50):
            for y in range(20, self._height, 50):
                if self._possibility((x, y), (x + width, y + height)):
                    photo_name = self._gen_name()
                    
                    self.add_photo((x, y), (x + width, y + height), photo_name)
                    
                    # photo = Photo(x, y, width, height, photo_name)
                    return x, y # photo
        return None
