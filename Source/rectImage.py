__author__ = 'athira'

import cv2

# Load an image and read it
img = cv2.imread('cat.jpg')  #load the image
height, width, depth = img.shape
print height, width, depth

#Draw rectangle in an image
cv2.rectangle(img, (100, 0), (400, 200), (0, 255, 0), 3)


#Writ a text in an image
font = cv2.FONT_ITALIC
cv2.putText(img, 'HelloKitty!', (100, 500), font, 2, (255, 255, 0), 2)

cv2.namedWindow('image', )
cv2.imshow('image', img)
cv2.waitKey(0)