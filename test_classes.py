from SimpleCanvas import Canvas

def test_possibility_false():
    canvas = Canvas()
    canvas.add_photo((464, 934), (754, 1000), "P_01")
    result = canvas._possibility((176, 754), (470, 910))
    assert result == False


def test_possibility_true():
    canvas = Canvas()
    canvas.add_photo((464, 934), (754, 1000), "P_01")
    result = canvas._possibility((764, 234), (1254, 600))
    assert result == True


def test_photo_name():
    canvas = Canvas()
    canvas._photos = 5
    result = canvas._gen_name()
    assert result == "P_05"


def test_cut_canvas():
    canvas = Canvas()
    canvas._width = 100
    canvas._height = 150
    canvas._map = {(0,0): "P_01", (0,50): "P_01", (0,100): "None", (0,150): "None",
                   (50,0): "P_01", (50,50): "P_01", (50,100): "None", (50,150): "None",
                   (100,0): "None", (100,50): "None", (100,100): "None", (100,150): "None"}
    result = canvas.cut_canvas()
    assert result == (100, 100)


def test_add_photo():
    canvas = Canvas()
    canvas._width = 100
    canvas._height = 150
    canvas._photos = 5
    canvas._map = {(0,0): "None", (0,50): "None", (0,100): "None", (0,150): "None",
                   (50,0): "None", (50,50): "None", (50,100): "None", (50,150): "None",
                   (100,0): "None", (100,50): "None", (100,100): "None", (100,150): "None"}
    canvas.add_photo((0,20), (90, 80), "P_06")
    assert canvas._photos == 6
    assert canvas._map == {(0,0): "P_06", (0,50): "P_06", (0,100): "None", (0,150): "None",
                        (50,0): "P_06", (50,50): "P_06", (50,100): "None", (50,150): "None",
                        (100,0): "None", (100,50): "None", (100,100): "None", (100,150): "None"}


def test_find_free_place_None():
    canvas = Canvas()
    canvas._width = 150
    canvas._height = 150
    canvas._map = {(0,0): "None", (0,50): "None", (0,100): "None", (0,150): "None",
                   (50,0): "None", (50,50): "None", (50,100): "None", (50,150): "None",
                     (100,0): "None", (100,50): "None", (100,100): "None", (100,150): "None"}
    result = canvas.find_free_place(150, 100)
    assert result == None



def test_find_free_place_ok():
    canvas = Canvas()
    canvas._width = 200
    canvas._height = 200
    canvas._map = {(0,0): "P_01", (0,50): "None", (0,100): "None", (0,150): "None",
                   (50,0): "None", (50,50): "None", (50,100): "None", (50,150): "None",
                     (100,0): "None", (100,50): "None", (100,100): "None", (100,150): "None"}
    result = canvas.find_free_place(80, 80)
    assert result == (20, 70)
