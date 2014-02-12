__author__ = 'athira'

import cv2
import numpy as np

print cv2.__version__

#Read an image in python
img1 =cv2.imread('cat.jpg',0) #read in gray scale
cv2.imshow("My first image",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.namedWindow('My first image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)


