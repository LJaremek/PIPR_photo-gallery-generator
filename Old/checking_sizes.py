from urllib.request import urlopen
from time import sleep
import numpy as np
import cv2


width = []
height = []
main_page = "https://source.unsplash.com/featured/?"
topics = ["glass", "bread", "gun", "dirt", "wood", "water"]

for topic in topics:
    for i in range(10):
        response = urlopen(main_page+topic)
        image = np.asarray(bytearray(response.read()), dtype = "uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        width.append(image.shape[1])
        height.append(image.shape[0])
        print(width[-1], height[-1])
        sleep(1)
    print("width", min(width), max(width))
    print("height", min(height), max(height))
