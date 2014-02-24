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
from os import listdir
from os.path import isfile, join

class FileIO:
    def __init__(self, det_dir = './RESOURCES/Detections/.', vid_dir = './RESOURCES/JPEG/.'):
        # The directories specification.
        self.detection_dir = det_dir
        self.videos_dir = vid_dir

        # The actual list
        self.camera_list = {}
        self.det_list = {}
        return

    def __populate_camera__(self):
        """
        Process each folder in the specified video dir.
        """
        for f in listdir(self.videos_dir):
            # For each folder create an dictionary entry with the frames' names
            if not isfile(join(self.videos_dir, f)):
                self.camera_list[f] = [im for im in listdir(join(self.videos_dir, f)) if isfile(join(self.videos_dir, f, im))]
        return

    def __populate_det__(self):
        """
        Process each folder in the specified detection dir.
        """
        for f in listdir(self.videos_dir):
            # For each folder create an dictionary entry with the video name, frame number and detections in it
            if not isfile(join(self.videos_dir, f)):
                self.det_list[f] = {}
                for det in listdir(join(self.videos_dir, f)):
                    self.det_list[f][det] = self.__process_det_file(join(self.videos_dir, f, det))
        return

    def __process_det_file(self, det_file = ''):
        return []

    def retrieve_videos_list(self):
        return self.camera_list.keys()

if __name__ == "__main__":
    fio = FileIO()
    fio.__populate_camera__()
    fio.__populate_det__()

    print fio.camera_list
    print fio.retrieve_videos_list()
    print fio.det_list