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

#/-----------------------------------------------------------------------------
# Our imports
import ImageIO

def remove_duplicates(seq):
    """
    Removes duplicates from a list.
    As seen in:
    http://stackoverflow.com/a/480227
    """
    seen = set()
    seen_add = seen.add
    return [x for x in seq if x not in seen and not seen_add(x)]


def isfloat(value):
    """
    Checks if it is float.
    As seen in:
    http://stackoverflow.com/a/20929983
    """
    try:
        float(value)
        return True
    except ValueError:
        return False