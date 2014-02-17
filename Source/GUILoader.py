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
        #initialize parent class
        wxTrackerForm.TrackerMainFrame.__init__(self, parent)
        io = IO.ImageIO()
        io.loadImage('./RESOURCES/tree.jpg')
        self.canvas = pyGL.QuadCanvas(self.glPanel, io.image)
        self.canvas.SetMinSize((300, 300))

        self.glPanel.SetSize((300, 300))
        self.glPanel.Layout()

    # This function is called whenever the window is resized
    def reDraw(self, event):
        size = self.glPanel.GetSize()
        if size.width < size.height:
            size.height = size.width
        else:
            size.width = size.height
        self.canvas.SetSize(size)
        self.glPanel.SetSize(size)
        if (self.canvas.init):
            self.canvas.DoSetViewport()
            self.canvas.OnDraw()
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

if __name__ == "__main__":
    # WX Mandatory App creation
    app = wx.App(False)

    # Create the wxTrackerForm window (The Main App window)
    frame = CalcFrame(None)

    # Show the wxTrackerForm frame
    frame.Show(True)

    # Start the WX Application
    app.MainLoop()