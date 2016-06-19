import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import numpy as np

   
def setOrtho(w, h):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, w, h, 0, -1000, 1000)
    glMatrixMode(GL_MODELVIEW)

def addTexture(img):
    textureId = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textureId) 
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.shape[1], img.shape[0], 0, GL_BGR, GL_UNSIGNED_BYTE, img)
    
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST) 
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST) 
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

    return textureId

class FaceRenderer:
    def __init__(self, targetImg, textureImg, textureCoords, mesh):
        self.h = targetImg.shape[0]
        self.w = targetImg.shape[1]

        pygame.init()
        pygame.display.set_mode((self.w, self.h), DOUBLEBUF|OPENGL)
        setOrtho(self.w, self.h)

        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D) 

        self.textureCoords = textureCoords
        self.textureCoords[0, :] /= textureImg.shape[1] 
        self.textureCoords[1, :] /= textureImg.shape[0]

        self.faceTexture = addTexture(textureImg)
        self.renderTexture = addTexture(targetImg)

        self.mesh = mesh

    def drawFace(self, vertices):
        glBindTexture(GL_TEXTURE_2D, self.faceTexture) 

        glBegin(GL_TRIANGLES)
        for triangle in self.mesh:
            for vertex in triangle:
                glTexCoord2fv(self.textureCoords[:, vertex])
                glVertex3fv(vertices[:, vertex])
            
        glEnd()

    def render(self, vertices):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        self.drawFace(vertices)

        data = glReadPixels(0, 0, self.w, self.h, GL_BGR, GL_UNSIGNED_BYTE)
        renderedImg = np.fromstring(data, dtype=np.uint8)
        renderedImg = renderedImg.reshape((self.h, self.w, 3))
        for i in range(renderedImg.shape[2]):
            renderedImg[:, :, i] = np.flipud(renderedImg[:, :, i])

        pygame.display.flip()
        return renderedImg
