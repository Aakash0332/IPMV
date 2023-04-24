import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("image.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("a",gray)

hist,bins=np.histogram(gray.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf*float(hist.max())/cdf.max()
plt.plot(cdf_normalized,color='b')
plt.hist(gray.flatten(),256,[0,256],color='r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'),loc='upper left')
plt.show()

equ=cv2.equalizeHist(gray)
cv2.imshow("a",equ)

hist,bins=np.histogram(equ.flatten(),256,[0,256])
cdf=hist.cumsum()
cd_normalized = cdf*float(hist.max())/cdf.max()
plt.plot(cdf_normalized,color='b')
plt.hist(equ.flatten(),256,[0,256],color='r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'),loc='upper left')
plt.show()

cv2.waitKey(5000)
