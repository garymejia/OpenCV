import cv2 as cv

faceCascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv.imread("lena.png")
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

for(x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)


cv.imshow("Result", img)
cv.waitKey(0)