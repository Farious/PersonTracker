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
import wx, numpy as np
import wx.lib.mixins.inspection

# Our imports
import wxTrackerForm
import pyGL
import ImageIO as IO


# Defining the class that will inherit the TrackerMainFrame class created with wxFowmBuilder.
class CalcFrame(wxTrackerForm.TrackerMainFrame):
    # Class constructor
    def __init__(self, parent):
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
                    # if size.width < size.height:
                    #     size.height = size.width
                    # else:
                    #     size.width = size.height
                    canvas.SetSize(size)
                    panel.SetSize(size)
                    if canvas.init:
                        canvas.RepositionQuad()
        self.Layout()

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
        io = IO.ImageIO()
        # io.loadImage("./RESOURCES/JPEG/camera60/I00009.jpeg")
        io.loadImage("./RESOURCES/tree.jpg")
        self.statsCanvas.loadImage(io.returnImage())
        event.Skip()

    # Define the behaviour for the "forward" button
    def forwardBtnClick(self, event):
        io = IO.ImageIO()
        io.loadImage("./RESOURCES/JPEG/camera60/I00009.jpeg")
        #io.loadImage("./RESOURCES/tree.jpg")
        self.setMainImage(io.returnImage())
        event.Skip()

    def setMainImage(self, image):
        self.streamCanvas.loadImage(image)


class MyApp(wx.App, wx.lib.mixins.inspection.InspectionMixin):
    def OnInit(self):
        self.Init()  # initialize the inspection tool
        frame = CalcFrame(None)
        frame.Show(True)
        self.SetTopWindow(frame)
        return True

if __name__ == "__main__":
    # WX Mandatory App creation
    # app = wx.App(False)
    app = MyApp()
    # Create the wxTrackerForm window (The Main App window)
    # frame = CalcFrame(None)

    # Show the wxTrackerForm frame
    # frame.Show(True)

    # Start the WX Application
    app.MainLoop()