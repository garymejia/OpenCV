import cv2 as cv
import numpy as np
from joining_images import StackedImages
widthImg = 640
heightImg = 480
frameWidth = 640 
frameHeight = 480
cap = cv.VideoCapture(0)
cap.set(3, widthImg)
cap.set(4, heightImg)
#brightness 
cap.set(10, 150)


def preProcessing(img):
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    imgBlur = cv.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv.Canny(imgBlur, 200, 200)
    kernel = np.ones((5, 5))
    imgDila = cv.dilate((imgCanny), kernel, iterations= 2)
    imgThres = cv.erode(imgDila, kernel, iterations=1)
    return imgThres

def getContours(img):
    biggest = np.array([])
    maxArea = 0
    contours,hierarchy = cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area>1000:
            #cv.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv.arcLength(cnt,True)
            approx = cv.approxPolyDP(cnt,0.02*peri,True)
            if area >maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
    cv.drawContours(imgContour, biggest, -1, (255, 0, 0), 20)
    return biggest


def reorder(myPoints):
    myPoints = myPoints.reshape((4,2))
    myPointsNew = np.zeros((4,1,2),np.int32)
    add = myPoints.sum(1)
    #print("add", add)
    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints,axis=1)
    myPointsNew[1]= myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    #print("NewPoints",myPointsNew)
    return myPointsNew


def getWarp(img, biggest):
    biggest = reorder(biggest)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
    matrix = cv.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv.warpPerspective(img, matrix, (widthImg, heightImg))
    return imgOutput


while True:
    success, img = cap.read()
    cv.resize(img,(widthImg, heightImg))
    imgContour= img.copy() 

    imgThres = preProcessing(img)
    stack = StackedImages()

    biggest = getContours(imgThres)
    if biggest.size != 0:
        imgWarped = getWarp(img, biggest)
        imageArray = ([img, imgThres], [imgContour, imgWarped])
    else:
        imageArray = ([img, imgThres], [img, img])
    
    si = stack.stackImages(0.6, imageArray)
    cv.imshow("warped", si)
    if(cv.waitKey(1) & 0xFF == ord('q')):
        break


 