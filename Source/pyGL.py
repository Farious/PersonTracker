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

try:
    from wx import glcanvas

    haveGLCanvas = True
except ImportError:
    haveGLCanvas = False

try:
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GLUT import *

    haveOpenGL = True
except ImportError:
    haveOpenGL = False

# Class defining the base OpenGL Canvas
class MyCanvasBase(glcanvas.GLCanvas):
    def __init__(self, parent, image):
        self.image = image
        glcanvas.GLCanvas.__init__(self, parent, -1)
        self.init = False
        self.context = glcanvas.GLContext(self)

        # Mouse position logic
        self.lastx = self.x = 30
        self.lasty = self.y = 30

        # Canvas size
        self.size = None

        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnMouseUp)
        self.Bind(wx.EVT_MOTION, self.OnMouseMotion)

    def OnEraseBackground(self, event):
        pass  # Do nothing, to avoid flashing on MSW.

    def OnSize(self, event):
        wx.CallAfter(self.DoSetViewport)
        event.Skip()

    def DoSetViewport(self):
        size = self.size = self.GetClientSize()
        self.SetCurrent(self.context)
        glViewport(0, 0, size.width, size.height)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL(self.image)
            self.init = True
        self.OnDraw()

    def OnMouseDown(self, evt):
        self.CaptureMouse()
        self.x, self.y = self.lastx, self.lasty = evt.GetPosition()

    def OnMouseUp(self, evt):
        self.ReleaseMouse()

    def OnMouseMotion(self, evt):
        if evt.Dragging() and evt.LeftIsDown():
            self.lastx, self.lasty = self.x, self.y
            self.x, self.y = evt.GetPosition()
            self.Refresh(False)


class QuadCanvas(MyCanvasBase):
    def InitGL(self, image):
        self.init = True
        self.imageID = self.loadImage(image)

        # set viewing projection
        glMatrixMode(GL_PROJECTION)
        glOrtho(0, 1, 0, 1, -2, 2)

        # position viewer
        glMatrixMode(GL_MODELVIEW)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)

    def loadImage(self, image):
        ix, iy = image.shape[:2]
        ID = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, ID)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, ix, iy, 0, GL_RGB, GL_UNSIGNED_BYTE, image)
        return ID

    def setupTexture(self):
        """Render-time texture environment setup"""
        glEnable(GL_TEXTURE_2D)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
        glBindTexture(GL_TEXTURE_2D, self.imageID)

    def OnDraw(self):
        self.setupTexture()
        # clear color and depth buffers
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glBegin(GL_QUADS)
        glNormal3f(0.0, 0.0, 1.0)

        glTexCoord2f(0, 1)
        glVertex3f(0, 0, 0)

        glTexCoord2f(1, 1)
        glVertex3f(1, 0, 0)

        glTexCoord2f(1, 0)
        glVertex3f(1, 1, 0)

        glTexCoord2f(0, 0)
        glVertex3f(0, 1, 0)

        glEnd()

        self.SwapBuffers()