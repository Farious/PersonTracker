__author__ = 'athira'

import cv2

# Load an image and read it
img1 = cv2.imread('cat.jpg')  #load the image
img2 = cv2.imread('cat.jpg', 0)  #load the image in gray scale
cv2.imshow('image1', img1)
cv2.waitKey(0)

cv2.namedWindow('image2', cv2.WINDOW_NORMAL)  # There is a special case where you can already create a window and
# load image to it later. In that case, you can specify whether window is resizable or not.
#  It is done with the function cv2.namedWindow().
# By default, the flag is cv2.WINDOW_AUTOSIZE.
# But if you specify flag to be cv2.WINDOW_NORMAL, you can resize window.
# It will be helpful when image is too large in dimension and adding track bar to windows.
cv2.imshow('image2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Write an Image
cv2.imwrite('catgray.png', img2)

#sum up version

cv2.imshow('image3', img1)
k = cv2.waitKey(0)
if k == 10:  # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):  # wait for 's' key to save and exit
    cv2.imwrite('meow.png', img1)
    cv2.destroyAllWindows()

