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
import wx
import wx.lib.mixins.inspection  # Ctrl+Alt+i to open an inspection window to retrieve information on WX widgets

# Our imports
import wxTrackerForm
import pyGL
import fileIO as FIO

# Class used to start the wx window. The wx.lib.mixins.inspection.InspectionMixin is a class that, when inherited,
# enables a debug mode. To enter this mode press: Ctrl - Alt - I. In the window that pops up we can debug every UI
# aspect.
class MyApp(wx.App, wx.lib.mixins.inspection.InspectionMixin):
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


# Defining the class that will inherit the TrackerMainFrame class created with wxFowmBuilder.
# It's in here that it is needed to populate the functions of each button\timers\etc.
class CalcFrame(wxTrackerForm.TrackerMainFrame):
    # Class constructor
    def __init__(self, parent):
        self.fio = FIO.FileIO()
        self.refresh = False
        self.i = 0
        #Initialize parent class
        wxTrackerForm.TrackerMainFrame.__init__(self, parent)

        # Configuring the three OpenGL windows: Video Stream; ROC Curve; Statistic Panel

        # Video Stream
        self.streamCanvas = pyGL.QuadCanvas(self.glPanel)
        self.glPanel.Layout()

        # Statistics Panel
        self.statsCanvas = pyGL.QuadCanvas(self.statsPanel)
        self.statsPanel.Layout()

        # ROC Panel
        self.rocCanvas = pyGL.QuadCanvas(self.rocTab)
        self.rocTab.Layout()

        # All panels
        self.glCanvasSet = {self.trackerTab: [(self.streamCanvas, self.glPanel),
                                              (self.statsCanvas, self.statsPanel)],
                            self.rocTab: [(self.rocCanvas, self.rocTab)]}

    # This function is called whenever the window is resized
    def reDraw(self, event):
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
                        canvas.OnSize(event)
                        canvas.OnDraw()
        event.Skip()
        self.Layout()

    """
    wxPython Buttons - Main Tracker Tab - We need to implement the "video" management buttons.
    """
    # Define behaviour when we click the "rewind" button
    def rewindBtnClick(self, event):
        event.Skip()

    # Define the behaviour for the "previous frame" button
    def prevFrameBtnClick(self, event):
        event.Skip()

    # Define the behaviour for the "stop" button
    def stopBtnClick(self, event):
        event.Skip()

    # Define the behaviour for the "play" button
    def playBtnClick(self, event):
        event.Skip()

    # Define the behaviour for the "pause" button
    def pauseBtnClick(self, event):
        event.Skip()

    # Define the behaviour for the "next frame" button
    def nextFrameBtnClick(self, event):
        event.Skip()

    # Define the behaviour for the "forward" button
    def forwardBtnClick(self, event):
        event.Skip()

    """
    wxPython Timers - We need to implement our updating functions in here
    """

    def updateStreamImage(self, event):
        event.Skip()
        return

    def updateROC(self, event):
        event.Skip()
        return

    def updateStatPanel(self, event):
        event.Skip()
        return

    def updateGLCanvas(self, event):
        self.reDraw(event)
        event.Skip()
        return

    """
    Behaviour events - Keyboard, toolbar clicks, etc
    """

    def chkListKeyDown(self, event):
        if wx.GetKeyState(wx.WXK_F5):
            self.refresh = True
        event.Skip()
        return

    def chkListKeyUp(self, event):
        if self.refresh:
            self.refresh = False
            # DO STUFF HERE
            print "Refresh"
        return

    def exit_form(self, event):
        self.Destroy()
        event.Skip()
        return


if __name__ == "__main__":
    debug = False
    # WX Mandatory App creation
    app = MyApp(debug)

    # Start the WX Application
    app.MainLoop()