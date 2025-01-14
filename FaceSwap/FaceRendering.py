import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np


def setOrtho(w, h):
    """Sets the orthographic projection matrix for OpenGL"""
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, w, h, 0, -1000, 1000)
    glMatrixMode(GL_MODELVIEW)


def addTexture(img):
    """Creates and binds a texture to OpenGL"""
    textureId = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textureId)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    
    # Load texture image into OpenGL
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.shape[1], img.shape[0], 0, GL_BGR, GL_UNSIGNED_BYTE, img)
    
    # Set texture filtering and environment modes
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

    return textureId


class FaceRenderer:
    def __init__(self, targetImg, textureImg, textureCoords, mesh):
        """Initializes the OpenGL context and textures for the renderer"""
        self.h = targetImg.shape[0]
        self.w = targetImg.shape[1]

        pygame.init()
        pygame.display.set_mode((self.w, self.h), DOUBLEBUF | OPENGL)
        setOrtho(self.w, self.h)

        # Enable OpenGL depth testing and texture mapping
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)

        # Normalize the texture coordinates based on texture image dimensions
        self.textureCoords = textureCoords
        self.textureCoords[0, :] /= textureImg.shape[1]
        self.textureCoords[1, :] /= textureImg.shape[0]

        # Create OpenGL textures
        self.faceTexture = addTexture(textureImg)
        self.renderTexture = addTexture(targetImg)

        self.mesh = mesh

    def drawFace(self, vertices):
        """Draws the 3D face with texture applied"""
        glBindTexture(GL_TEXTURE_2D, self.faceTexture)

        glBegin(GL_TRIANGLES)
        for triangle in self.mesh:
            for vertex in triangle:
                glTexCoord2fv(self.textureCoords[:, vertex])
                glVertex3fv(vertices[:, vertex])
        glEnd()

    def render(self, vertices):
        """Renders the 3D scene and returns the resulting image"""
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.drawFace(vertices)

        # Read pixels from the OpenGL framebuffer
        data = glReadPixels(0, 0, self.w, self.h, GL_BGR, GL_UNSIGNED_BYTE)
        renderedImg = np.frombuffer(data, dtype=np.uint8)
        renderedImg = renderedImg.reshape((self.h, self.w, 3))
        
        # Flip the image vertically
        renderedImg = np.flipud(renderedImg)

        # Display the rendered image
        pygame.display.flip()
        return renderedImg
