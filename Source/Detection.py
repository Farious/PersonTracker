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


class Detection:
    """
    Class to hold a detection configuration
    """

    def __init__(self, left, top, width, height, confidence, real, ids):
        self.left = int(left)
        self.top = int(top)
        self.right = int(left + width)
        self.bottom = int(top + height)
        self.confidence = confidence
        self.real_id = int(real)
        self.ids = [int(id) for id in ids]
        return

    def return_dict(self):
        return {'left': self.left,
                'top': self.top,
                'right': self.right,
                'bottom': self.bottom,
                'confidence': self.confidence,
                'real_id': self.real_id,
                'ids': self.ids
        }