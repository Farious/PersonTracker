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
import wx
import wx.lib.mixins.inspection  # Ctrl+Alt+i to open an inspection window to
# retrieve information on WX widgets

#/-----------------------------------------------------------------------------
# Our imports
import wxTrackerForm
import pyGL
from fileIO import *


class MyApp(wx.App, wx.lib.mixins.inspection.InspectionMixin):
    """
    Class used to start the wx window. The wx.lib.mixins.inspection.InspectionMixin is a class that, when inherited,
    enables a debug mode. To enter this mode press: Ctrl - Alt - I. In the window that pops up we can debug every UI
    aspect.
    """

    def __init__(self, debug=False):
        super(MyApp, self).__init__()
        if debug:
            self.Init()  # initialize the inspection tool

    def OnInit(self):
        # Create the wxTrackerForm window (The Main App window)
        frame = CalcFrame(None)

        # Show the wxTrackerForm frame
        frame.Show(True)
        self.SetTopWindow(frame)
        return True


class CalcFrame(wxTrackerForm.TrackerMainFrame):
    """
    Defining the class that will inherit the TrackerMainFrame class created with wxFowmBuilder.
    It's in here that it is needed to populate the functions of each button\timers\etc.
    """

    def __init__(self, parent):
        # Initialize parent class
        wxTrackerForm.TrackerMainFrame.__init__(self, parent)

        # Needed properties
        self.fio = FileIO()
        self.refresh = False
        self.i = 0
        self.speed = 10  # Frames-per-second
        self.dFrame = 0  # Delta of frames since last update

        #/---------------------------------------------------------------------
        # Configuring the three OpenGL windows:
        # Video Stream;
        # ROC Curve;
        # Statistic Panel

        # Video Stream
        self.stream_canvas = pyGL.QuadCanvas(self.glPanel)
        self.glPanel.Layout()

        # Statistics Panel
        self.stats_canvas = pyGL.QuadCanvas(self.statTab)
        self.statTab.Layout()

        # ROC Panel
        self.roc_canvas = pyGL.QuadCanvas(self.rocTab)
        self.rocTab.Layout()

        # All panels
        self.glCanvasSet = {self.trackerTab: [(self.stream_canvas, self.glPanel)],
                            self.rocTab: [(self.roc_canvas, self.rocTab)],
                            self.statTab: [(self.stats_canvas, self.statTab)]}

        # Update Checklists
        self.fio.update_lists()
        self.personCheckList.Set(self.fio.retrieve_det_persons())
        self.videoChkList.Set(self.fio.retrieve_videos_list())

        return

    def reDraw(self, event):
        """
        This function is called whenever the window is resized
        """
        for winName in self.glCanvasSet.keys():
            if winName.IsShown():
                for canvas, panel in self.glCanvasSet.get(winName):
                    size = panel.Size
                    canvas.SetSize(size)
                    panel.SetSize(size)
                    if canvas.init:
                        canvas.OnSize(event)
                        canvas.OnDraw()
                    else:
                        canvas.InitGL()
                        canvas.loadImage(canvas.image)
                        canvas.OnSize(event)
                        canvas.OnDraw()
        event.Skip()
        self.Layout()
        return

    def update_ui( self, event ):
        self.Layout()
        return

    # """
    # wxPython Buttons - Main Tracker Tab - We need to implement the "video" management buttons.
    # """
    def rewindBtnClick(self, event):
        """
        Define behaviour when we click the "rewind" button
        """
        event.Skip()

    def prevFrameBtnClick(self, event):
        """
        Define the behaviour for the "previous frame" button
        """
        event.Skip()

    def stopBtnClick(self, event):
        """
        Define the behaviour for the "stop" button
        """
        event.Skip()

    def playBtnClick(self, event):
        """
        Define the behaviour for the "play" button
        """
        self.glTimer.Start(self.speed)
        event.Skip()

    def pauseBtnClick(self, event):
        """
        Define the behaviour for the "pause" button
        """
        self.glTimer.Stop()
        event.Skip()

    def nextFrameBtnClick(self, event):
        """
        Define the behaviour for the "next frame" button
        """
        event.Skip()

    def forwardBtnClick(self, event):
        """
        Define the behaviour for the "forward" button
        """
        event.Skip()

    # """
    # wxPython Timers - We need to implement our updating functions in here
    # """
    def updateStreamImage(self, event):
        """
        """
        frame_nr = self.fio.current_frame
        sel_vid = self.fio.selected_videos

        if sel_vid == {}:
            self.dFrame = 0
            return

        cam_name = sel_vid.keys()[0]

        all_frames = sel_vid[cam_name].keys()
        all_frames.sort()

        frame_name = all_frames[frame_nr]

        frame = self.fio.load_image_print_text(cam_name, frame_name, self.chkbox_show_det.Value, self.chkbox_show_reid.Value)

        if frame != None:
            self.stream_canvas.loadImage(frame)
            frame_nr += 1

        if frame_nr >= len(sel_vid["camera60"]):
            frame_nr = 0

        self.fio.current_frame = frame_nr

        event.Skip()
        return

    def updateROC(self, event):
        """
        """
        event.Skip()
        return

    def updateStatPanel(self, event):
        """
        """
        event.Skip()
        return

    def updateGLCanvas(self, event):
        """
        """
        self.reDraw(event)
        event.Skip()
        return

    def personSelectionUpdate(self, event):
        """
        """
        self.fio.person_input_from_chklist(self.personCheckList.GetChecked())
        return

    def videoSelectionUpdate(self, event):
        """
        """
        self.fio.video_input_from_chklist(self.videoChkList.GetChecked())
        return

    def updateCheckList(self, event):
        """
        """
        return

    # """
    # Behaviour events - Keyboard, toolbar clicks, etc
    # """
    def show_det_only(self, event):
        """
        """
        self.fio.show_all = not self.fio.show_all
        return

    def chkListKeyDown(self, event):
        """
        """
        if wx.GetKeyState(wx.WXK_F5):
            self.refresh = True
        event.Skip()
        return

    def chkListKeyUp(self, event):
        """
        """
        if self.refresh:
            self.refresh = False
            # DO STUFF HERE
            self.fio.update_lists()
            self.personCheckList.Set(self.fio.retrieve_det_persons())
            self.videoChkList.Set(self.fio.retrieve_videos_list())
        return

    def exit_form(self, event):
        """
        """
        self.Destroy()
        event.Skip()
        return

    def update_fps( self, event ):
        self.speed = 1000. / self.fps_slider.GetValue()
        if self.glTimer.IsRunning():
            self.glTimer.Start(self.speed)
        return

    def deactivate_reid( self, event ):
        self.chkbox_show_reid.Enabled = self.chkbox_show_det.Value
        return

if __name__ == "__main__":
    debug = True
    # WX Mandatory App creation
    app = MyApp(debug)

    # Start the WX Application
    app.MainLoop()