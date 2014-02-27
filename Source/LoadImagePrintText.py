import cv2


def loadImagePrintTextBKP(cam, frame, debugREID=1, showPD=1, debugPD=0, PDthreshold=-1):
    """

    :param cam:
    :param frame:
    :param debugREID:
    """

    ## Pre-defined static variables
    CV_FILLED = -1
    red = (0, 0, 255)
    green = (0, 255, 0)
    black = (0, 0, 0)
    white = (255, 255, 255)
    thickness = 8
    if cam == 60:
        fontScale = 2  # 2 for Camera 60 (4MPixel), 1 for other cameras (1MPixel)
    else:
        fontScale = 1
    textHeight = 25 * fontScale  # 50 for cv2.FONT_HERSHEY_DUPLEX in cam60 image sizes
    letterWidth = 18 * fontScale
    smalltextHeight = 16 * fontScale  # 50 for cv2.FONT_HERSHEY_DUPLEX in cam60 image sizes
    smallletterWidth = 13 * fontScale

    JPEGspath = "RESOURCES\JPEG\camera" + str(cam) + "\\"
    filename = "I" + str(frame).zfill(5) + ".jpeg"
    image = cv2.imread(JPEGspath + filename)

    if showPD == 0:  # Don't print anything in image, just return the RAW
        return image

    detectionsPath = ".\RESOURCES\Detections\camera" + str(cam) + "\\"
    detectionFile = "I" + str(frame).zfill(5) + ".txt"

    fileText = open(detectionsPath + detectionFile, 'r')
    lines = fileText.readlines()
    fileText.close()

    res1 = [line.rstrip('\n').split(',') for line in lines]
    for i, values in enumerate(res1):
        res1[i] = [float(value) for value in values]
        left = int(res1[i][0])
        top = int(res1[i][1])
        right = left + int(res1[i][2])
        bottom = top + int(res1[i][3])
        confidence = res1[i][4]

        if confidence < PDthreshold:  # Don't print anything, neither detection or RE-ID
            return image

        confidence = str(confidence)

        ## Coordinate frame is (x,y) starting at top-left corner
        ## cv2.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]])
        cv2.rectangle(image, (left, top), (right, bottom), red, thickness)

        if debugPD:
            cv2.rectangle(image, (left, bottom),
                          (left + smallletterWidth * len(confidence), bottom + smalltextHeight + fontScale), white,
                          CV_FILLED)
            cv2.putText(image, confidence, (left, bottom + smalltextHeight), cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale,
                        color=black, thickness=thickness / 2)

        if len(res1[i]) > 5:  # There is a re-IDentification for this detection
            correctID = int(res1[i][5])
            REIDs = [int(value) for value in res1[i][6:]]

            ## Given a list of names, put one white box for each, on top of the image, and print the text on each respective
            # whitebox

            # Standard person names are PersonXXX
            texts = [str(k + 1) + ".Person" + str(ID).zfill(3) for k, ID in enumerate(REIDs)]
            # But for a few select persons that we do know their first name, we can re-name the text to their names
            # It would probably be nicer if made in a single cycle
            for k, ID in enumerate(REIDs):
                if ID == 22:
                    texts[k] = str(k + 1) + ".Matteo"
                if ID == 32:
                    texts[k] = str(k + 1) + ".Dario"

            for k, ID in enumerate(REIDs):
                text = texts[k]
                j = k
                # in thickness CV_FILLED is -1
                # +fontScale to give a little white margin on the bottom
                cv2.rectangle(image, (left, top - textHeight * j + fontScale),
                              (left + letterWidth * len(text), top - textHeight * (j + 1)), white, CV_FILLED)
                if ID == correctID:
                    color = green
                else:
                    color = red
                if debugREID == 0:
                    color = black
                cv2.putText(image, text, (left, top - textHeight * j), cv2.FONT_HERSHEY_DUPLEX, fontScale, color,
                            thickness=thickness / 2)

def loadImagePrintText(cam, frame, id_list = [], debugREID=1, showPD=1, debugPD=0, PDthreshold=-1):
    """

    :param cam:
    :param frame:
    :param debugREID:
    """

    ## Pre-defined static variables
    CV_FILLED = -1
    red = (0, 0, 255)
    green = (0, 255, 0)
    black = (0, 0, 0)
    white = (255, 255, 255)
    thickness = 8
    if cam == 60:
        fontScale = 2  # 2 for Camera 60 (4MPixel), 1 for other cameras (1MPixel)
    else:
        fontScale = 1
    textHeight = 25 * fontScale  # 50 for cv2.FONT_HERSHEY_DUPLEX in cam60 image sizes
    letterWidth = 18 * fontScale
    smalltextHeight = 16 * fontScale  # 50 for cv2.FONT_HERSHEY_DUPLEX in cam60 image sizes
    smallletterWidth = 13 * fontScale

    file_path = join(self.videos_dir, cam, frame + ".jpeg")
    image = cv2.imread(JPEGspath + filename)

    if showPD == 0:  # Don't print anything in image, just return the RAW
        return image

    detectionsPath = ".\RESOURCES\Detections\camera" + str(cam) + "\\"
    detectionFile = "I" + str(frame).zfill(5) + ".txt"

    fileText = open(detectionsPath + detectionFile, 'r')
    lines = fileText.readlines()
    fileText.close()

    res1 = [line.rstrip('\n').split(',') for line in lines]
    for i, values in enumerate(res1):
        res1[i] = [float(value) for value in values]
        left = int(res1[i][0])
        top = int(res1[i][1])
        right = left + int(res1[i][2])
        bottom = top + int(res1[i][3])
        confidence = res1[i][4]

        if confidence < PDthreshold:  # Don't print anything, neither detection or RE-ID
            return image

        confidence = str(confidence)

        ## Coordinate frame is (x,y) starting at top-left corner
        ## cv2.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]])
        cv2.rectangle(image, (left, top), (right, bottom), red, thickness)

        if debugPD:
            cv2.rectangle(image, (left, bottom),
                          (left + smallletterWidth * len(confidence), bottom + smalltextHeight + fontScale), white,
                          CV_FILLED)
            cv2.putText(image, confidence, (left, bottom + smalltextHeight), cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale,
                        color=black, thickness=thickness / 2)

        if len(res1[i]) > 5:  # There is a re-IDentification for this detection
            correctID = int(res1[i][5])
            REIDs = [int(value) for value in res1[i][6:]]

            ## Given a list of names, put one white box for each, on top of the image, and print the text on each respective
            # whitebox

            # Standard person names are PersonXXX
            texts = [str(k + 1) + ".Person" + str(ID).zfill(3) for k, ID in enumerate(REIDs)]
            # But for a few select persons that we do know their first name, we can re-name the text to their names
            # It would probably be nicer if made in a single cycle
            for k, ID in enumerate(REIDs):
                if ID == 22:
                    texts[k] = str(k + 1) + ".Matteo"
                if ID == 32:
                    texts[k] = str(k + 1) + ".Dario"

            for k, ID in enumerate(REIDs):
                text = texts[k]
                j = k
                # in thickness CV_FILLED is -1
                # +fontScale to give a little white margin on the bottom
                cv2.rectangle(image, (left, top - textHeight * j + fontScale),
                              (left + letterWidth * len(text), top - textHeight * (j + 1)), white, CV_FILLED)
                if ID == correctID:
                    color = green
                else:
                    color = red
                if debugREID == 0:
                    color = black
                cv2.putText(image, text, (left, top - textHeight * j), cv2.FONT_HERSHEY_DUPLEX, fontScale, color,
                            thickness=thickness / 2)

    return image

