import numpy as np
import matplotlib.pylab as plt
import cv2
img=cv2.imread('img2.jpeg')

cv2.imshow('input image',img)

kernel=np.ones((5,5),np.uint8)

img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=1)
img_opening = cv2.dilate(img_erosion , kernel, iterations=1)
img_closing = cv2.erode(img_dilation , kernel, iterations=1)
img_boundary= img-img_erosion

cv2.imshow('Eroded image',img_erosion )
cv2.imshow('dilated image',img_dilation )
cv2.imshow('Opening',img_opening )
cv2.imshow('Closing',img_closing )
cv2.imshow('boundary extracted',img_boundary )

cv2.waitKey(0)
