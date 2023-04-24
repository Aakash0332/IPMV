import numpy as np
import matplotlib.pylab as plt
import cv2
img=cv2.imread('image.jpg')
cv2.imshow('input image',img)
kernel=np.ones((5,5),np.uint8)
img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilate = cv2.dilate(img, kernel, iterations=1)
img_boundary= img-img_erosion
img_open = cv2.dilate(img_erosion, kernel, iterations=1)
img_close = cv2.erode(img_dilate, kernel, iterations=1)
cv2.imshow('Erode image',img_erosion)
cv2.imshow('dilated image',img_dilate)
cv2.imshow('bound',img_boundary)
cv2.imshow('open',img_open)
cv2.imshow('close',img_close)
kernel1=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
kernel2=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
kernel3=cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
img_erosion = cv2.erode(img, kernel1, iterations=1)
img_dilate = cv2.dilate(img, kernel2, iterations=1)
cv2.waitKey(0)