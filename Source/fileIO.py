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

from Detection import *
from Tools import *
import ImageIO


class FileIO:
    def __init__(self, det_dir='./RESOURCES/Detections/.', vid_dir='./RESOURCES/JPEG/.'):
        # The directories specification.
        self.detection_dir = det_dir
        self.videos_dir = vid_dir

        # The actual list
        self.camera_list = {}
        self.det_list = {}

        # Selected persons
        self.selected_persons = {}
        self.person_ids = []

        # Selected videos buffer
        self.iio = ImageIO.ImageIO()
        self.selected_videos = {}
        self.current_frame = -1

        # Frames that will appear
        self.frames_ref = {}
        self.frames = []
        # Should we show every frame or only those with the selected persons
        self.show_all = True
        return

    def __populate_camera__(self):
        """
        Process each folder in the specified video dir.
        """
        for f in listdir(self.videos_dir):
            # For each folder create an dictionary entry with the frames' names
            if not isfile(join(self.videos_dir, f)):
                self.camera_list[f] = {}
                for im in listdir((join(self.videos_dir, f))):
                    self.camera_list[f][im.split('.')[0]] = self.__process_cam_file(
                        join(self.videos_dir, f, im)
                    )
        return

    def __populate_det__(self):
        """
        Process each folder in the specified detection dir.
        """
        for f in listdir(self.detection_dir):
            # For each folder create an dictionary entry with the video name, frame number and detections in it
            if not isfile(join(self.detection_dir, f)):
                self.det_list[f] = {}
                for det in listdir(join(self.detection_dir, f)):
                    self.det_list[f][det.split('.')[0]] = self.__process_det_file(join(self.detection_dir, f, det))
        return

    def __process_det_file(self, det_file=''):
        file_text = open(det_file, 'r')
        lines = file_text.readlines()
        file_text.close()

        result = []
        for line in lines:
            aux = [float(val) for val in line.rstrip('\n').split(',')]
            result.append(aux)

        for i, det in enumerate(result):
            detection = Detection(det[0], det[1], det[2], det[3], det[4], det[5], det[6:])
            result[i] = detection.return_dict()

        return result

    def __process_cam_file(self, cam_file=''):
        self.iio.loadImage(cam_file)
        return self.iio.returnImage()

    def person_input_from_chklist(self, checked_ids):
        """
        checked_ids - integer lists
        """

        result = {}
        for camera in self.det_list.keys():
            result[camera] = []

            cam = self.det_list[camera]
            for frame in cam:
                for det in cam[frame]:
                    for m_id in checked_ids:
                        r_id = self.person_ids[m_id]
                        if r_id in det['ids']:
                            result[camera].append(frame)

        for cam in result:
            result[cam].sort()
            result[cam] = remove_duplicates(result[cam])

        self.selected_persons = result

        # Update which frames to show in the stream
        self.frames_to_show()
        return

    def video_input_from_chklist(self, checked_ids):
        cams = [self.camera_list.keys()[x] for x in checked_ids]

        self.selected_videos = {}
        for cam in cams:
            self.selected_videos[cam] = [videos for videos in self.camera_list[cam].values()]

        # Update which frames to show in the stream
        self.frames_to_show()
        return

    def frames_to_show(self):
        sel_pers_frames = {}

        if self.show_all:
            sel_pers_frames = self.selected_videos
        else:
            sel_pers_cam = self.selected_persons.keys()
            sel_cams = self.selected_videos.keys()
            for cams in sel_pers_cam and sel_cams:
                sel_pers_frames[cams] = self.selected_persons[cams]

        self.frames_ref = sel_pers_frames
        return

    def update_lists(self):
        self.__populate_camera__()
        self.__populate_det__()
        return

    def retrieve_videos_list(self):
        return self.camera_list.keys()

    def retrieve_det_persons(self):
        result = []
        for video in self.det_list.values():
            result += [[det['real_id']] + det['ids'] for frames in video.values() for det in frames]

        result = [y for x in result for y in x]
        result.sort()
        result = remove_duplicates(result)
        self.person_ids = result
        result = ['Person ' + str(val) for val in result]
        return result

    def retrieve_current_frame(self):

        return


if __name__ == "__main__":
    fio = FileIO()
    fio.update_lists()

    print "a", fio.camera_list
    print "b", fio.retrieve_videos_list()
    print "c", fio.retrieve_det_persons()
    print "d", fio.det_list
    print "e", fio.camera_list