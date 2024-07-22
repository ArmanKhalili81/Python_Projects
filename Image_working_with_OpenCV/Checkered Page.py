import cv2 as cv
import numpy as np

tmp1 =0
tmp2 =50
tmp3 =0
tmp4 =50
ls = [(255,0,0),(0,255,0),(0,0,255)]
im = np.zeros((500,500,3),dtype=np.uint8)
for i in range(10) :
    for j in range(10) :
        im[tmp1:tmp2,tmp3:tmp4] = (255,0,0)
        im[tmp1:tmp2,tmp3+50:tmp4+50] = (0,255,0)
        im[tmp1:tmp2,tmp3+100:tmp4+100] = (0,0,255)
        tmp3 += 150
        tmp4 += 150
    tmp1 += 50
    tmp2 += 50
    tmp3 =0
    tmp4 =50
    for k in range(10) :
        im[tmp1:tmp2,tmp3:tmp4] = (0,255,0)
        im[tmp1:tmp2,tmp3+50:tmp4+50] = (0,0,255)
        im[tmp1:tmp2,tmp3+100:tmp4+100] = (255,0,0)
        tmp3 += 150
        tmp4 += 150
    tmp1 += 50
    tmp2 += 50
    tmp3 =0
    tmp4 =50
    for j in range(10) :
        im[tmp1:tmp2,tmp3:tmp4] = (0,0,255)
        im[tmp1:tmp2,tmp3+50:tmp4+50] = (255,0,0)
        im[tmp1:tmp2,tmp3+100:tmp4+100] = (0,255,0)
        tmp3 += 150
        tmp4 += 150
    tmp1 += 50
    tmp2 += 50
    tmp3 =0
    tmp4 =50
cv.imshow("Windows" , im)
cv.waitKey(0)   