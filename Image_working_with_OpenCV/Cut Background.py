import cv2 as cv
import numpy as np

img = cv.imread("Cat.jpg")
b,g,r = cv.split(img)
n = np.zeros(img.shape,dtype=np.uint8)
newlayer = cv.add(b,g)
for i in range(newlayer.shape[0]):
    for j in range(newlayer.shape[1]):
         n[i,j] = newlayer[i][j]
newlayer1 = cv.bitwise_or(n,img)
cv.imshow("win1",newlayer1)
cv.waitKey(0)