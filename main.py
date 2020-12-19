import numpy as np
import cv2

#Load a color image in grayscale
img = cv2.imread('test.jpeg', 0)

#display an image in a window
cv2.imshow('image', img)
#0 argument in waitkey sets loop indefinitely and waits for any key to terminate
cv2.waitKey(0)
cv2.destroyAllWindows()