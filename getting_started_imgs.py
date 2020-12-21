import numpy as np
import cv2 as cv

#Load a color image in grayscale
#first argument is the path to the file while the second argument is optional and specifies the format in which we wan
#t the image
img = cv.imread('test.jpeg', 0)
if img is None:
    sys.exit("Could not read the image")

#display an image in a window
cv.imshow('image', img)

#0 argument in waitkey sets loop indefinitely and waits for any key to terminate
k = cv.waitKey(0)
#overwrite img with edited img if user presses s 
if k == ord("s"):
    cv.imwrite("test.jpeg", img)

cv.destroyAllWindows()