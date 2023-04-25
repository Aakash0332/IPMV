import cv2

img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

ret,thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
out = cv2.hconcat([img, thresh])

cv2.imshow('output', out)
cv2.waitKey(0)
