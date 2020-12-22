import numpy as np 
import cv2 as cv

#create a black image
img = np.zeros((512, 512, 3), np.uint8)

#draw a diagonal blue line with thickness of 5 px
cv.line(img, (0,0), (511, 511), (255, 0, 0), 5)
cv.rectangle(img, (30, 30), (300, 200), (0, 255, 0), 5) 
cv.circle(img, (200, 200), 80, (255, 0, 0), 3) 
cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)

cv.imshow('dark', img) 
  
# Allows us to see image 
# untill closed forcefully 
cv.waitKey(0) 
cv.destroyAllWindows() 