import numpy as np
import cv2

#Load a color image in grayscale
#first argument is the path to the file while the second argument is optional and specifies the format in which we wan
#t the image
img = cv2.imread('test.jpeg', 0)
if img is None:
    sys.exit("Could not read the image")

#display an image in a window
cv2.imshow('image', img)

#0 argument in waitkey sets loop indefinitely and waits for any key to terminate
cv2.waitKey(0)
cv2.destroyAllWindows()