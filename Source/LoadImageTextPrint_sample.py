# import numpy as np
import cv2
# import linecache
import LoadImagePrintText as f
# >>> import os
# >>> os.chdir("C:\Users\dario\Desktop\Dropbox\Work\DemoHDA\git\Source\\")

## Input
cam = 60
frame = 26
debugREID = 1

img = f.loadImagePrintText(cam, frame, debugREID=0, debugPD=1, PDthreshold=20)

cv2.namedWindow("1", cv2.WINDOW_NORMAL)
cv2.resizeWindow("1", 2560/4, 1600/4)
cv2.imshow("1",img)
cv2.waitKey(0)






## Pre-defined static variables
# CV_FILLED = -1
# red = (0, 0, 255)
# green = (0, 255, 0)
# black = (0, 0, 0)
# white = (255, 255, 255)
# thickness = 8
# if cam == 60:
#     fontScale = 2  # 2 for Camera 60 (4MPixel), 1 for other cameras (1MPixel)
# else:
#     fontScale = 1
#
# # user = "dario" # "Toshiba"
# # JPEGspath = "C:\Users\\" + user + "\Desktop\Dropbox\Work\HDA_Dataset\VIDeoSequences\JPEG\camera60\\"
# JPEGspath = "RESOURCES\JPEG\camera" + str(cam) + "\\"
# filename = "I000" + str(frame) + ".jpeg"
# image = cv2.imread(JPEGspath + filename)
#
# cv2.namedWindow("1", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("1", 2560/2, 1600/2)
#
# # DetectionsPath = "C:\\Users\\" + user + "\Desktop\Dropbox\Work\DemoHDA\\7.0.SmallLimited\\"
# # detectionfile = "\set60\V000\I000" + str(frame) + ".txt"
# detectionsPath = "RESOURCES\Detections\set" + str(cam) + "\V000\\"
# detectionFile = "I000" + str(frame) + ".txt"
#
# # line = 'place-holder'
# ind = 1
#
# fileText = open(detectionsPath + detectionFile, 'r')
# lines = fileText.readlines()
# fileText.close()
#
# res1 = [line.rstrip('\n').split(',') for line in lines]
# for i, values in enumerate(res1):
#     res1[i] = [int(float(value)) for value in values]  # [:4]
#     leftTop = np.array((res1[i][0], res1[i][1]))
#     rightBottom = leftTop + np.array((res1[i][2], res1[i][3]))
#     left = res1[i][0]
#     top = res1[i][1]
#     right = left+res1[i][2]
#     bottom = top+res1[i][3]
#     if len(res1[i]) > 5:  # There is a re-IDentification for this detection
#         correctID = res1[i][5]
#         REIDs = res1[i][6:]
#
#     imgR = image
#     ## in thickness CV_FILLED is -1
#     ## Coordinate frame is (x,y) starting at top-left corner
#     ## cv2.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]])
#     cv2.rectangle(imgR, (left, top), (right, bottom), red, thickness)
#
#     ## Given a list of names, put one white box for each, on top of the image, and print the text on each respective
#     # whitebox
#
#     # Standard person names are PersonXXX
#     texts = [str(k+1) + ".Person" + str(ID).zfill(3) for k, ID in enumerate(REIDs)]
#     # But for a few select persons that we do know their first name, we can re-name the text to their names
#     # It would probably be nicer if made in a single cycle
#     for k, ID in enumerate(REIDs):
#         if ID == 22:
#             texts[k] = str(k+1) + ".Matteo"
#         if ID == 32:
#             texts[k] = str(k+1) + ".Dario"
#         # print texts[k]
#
#     # texts = ("1.Matteo","2.Dario")
#     textHeight = 25*fontScale  # 50 for cv2.FONT_HERSHEY_DUPLEX in cam60 image sizes
#     letterWidth = 18*fontScale
#     # for j, text in enumerate(texts):
#     for k, ID in enumerate(REIDs):
#         text = texts[k]
#         j=k
#         cv2.rectangle(imgR, (left, top-textHeight*j),
#                       (left + letterWidth*len(text), top-textHeight*(j+1)), white, CV_FILLED)  # tuple(topleft + (textWIDth, 0))
#         ## cv2.putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
#         if ID == correctID:
#             color = green
#         else:
#             color = red
#         if debugREID == 0:
#             color = black
#         cv2.putText(imgR, text, (left, top-textHeight*j), cv2.FONT_HERSHEY_DUPLEX, fontScale, color, thickness=thickness/2)
#
#     cv2.imshow("1",imgR)
#
#
# cv2.waitKey(0)


# FONT_HERSHEY_SIMPLEX, FONT_HERSHEY_PLAIN, FONT_HERSHEY_DUPLEX, FONT_HERSHEY_COMPLEX, FONT_HERSHEY_TRIPLEX,
# FONT_HERSHEY_COMPLEX_SMALL, FONT_HERSHEY_SCRIPT_SIMPLEX, or FONT_HERSHEY_SCRIPT_COMPLEX


# cv2.putText(imgR, text, tuple(topleft), cv2.FONT_HERSHEY_SIMPLEX, 3, black, thickness/2)
# cv2.putText(imgR, text, tuple(topleft+(0, textHeight)), cv2.FONT_HERSHEY_PLAIN, 3, black, thickness/2)
# cv2.putText(imgR, text, tuple(topleft+(0, textHeight*2)), cv2.FONT_HERSHEY_DUPLEX, 3, black, thickness/2)
# cv2.putText(imgR, text, tuple(topleft+(0, textHeight*3)), cv2.FONT_HERSHEY_COMPLEX, 3, black, thickness/2)
# cv2.putText(imgR, text, tuple(topleft+(0, textHeight*4)), cv2.FONT_HERSHEY_TRIPLEX, 3, black, thickness/2)
# cv2.putText(imgR, text, tuple(topleft+(0, textHeight*5)), cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, black, thickness/2)
# cv2.putText(imgR, text, tuple(topleft+(0, textHeight*6)), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 3, black, thickness/2)
# cv2.putText(imgR, text, tuple(topleft+(0, textHeight*7)), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 3, black, thickness/2)
