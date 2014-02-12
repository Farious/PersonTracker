import numpy as np
import cv2
import linecache

CV_FILLED = -1
red = (0, 0, 255)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
thickness = 8

frame = 26

# user = "dario" # "Toshiba"
# datasetpath = "C:\Users\\" + user + "\Desktop\Dropbox\Work\HDA_Dataset\VideoSequences\JPEG\camera60\\"
datasetpath = "RESOURCES\\"
filename = "I000" + str(frame) + ".jpeg"
image = cv2.imread(datasetpath + filename) 

cv2.namedWindow("1", cv2.WINDOW_NORMAL)
cv2.resizeWindow("1", 2560/2, 1600/2)

##cv2.imshow("1",image)
##cv2.waitKey(0)

# detectionspath = "C:\\Users\\" + user + "\Desktop\Dropbox\Work\DemoHDA\\7.0.SmallLimited\\"
# detectionfile = "\set60\V000\I000" + str(frame) + ".txt"
detectionspath = "RESOURCES\\"
detectionfile = "I000" + str(frame) + ".txt"

line = 'place-holder'
ind = 1

fileText = open(detectionspath + detectionfile, 'r')
lines = fileText.readlines()
print "MISSING FCLOSE SOMEWHERE"

res1 = [line.rstrip('\n').split(',') for line in lines]
for i, values in enumerate(res1):
    res1[i] = [int(float(value)) for value in values][:4]
    lefttop = np.array((res1[i][0], res1[i][1]))
    rightbottom = lefttop + np.array((res1[i][2], res1[i][3]))
    left = res1[i][0]
    top = res1[i][1]
    right = left+res1[i][2]
    bottom = top+res1[i][3]

    imgR = image
    ## in thickness CV_FILLED is -1
    ## Coordinate frame is (x,y) starting at top-left corner
    ## cv2.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]])
    cv2.rectangle(imgR, (left, top), (right, bottom), red, thickness)

    # Given a list of names, put one white box for each, on top of the image, and print the text on each respective
    # whitebox
    texts = ("1.Matteo","2.Dario")
    fontScale = 2
    textHeight = 25*fontScale # 50 for cv2.FONT_HERSHEY_DUPLEX in cam60 image sizes
    textWidth = 800
    for j, text in enumerate(texts):
        cv2.rectangle(imgR, (left, top-textHeight*j), (right, top-textHeight*(j+1)), white, CV_FILLED) #tuple(topleft + (textWidth, 0))
        ## cv2.putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
        cv2.putText(imgR, text, (left, top-textHeight*j), cv2.FONT_HERSHEY_DUPLEX, fontScale, color=black, thickness=thickness/2)

    cv2.imshow("1",imgR)


cv2.waitKey(0)


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
