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
