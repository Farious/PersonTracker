__author__ = 'athira'

import cv2
#from numpy import *


data = open("C:\\Users\\athira\\PycharmProjects\\HDA\\Demoset\\set18\\V000\\I00700.txt", 'r')
aa = data.read()
a = aa.rstrip('\n').split(',')[0]
a = int(float(a))
b = aa.rstrip('\n').split(',')[1]
b = int(float(b))
c = aa.rstrip('\n').split(',')[2]
c = int(float(c))
d = aa.rstrip('\n').split(',')[3]
d = int(float(d))
print aa.rstrip('\n').split(',')

#for line in data.readlines():
#print line
img = cv2.imread('C:\\Users\\athira\\PycharmProjects\\HDA\\Demoset\\camera18\\I00700.jpeg')
height, width, depth = img.shape
print height, width, depth

#Draw rectangle in an image
cv2.rectangle(img, (a, b), (a + c, b + d), (0, 255, 0), 3)
cv2.imshow('image', img)
cv2.waitKey(0)