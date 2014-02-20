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
    from OpenGL.GLU import *
    from OpenGL.GLUT import *

    haveOpenGL = True
except ImportError:
    haveOpenGL = False

def compile_program(vertex_src, fragment_src):
    '''
    Compile a Shader program given the vertex
    and fragment sources
    '''
    
    program = glCreateProgram()
 
    shaders = []
 
    for shader_type, src in ((GL_VERTEX_SHADER, vertex_src), 
                             (GL_FRAGMENT_SHADER, fragment_src)):
        shader = glCreateShader(shader_type)
        glShaderSource(shader, src)
        glCompileShader(shader)

        shaders.append(shader)
            
        status = glGetShaderiv(shader, GL_COMPILE_STATUS)
    
        if not status:
            if glGetShaderiv(shader, GL_INFO_LOG_LENGTH) > 0:
                log = glGetShaderInfoLog(shader)
                print >> sys.stderr, log.value
            glDeleteShader(shader)
            raise ValueError, 'Shader compilation failed'

        glAttachShader(program, shader)
 
    glLinkProgram(program)

    for shader in shaders:
        glDeleteShader(shader)
 
    return program
	
# Class defining the base OpenGL Canvas
class MyCanvasBase(glcanvas.GLCanvas):
    def __init__(self, parent):
        w, h = parent.Size
        # Empty image
        self.image = np.ones((w, h, 3), np.uint8) * 255

        # GLCanvas constructor
        glcanvas.GLCanvas.__init__(self, parent, -1)

        # Bool indicating if this was correctly initialized
        self.init = False

        # OpenGL Context
        self.context = glcanvas.GLContext(self)

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
		
		self.fragment_shader_src = '''
        uniform sampler1D TransferFunction;
        uniform sampler3D VolumeData;       
        void main(void)
        {            
            gl_FragColor = vec4(1.0, 0.0, 0.0, 0.0);
        }
        '''

        self.vertex_shader_src = '''
        void main(void)
        {
            gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
        }
        '''        
        self.fragment_src_file = 'earth.f.c'
        self.vertex_src_file = 'earth.v.c'
		
		# List of textures that need to be freed
        self.texture_list = []
        # List of VBOs that need to be freed
        self.buffers_list = []

    def OnEraseBackground(self, event):
        pass  # Do nothing, to avoid flashing on MSW.

    def OnSize(self, event):
        wx.CallAfter(self.DoSetViewport)
        event.Skip()

    def DoSetViewport(self):
        size = self.GetClientSize()
        self.SetCurrent(self.context)
        glViewport(0, 0, size.width, size.height)

    def RepositionQuad(self):
        """We want to calculate the maximum size the image can have without
        distortions and taking up the maximum space available
        """
        self.DoSetViewport()
        if self.image.shape:
            # Image size
            imH, imW = self.image.shape[:2]

            # Size, in pixels, of the container canvas, glOrtho
            # is defined to be 0 to 1 in W and H. So 1 in each size
            # is equivalent to the container size in pixels
            clW, clH = self.GetClientSize()
            rW, rH = 1, 1

            # If the image is non-empty
            if imW > 0 and imH > 0:
                # Identify the minimum size
                rC = clW/clH
                rI = imW/imH

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
                    rH = (1/rI) * rC
                else:
                    rW = rI * (1/rC)
                    rH = 1

                if rW * clW > clW:
                    rW = 1
                    rH = (1/rI) * rC
                if rH * clH > clH:
                    rH = 1
                    rW = rI * (1/rC)

            # Apply Transformation in Model View Space
            glLoadIdentity()
            glScalef(rW, rH, 0)

            # Move to Camera space to reset it and center the object
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            glOrtho(0, 1, 0, 1, -1, 1)
            glTranslatef((1-rW)/2, (1-rH)/2, 0)

            # Return to Model View Space
            glMatrixMode(GL_MODELVIEW)

            # Set Viewport and Draw
            self.DoSetViewport()
            self.OnDraw()

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
    def InitGL(self):        
        # Load the Shader sources from the files
        self.LoadShaderSources()
        
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glEnableClientState(GL_VERTEX_ARRAY)
        
        glDepthFunc(GL_LESS)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glShadeModel(GL_SMOOTH)
        
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClearDepth(1.0)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, self.width/float(self.height), 0.1, 1000.0)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
        self.SetupLighting()
        self.LoadVolumeData()
        self.LoadTransferFunction((self.t_graph.t_function.get_map() / array([255.0, 255.0, 255.0, 1.0])).flatten())
        self.program = compile_program(self.vertex_shader_src, self.fragment_shader_src)
        self.BuildGeometry()

    def loadImage(self, image):
        self.DoSetViewport()
        iy, ix = image.shape[:2]

        ID = glGenTextures(1)
        self.imageID = ID
        self.image = image
        glBindTexture(GL_TEXTURE_2D, self.imageID)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, ix, iy, 0, GL_RGB, GL_UNSIGNED_BYTE, self.image)
        return self.imageID

    def setupTexture(self):
        """Render-time texture environment setup"""
        glEnable(GL_TEXTURE_2D)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
        glBindTexture(GL_TEXTURE_2D, self.imageID)

    def updateTexture(self):
        self.DoSetViewport()

    def LoadShaderSources(self):
        try:
            self.fragment_shader_src = open(self.fragment_src_file).read()
        except IOError, e:
            print 'Fragment source not found, using default'

        try:
            self.vertex_shader_src = open(self.vertex_src_file).read()
        except IOError, e:
            print 'Vertex source not found, using default'
		
    def SetupUniforms(self):
       
        # Init the texture units
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_1D, self.transfer_function)
        glUniform1i(glGetUniformLocation(self.program, "TransferFunction"), 0)
        glUniform1i(glGetUniformLocation(self.program, "EnableLighting"), 
                    self.lighting)
        glUniform1i(glGetUniformLocation(self.program, "NumberOfLights"), 
                    self.light_count)
		
    def OnDraw(self):
        self.SetCurrent()
        if not self.init:
            self.InitGL()
            self.init = True

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        glTranslate(0.0, 0.0, -2.0)
        glRotate(self.rotation_y, 0.0, 1.0, 0.0)
        glRotate(self.rotation_x, 1.0, 0.0, 0.0)
        glTranslate(-0.5, -0.5, -0.5)

        glEnable(GL_BLEND)
        glEnable(GL_POLYGON_SMOOTH)


        # Draw the box
        glUseProgram(0)
        glColor(0.0, 1.0, 0.0)
        glDisable(GL_LIGHTING)
        glVertexPointerf(box)
        glDrawArrays(GL_LINES, 0, len(box))

        # Draw the slice planes
        glUseProgram(self.program)
        
        self.SetupUniforms()

        # Choose the correct set of planes
        if self.rotation_y < 45.0 or self.rotation_y >= 315.0:
            vertex_vbo = self.planes_vbo['xy'][0]
        elif self.rotation_y >= 45.0 and self.rotation_y < 135.0:
            vertex_vbo = self.planes_vbo['yz'][1]
        elif self.rotation_y >= 135.0 and self.rotation_y < 225.0:
            vertex_vbo = self.planes_vbo['xy'][1]
        elif self.rotation_y >= 225.0 and self.rotation_y < 315.0:
            vertex_vbo = self.planes_vbo['yz'][0]
                    
        # Render the planes using VBOs
        glBindBuffer(GL_ARRAY_BUFFER, vertex_vbo)
        glVertexPointer(3, GL_FLOAT, 0, None)
        glDrawArrays(GL_QUADS, 0, 4*plane_count)
        glBindBuffer(GL_ARRAY_BUFFER, 0)

        self.SwapBuffers()
        return