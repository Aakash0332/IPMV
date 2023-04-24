import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread("image.jpg")
imgs = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(imgs, cmap=plt.cm.gray)
m,n =imgs.shape
mask = np.ones([3, 3], dtype= int)
mask = mask/9
img_new = np.zeros([m, n])
for i in range (1, m-1):
 for j in range(1, n-1):
     temp = imgs[i-1, j-1]*mask[0, 0]+imgs[i-1, j]*mask[0, 1]+imgs[i-1, j+1]*mask[0, 2]+imgs[i, j-1]*mask[1, 0]+imgs[i, j]*mask[1, 1]+imgs[i, j+1]*mask[1, 2]+imgs[i+1, j]*mask[2, 1]+imgs[i+1, j+1]*mask[2, 2]
     img_new[i, j]= temp
img_new = img_new.astype(np.uint8)
plt.imshow(img_new, cmap=plt.cm.gray)
plt.show()

plt.imshow(imgs, cmap=plt.cm.gray)
sharp_kernel =np.array([[-1, -1,-1],
 [-1, 8, -1],
 [-1, -1, -1]])
sharp_img = cv2.filter2D(src=img, ddepth=-1, kernel=sharp_kernel)
cv2.imshow('output image ', sharp_img)
cv2.waitKey(0)
