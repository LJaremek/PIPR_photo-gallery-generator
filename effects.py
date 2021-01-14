import numpy as np
import cv2


def blur(image):
    return cv2.blur(image, (10, 10))


def canny(image):
    image = cv2.Canny(image, 100, 200)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # corretion shapes
    return image


def bilateral(image):
    return cv2.bilateralFilter(image, d=9, sigmaColor=200, sigmaSpace=200)


def sepia(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_1 = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray_1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 5)
    image = cv2.cvtColor(edges, cv2.COLOR_RGB2BGR) # corretion shapes
    return image


def bitwise(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_1 = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray_1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 5)
    color = cv2.bilateralFilter(image, d=9, sigmaColor=200,sigmaSpace=200)
    return cv2.bitwise_and(color, color, mask=edges)


def pastel(image):
    data = np.float32(image).reshape((-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
    ret, label, center = cv2.kmeans(data, 7, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    result = center[label.flatten()]
    return result.reshape(image.shape)

def old_cartoon(image):
    blurred = cv2.medianBlur(pastel(image), 3)
    return cv2.bitwise_and(blurred, blurred, mask=sepia(image))


def points(image):
    image = sepia(image)
    image = canny(image)
    return sepia(image)


effects_dict = {"blur": blur,
                "canny": canny,
                "bilateral": bilateral,
                "sepia": sepia,
                "bitwise": bitwise,
                "pastel": pastel,
                "old_cartoon": old_cartoon,
                "points": points}
