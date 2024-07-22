import cv2 as cv
import numpy as np

img1 = cv.imread("nature.jpg")
img2 = cv.imread("fun.jpg")
img3 = cv.imread("download.jpg")
# h , w = img2.shape[:2]
# gray = np.zeros((h,w),dtype=np.uint8)
# for i in range((img2.shape[0])):
#     for j in range(img2.shape[1]):
#        gray[i,j] = (0.07 * img2[i,j,0]) + (0.72 * img2[i,j,1]) + (0.21 * img2[i,j,2])
# img3 = cv.merge([res])
cv.imshow("new",img1)
# cv.imshow("green",g)
# cv.imshow("blue",b)
cv.waitKey(0)
cv.destroyAllWindows()