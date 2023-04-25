import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("img1.png", cv2.IMREAD_GRAYSCALE)

#smoothing
mask = np.ones([3, 3], dtype=np.float32) / 9
img_new = cv2.filter2D(img, -1, mask)
plt.imshow(img_new, cmap=plt.cm.gray)
plt.show()

#Sharping
sharp_kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
sharp_img = cv2.filter2D(img, -1, sharp_kernel)
cv2.imshow('output image', sharp_img)
cv2.waitKey(0)
