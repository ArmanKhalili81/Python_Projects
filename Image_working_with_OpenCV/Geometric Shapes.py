import cv2 as cv
import numpy as np

win = np.zeros((400,600,3),dtype=np.uint8)
#-------------------------------------------
cv.ellipse(win,(80,60),(70,40),0,0,360,color=(0,255,0),thickness=-1)
#------------------------------------------- oval
cv.rectangle(win,(180,20),(300,90),(0,0,255),thickness=-1)
#------------------------------------------- Rectangle
p1 = (440,0)
p2 = (460,60)
p3 = (525,50)
p4 = (470,94)
p5 = (500,150)
p6 = (440,110)
p7 = (380,150)
p8 = (410,94)
p9 = (360,50)
p10 = (420,60)
star = np.array([p1,p2,p3,p4,p5,p6,p7,p8,p9,p10])
cv.drawContours(win,[star],0,(188,51,247),-1)
#------------------------------------------------Star
cv.rectangle(win,(10,300),(120,200),(0,128,255),-1)
#------------------------------------------------Square
cv.circle(win,(250,250),60,(0,255,255),-1)
#------------------------------------------------Circle
pt1 = (450,200)
pt2 = (520,300)
pt3 = (380,300)
Triangle = np.array([pt1,pt2,pt3])
cv.drawContours(win,[Triangle],0,(194,33,65),-1)
cv.imshow("window",win)
cv.waitKey(0)
cv.destroyAllWindows()