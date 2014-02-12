#-*- coding: utf-8 -*-
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
import sys, pygtk, gtk, gtk.glade
import gtk.gtkgl
# from OpenGL.GL import *
# from OpenGL.GLU import *

# our imports
import ImageIO as IO

class PersonTrackerGUI:
    def gtk_main_quit(self, widget, data=None):
        print "destroy signal occurred"
        gtk.main_quit()

    def __init__(self):
        self.gladeFile = 'HDA3.8.glade'
        self.GUIFolder = './GUI/'

        # Initializes the GTK builder (<3.0)
        self.gtkBuilder = gtk.Builder()
        self.gtkBuilder.add_from_file(self.GUIFolder + self.gladeFile)

        # Initializes and defines the signals\events in the window
        self.gtkBuilder.connect_signals(self)

        # Selects which window so show
        self.gtkBuilder.get_object('TrackerMainWindow').show_all()

        self.settings = gtk.settings_get_default()
        self.settings.props.gtk_button_images = True


if __name__ == "__main__":
    app = PersonTrackerGUI()
    gtk.main()