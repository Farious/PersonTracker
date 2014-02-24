# -*- coding: utf-8 -*-
from __future__ import division
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

try:
    from wx import glcanvas

    haveGLCanvas = True
except ImportError:
    haveGLCanvas = False

try:
    from OpenGL.GL import *
    from OpenGL.GL import shaders
    from OpenGL.arrays import vbo
    from OpenGL.GLU import *
    from OpenGL.GLUT import *

    haveOpenGL = True
except ImportError:
    haveOpenGL = False

# Class defining the base OpenGL Canvas
class MyCanvasBase(glcanvas.GLCanvas):
    def __init__(self, parent):
        w, h = parent.Size

        # Empty image
        self.image = np.ones((w, h, 3), np.uint8) * 0

        # GLCanvas constructor
        glcanvas.GLCanvas.__init__(self, parent, -1)

        # Bool indicating if this was correctly initialized
        self.init = False

        # OpenGL Context
        self.context = glcanvas.GLContext(self)
        self.program = -1
        self.vbo = -1

        self.rH = 1
        self.rW = 1

        # Mouse position logic
        self.lastx = self.x = 30
        self.lasty = self.y = 30

        # Canvas size
        self.size = None

        # Event Binding
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnMouseUp)
        self.Bind(wx.EVT_MOTION, self.OnMouseMotion)
        return

    def OnEraseBackground(self, event):
        pass  # Do nothing, to avoid flashing on MSW.

    def OnSize(self, event):
        wx.CallAfter(self.DoSetViewport)
        return

    def DoSetViewport(self):
        size = self.GetClientSize()
        self.SetCurrent(self.context)
        self.RepositionQuad()
        glViewport(0, 0, size.width, size.height)

    def RepositionQuad(self):
        """We want to calculate the maximum size the image can have without
        distortions and taking up the maximum space available
        """
        if self.image.shape:
            # Image size
            imH, imW = self.image.shape[:2]

            # Size, in pixels, of the container canvas, glOrtho
            # is defined to be 0 to 1 in W and H. So 1 in each size
            # is equivalent to the container size in pixels
            clW, clH = self.GetClientSize()
            rW, rH = 1, 1

            # If the image is non-empty
            if imW > 0 and imH > 0 and clW > 0 and clH > 0:
                # Identify the minimum size
                rC = clW / clH
                rI = imW / imH

                val = 0
                if imH > imW:
                    if clH > clW:
                        val = 1
                    else:
                        val = 2
                else:
                    if clH > clW:
                        val = 3
                    else:
                        val = 4

                if val == 1 or val == 3:
                    rW = 1
                    rH = (1 / rI) * rC
                else:
                    rW = rI * (1 / rC)
                    rH = 1

                if rW * clW > clW:
                    rW = 1
                    rH = (1 / rI) * rC
                if rH * clH > clH:
                    rH = 1
                    rW = rI * (1 / rC)

            self.rH = rH
            self.rW = rW

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL()
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
    def load_shaders(self):
        self.SetCurrent(self.context)
        self.val = 0
        # Show OpenGL Information
        print "Vendor:   " + glGetString(GL_VENDOR)
        print "Renderer: " + glGetString(GL_RENDERER)
        print "OpenGL Version:  " + glGetString(GL_VERSION)
        print "Shader Version:  " + glGetString(GL_SHADING_LANGUAGE_VERSION)

        VERTEX_SHADER = shaders.compileShader("""#version 330 core
        layout(location = 0) in vec4 position;
        uniform vec2 scale;
        out vec2 uv;
        void main() {
        gl_Position = vec4(position.xy * scale, position.zw);
        uv = position.xy/2 + 0.5f;
        uv.y = 1 - uv.y;
        }""", GL_VERTEX_SHADER)

        FRAGMENT_SHADER = shaders.compileShader("""#version 330 core
        uniform sampler2D myTexture;
        in vec2 uv;
        out vec4 outputColor;
        void main() {
        outputColor = texture2D(myTexture, uv );
        }""", GL_FRAGMENT_SHADER)

        self.program = shaders.compileProgram(VERTEX_SHADER, FRAGMENT_SHADER)
        self.scale = glGetUniformLocation(self.program, "scale")
        self.texture = glGetUniformLocation(self.program, "myTexture")
        return


    def initialize_vertex_buffer(self):
        self.vbo = vbo.VBO(self.quad)
        return


    def InitGL(self):
        self.init = True

        self.quadObjectID = -1
        self.quad = np.array([
                [-1, -1, 0],
                [1, -1, 0],
                [1, 1, 0],
                [-1, 1, 0]
        ], 'f')

        self.initTexture = False

        self.load_shaders()
        self.initialize_vertex_buffer()

        # Setup the texture ID
        self.imageID = -1
        self.loadImage(self.image)


    def loadImage(self, image):
        self.SetCurrent(self.context)
        iy, ix = image.shape[:2]

        self.image = image

        if self.imageID == -1:
            self.imageID = glGenTextures(1)

        glActiveTexture(GL_TEXTURE0 + 1)
        if not self.initTexture:
            glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
            glBindTexture(GL_TEXTURE_2D, self.imageID)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, ix, iy, 0, GL_RGB, GL_UNSIGNED_BYTE, self.image)
            self.setupTexture()
        else:
            glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
            glBindTexture(GL_TEXTURE_2D, self.imageID)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, ix, iy, 0, GL_RGB, GL_UNSIGNED_BYTE, self.image)
            self.setupTexture()

        glUseProgram(self.program)
        glUniform1i(self.texture, self.imageID)
        glUseProgram(0)

        return


    def setupTexture(self):
        """Render-time texture environment setup"""
        self.SetCurrent(self.context)
        glActiveTexture(GL_TEXTURE0 + 1)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
        glBindTexture(GL_TEXTURE_2D, self.imageID)
        self.initTexture = True
        return

    def updateTexture(self):
        self.DoSetViewport()
        return

    def OnDraw(self):
        self.SetCurrent(self.context)

        # Clear Color Buffer
        glClearColor(240.0/255, 240.0/255, 240.0/255, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()

        # Draw using the shaders
        glUseProgram(self.program)

        glUniform2f(self.scale, self.rW, self.rH)

        if self.initTexture:
            glBindTexture(GL_TEXTURE_2D, self.imageID)
            glUniform1i(self.texture, self.imageID)


        # Bind the Quad
        self.vbo.bind()

        # Draw the Quad
        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointerf(self.vbo)
        glDrawArrays(GL_QUADS, 0, 4)

        # Unbind the Quad and stop using the shader
        self.vbo.unbind()
        glDisableClientState(GL_VERTEX_ARRAY)
        glUseProgram(0)

        # Swap buffer
        self.SwapBuffers()