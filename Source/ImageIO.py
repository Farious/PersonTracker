# -*- coding: utf-8 -*-
# Copyright {2014} {Instituto Superior Técnico - Lisboa}
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

__author__ = 'Fábio'

import cv2, numpy as np


class ImageIO:
    def __init__(self):
        self.image = 0
        self.imageID = ''

    def loadImage(self, filename):
        imArray = cv2.imread(filename)

        if imArray != None:
            self.image = imArray

    def returnImage(self):
        return self.image

    def showImage(self):
        if self.image != None:
            cv2.namedWindow('test', cv2.WINDOW_NORMAL)
            cv2.imshow('test', self.image)
            cv2.waitKey(0)

if __name__ == "__main__":
    io = ImageIO()
    io.loadImage('./RESOURCES/tree.jpg')
    io.showImage()