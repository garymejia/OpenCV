import cv2 as cv
import numpy as np


frameWidth = 640
frameHeight = 480
cap = cv.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

#myColors = [[38, 99, 79, 179, 170, 255],]
#myColors = [[38, 79, 170, 99, 179, 255],]
myColorValues = [0, 128, 0]
myPoints = []#[x, y, colorID, ]

def findColor(img, myColorValues):
    newPoints = []
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    lower = np.array([38, 79, 170])
    upper = np.array([99, 179, 255])
    mask = cv.inRange(imgHSV, lower, upper)
    x, y = getContours(mask)
    cv.circle(imgResult, (x, y), 10, myColorValues, cv.FILLED)
    if x!=0 and y!= 0:
        newPoints.append([x, y])
    """for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv.inRange(img, lower, upper)
        cv.imshow(str(color[0]), mask)
        getContours(mask)
"""
    return newPoints

def getContours(img):
    contours, Hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv.contourArea(cnt)
        #print(area)
        if area > 44:
            cv.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02*peri, True)
            x, y, w, h = cv.boundingRect(approx)
    return x+w//2,y

def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        #print(point)
        cv.circle(imgResult, (point[0][0], point[0][1]) , 10, myColorValues, cv.FILLED)


while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColorValues)
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newPoints)
    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColorValues)
    cv.imshow("Result", imgResult)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break