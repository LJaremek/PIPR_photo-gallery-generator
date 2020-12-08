import requests
from time import sleep
from random import randint
import numpy as np
import cv2
from urllib.request import urlopen

main_page = "https://source.unsplash.com/featured/?"
key_word = "lego"

site = main_page+key_word

photos = []
for i in range(2):
    resp = urlopen(site)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    sleep(2)
