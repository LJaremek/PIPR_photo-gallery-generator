from GalleryGenerator import GalleryGenerator


def test_init():
    gen = GalleryGenerator(height = 1500)
    assert gen._width == 1500
    assert gen._height == 1500
    assert len(gen.photos()) == 0
    assert gen._main_page == "https://source.unsplash.com/featured/?"


def test_resize_shapes():
    from Photo import Photo
    photo = Photo("image", "x", "y", 300, 600, "name")
    gen = GalleryGenerator()
    result = gen._resize_shapes(photo, 2)
    return result == (150, 300)


def test_background():
    from Photo import Photo
    gen = GalleryGenerator()
    background = Photo("image", "x", "y", "width", "height", "background")
    gen._background = background
    assert background == gen.background()


def test_photos():
    gen = GalleryGenerator()
    gen._approved_photos = ["photo1", "photo2", "photo3"]
    assert gen.photos() == ["photo1", "photo2", "photo3"]
