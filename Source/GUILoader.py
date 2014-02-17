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
        self.streamCanvas.SetMinSize((300, 300))
        self.glPanel.SetSize((300, 300))
        self.glPanel.Layout()

        # Statistics Panel
        self.statsCanvas = pyGL.QuadCanvas(self.statsPanel)
        self.statsCanvas.SetMinSize((300, 300))
        self.statsPanel.SetSize((300, 300))
        self.statsPanel.Layout()

        # ROC Panel
        self.rocCanvas = pyGL.QuadCanvas(self.rocTab)
        self.rocCanvas.SetMinSize((300, 300))
        self.rocTab.SetSize((300, 300))
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
                    size = panel.GetSize()
                    if size.width < size.height:
                        size.height = size.width
                    else:
                        size.width = size.height
                    canvas.SetSize(size)
                    panel.SetSize(size)
                    if canvas.init:
                        canvas.DoSetViewport()
                        canvas.OnDraw()
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
        event.Skip()

    # Define the behaviour for the "forward" button
    def forwardBtnClick(self, event):
        event.Skip()

    def setMainImage(self, image):
        print 1


if __name__ == "__main__":
    # WX Mandatory App creation
    app = wx.App(False)

    # Create the wxTrackerForm window (The Main App window)
    frame = CalcFrame(None)

    # Show the wxTrackerForm frame
    frame.Show(True)

    # Start the WX Application
    app.MainLoop()