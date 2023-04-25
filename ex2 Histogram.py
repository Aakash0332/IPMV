import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("img1.png", cv2.IMREAD_GRAYSCALE)
equ = cv2.equalizeHist(image)

plt.hist(image.ravel(), 256, [0, 256])
plt.show()

plt.hist(equ.ravel(), 256, [0, 256])
plt.show()
