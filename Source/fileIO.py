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
#/-----------------------------------------------------------------------------
# System imports
from os import listdir
from os.path import isfile, join
import cv2

#/-----------------------------------------------------------------------------
# Our imports
from Detection import *
from Tools import *
import ImageIO


class FileIO:
    """
    Class to deal with the GUI - File interactions.
    """

    def __init__(self, det_dir='./RESOURCES/Detections/.', vid_dir='./RESOURCES/JPEG/.'):
        # The directories specification.
        self.detection_dir = det_dir
        self.videos_dir = vid_dir

        # The actual list
        self.camera_list = {}
        self.det_list = {}
        self.person_ids = []

        # Selected persons's frame
        self.selected_persons = {}  # {"cam_name_1": {"frame_1": [id_1, ...], ...}, "cam_name_2": {...} ...}

        # Selected videos buffer
        self.iio = ImageIO.ImageIO()
        self.selected_videos = {}  # {"cam_name_1": {"frame_1": data_a, ...}, "cam_name_2": {...} ...}
        self.current_frame = -1

        # Frames that will appear
        self.frames_ref = {}  # {"cam_name_1": ["frame_1", "frame_2", ...], ...}
        self.frames = []

        # Should we show every frame or only those with the selected persons
        self.show_all = True
        return

    def __populate_camera__(self):
        """
        Process each folder in the specified video dir.
        This shouldn't be called directly
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
        This shouldn't be called directly
        """
        for f in listdir(self.detection_dir):
            # For each folder create an dictionary entry with the video name, frame number and detections in it
            if not isfile(join(self.detection_dir, f)):
                self.det_list[f] = {}
                det_list = listdir(join(self.detection_dir, f))
                det_list.sort()

                for det in det_list:
                    self.det_list[f][det.split('.')[0]] = self.__process_det_file(join(self.detection_dir, f, det))
        return

    def __process_det_file(self, det_file=''):
        """
        Defines what information to gather when processing each detection file.
        This shouldn't be called directly.
        Change anything in here as it will change what information it will gather from each file.
        """
        file_text = open(det_file, 'r')
        lines = file_text.readlines()
        file_text.close()

        result = []
        for line in lines:
            aux = [float(val) for val in line.rstrip('\n').split(',')]
            result.append(aux)

        for i, det in enumerate(result):
            if len(det) > 5:
                detection = Detection(det[0], det[1], det[2], det[3], det[4], det[5], det[6:])
                result[i] = detection.return_dict()
            else:
                detection = Detection(det[0], det[1], det[2], det[3], det[4], 0, [])
                result[i] = detection.return_dict()

        return result

    def __process_cam_file(self, cam_file=''):
        """
        Defines what information to gather when processing each cam's frame file.
        This shouldn't be called directly.
        Change anything in here as it will change what information it will gather from each file.

        Change this to do whatever you want. Becareful not to load each frame image into memory, as there may be
        infinite ammount
        """
        # self.iio.loadImage(cam_file)
        # result = self.iio.returnImage()
        return []

    def person_input_from_chklist(self, checked_ids):
        """
        This is called whenever the checkbox in the GUI is ticked
        checked_ids - integer lists, not directly related with the person's ID but with the array position
        """

        result = {}
        for camera in self.det_list.keys():
            result[camera] = {}

            cam = self.det_list[camera]
            for frame in cam:
                res_frame = []
                for det in cam[frame]:
                    for m_id in checked_ids:
                        r_id = self.person_ids[m_id]
                        if r_id in det['ids'] + [det['real_id']]:
                            res_frame.append(r_id)
                if res_frame:
                    result[camera][frame] = res_frame

        for cam in result.keys():
            for frame in result[cam].keys():
                result[cam][frame].sort()
                result[cam][frame] = remove_duplicates(result[cam][frame])

        self.selected_persons = result  # {"cam_name_1": {"frame_1": [id_1, ...], ...}, "cam_name_2": {...} ...}
        # Update which frames to show in the stream
        self.frames_to_show()
        return

    def video_input_from_chklist(self, checked_ids):
        """
        This is called whenever the checkbox in the GUI is ticked
        checked_ids - integer lists, this is directly linked with the videos list
        """
        cams = [self.camera_list.keys()[x] for x in checked_ids]

        result = {}  # {"cam_name_1": {"frame_1": data_a, ...}, "cam_name_2": {...} ...}
        for cam in cams:
            result[cam] = self.camera_list[cam]

        self.selected_videos = result

        # Update which frames to show in the stream
        self.frames_to_show()
        return

    def frames_to_show(self):
        """
        This method controls which frames should the main stream show.
        """
        sel_pers_frames = {}  # {"cam_name_1": ["frame_1", "frame_2", ...], ...}
        if self.selected_videos.keys():
            if self.show_all:
                for cam in self.selected_videos.keys():
                    sel_pers_frames[cam] = self.selected_videos[cam].keys()
            else:
                sel_pers_cam = self.selected_persons.keys()
                sel_cams = self.selected_videos.keys()
                for cams in sel_pers_cam and sel_cams:
                    if self.selected_persons[cams].keys():
                        sel_pers_frames[cams] = self.selected_persons[cams].keys()

        self.frames_ref = sel_pers_frames
        return

    def update_lists(self):
        """
        Updates every list based on the files existing in the current directory tree.
        """
        self.__populate_camera__()
        self.__populate_det__()
        return

    def retrieve_videos_list(self):
        """
        Retrieves the list of cameras found.
        """
        return self.camera_list.keys()

    def retrieve_det_persons(self):
        """
        Retrieve the list of persons found in the detection files.
        Based on the real_id and the found_id.
        This could be changed to show only the k-rank persons.
        """
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

    def retrieve_frame_from_cam(self, cam, frame):
        result = []

        file_path = join(self.videos_dir, cam, frame + ".jpeg")
        self.iio.loadImage(file_path)
        result = self.iio.returnImage()

        return result

    def load_image_print_text(self, cam, frame, showPD=1, showREID=1,
                              showOnlySelection=False, debugREID=1,
                              debugPD=0, PDthreshold=-1, rank = 10):
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

        file_path = join(self.videos_dir, cam, frame + ".jpeg")
        self.iio.loadImage(file_path)
        image = self.iio.returnImage()

        if showPD == 0:  # Don't print anything in image, just return the RAW
            return image

        if image.shape[1] > 2000 :
            fontScale = 2  # 2 for Camera 60 (4MPixel), 1 for other cameras (1MPixel)
        else:
            fontScale = 1

        textHeight = 25 * fontScale  # 50 for cv2.FONT_HERSHEY_DUPLEX in cam60 image sizes
        letterWidth = 18 * fontScale
        smalltextHeight = 16 * fontScale  # 50 for cv2.FONT_HERSHEY_DUPLEX in cam60 image sizes
        smallletterWidth = 13 * fontScale

        det_list = self.det_list

        for det in det_list[cam][frame]:
            confidence = det['confidence']
            left = det['left']
            top = det['top']
            right = det['right']
            bottom = det['bottom']
            real_id = det['real_id']
            det_ids = det['ids']

            exists = cam in self.selected_persons.keys()
            if exists:
                exists = frame in self.selected_persons[cam].keys()
            if exists:
                exists = real_id in self.selected_persons[cam][frame]

            if showOnlySelection and not exists:
                continue

            if confidence < PDthreshold:  # Don't print anything, neither detection or RE-ID
                continue

            confidence = str(confidence)

            if real_id != -1 and showREID:  # There is a re-IDentification for this detection
                correctID = real_id
                REIDs = det_ids

                if not correctID in REIDs[:rank]:
                    continue

            ## Coordinate frame is (x,y) starting at top-left corner
            ## cv2.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]])
            cv2.rectangle(image, (left, top), (right, bottom), red, thickness)

            if debugPD:
                cv2.rectangle(image, (left, bottom),
                              (left + smallletterWidth * len(confidence), bottom + smalltextHeight + fontScale), white,
                              CV_FILLED)
                cv2.putText(image, confidence, (left, bottom + smalltextHeight), cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale,
                            color=black, thickness=thickness / 2)

            if real_id != -1 and showREID:  # There is a re-IDentification for this detection
                correctID = real_id
                REIDs = det_ids

                if not correctID in REIDs[:rank]:
                    continue

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

                for k, ID in enumerate(REIDs[:rank]):
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


if __name__ == "__main__":
    fio = FileIO()
    fio.update_lists()

    print "a", fio.camera_list
    print "b", fio.retrieve_videos_list()
    print "c", fio.retrieve_det_persons()
    print "d", fio.det_list
    print "e", fio.camera_list

    # print fio.retrieve_frame_from_cam("camera60", "I00009")