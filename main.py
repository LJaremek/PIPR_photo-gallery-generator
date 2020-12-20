from UI import Window

app = Window()
app.show()

gen = GalleryGenerator()

gen.generate_galery(topic = "water")

gen.cut_canvas()
