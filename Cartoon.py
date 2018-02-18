from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *


def draw():
    glClearColor(1, 1, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POLYGON)
    # Body
    glColor(0.000, 0.000, 0.545)
    glVertex2d(.2, .2)
    glVertex2d(-.2, .2)
    glVertex2d(-.2, -.2)
    glVertex2d(.2, - .2)
    glEnd()
    # Right Leg
    glColor(00.000, 0.000, 0.545)
    glBegin(GL_POLYGON)
    glVertex2d(.05, - .2)
    glVertex2d(.15, - .2)
    glVertex2d(.15, -.5)
    glVertex2d(.05, - .5)
    glEnd()
    # Left Leg
    glColor(0.000, 0.000, 0.545)
    glBegin(GL_POLYGON)
    glVertex2d(-.05, - .2)
    glVertex2d(-.15, - .2)
    glVertex2d(-.15, -.5)
    glVertex2d(-.05, - .5)
    glEnd()
    # Left Hand
    glColor(0.000, 0.000, 0.545)
    glBegin(GL_POLYGON)
    glVertex2d(-.2, .2)
    glVertex2d(-.2, .1)
    glVertex2d(-.4, -.1)
    glVertex2d(-.45, -.05)
    glEnd()
    # Right Hand
    glColor(0.000, 0.000, 0.545)
    glBegin(GL_POLYGON)
    glVertex2d(.2, .2)
    glVertex2d(.2, .1)
    glVertex2d(0.4, -.1)
    glVertex2d(.45, -.05)
    glEnd()
    # Neck
    glColor(0.000, 0.000, 0.545)
    glBegin(GL_POLYGON)
    glVertex2d(.035, .2)
    glVertex2d(-.035, .2)
    glVertex2d(-.035, .28)
    glVertex2d(.035, .28)
    glEnd()
    # Head
    glColor(0.000, 0.000, 0.545)
    glBegin(GL_POLYGON)
    glVertex2d(.2, .28)
    glVertex2d(-.2, .28)
    glVertex2d(-.2, .52)
    glVertex2d(.2, .52)
    glEnd()
    # Mouth
    glColor(0, 0, 0)
    glBegin(GL_POLYGON)
    a = .02
    b = .05

    for th in np.arange(0, 2 * pi, .001):
        r = (a * b) / sqrt(((b ** 2) * (cos(th) ** 2)) + ((a ** 2) * (sin(th) ** 2)))
        x = r * sin(th)
        y = r * cos(th)
        glVertex2d(x, y + .32)

    glEnd()
    # Nose
    glColor(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2d(0, .41)
    glVertex2d(-.03, .37)
    glVertex2d(.03, .37)
    glEnd()
    # Right Eye
    glColor(0, 0, 0)
    glBegin(GL_POLYGON)
    r = .04
    for th in np.arange(0, 2 * pi, .001):
        x = r * sin(th)
        y = r * cos(th)
        glVertex2d(x+.09, y+.44)

    glEnd()
    # Left Eye
    glColor(0, 0, 0)
    glBegin(GL_POLYGON)
    r = .04
    for th in np.arange(0, 2 * pi, .001):
        x = r * sin(th)
        y = r * cos(th)
        glVertex2d(x-.09, y+.44)
    glEnd()
    # Tears
    glColor(0.000, 1.000, 1.000)
    glBegin(GL_POLYGON)
    r = .007
    for th in np.arange(0, 2 * pi, .001):
        x = r * sin(th)
        y = r * cos(th)
        glVertex2d(x - .09, y + .37)
    glEnd()
    glBegin(GL_POLYGON)
    for th in np.arange(0, 2 * pi, .001):
        x = r * sin(th)
        y = r * cos(th)
        glVertex2d(x - .09, y + .31)
    glEnd()
    glBegin(GL_POLYGON)
    for th in np.arange(0, 2 * pi, .001):
        x = r * sin(th)
        y = r * cos(th)
        glVertex2d(x - .09, y + .34)
    glEnd()
    glBegin(GL_POLYGON)
    for th in np.arange(0, 2 * pi, .001):
        x = r * sin(th)
        y = r * cos(th)
        glVertex2d(x + .09, y + .37)
    glEnd()
    glBegin(GL_POLYGON)
    for th in np.arange(0, 2 * pi, .001):
        x = r * sin(th)
        y = r * cos(th)
        glVertex2d(x + .09, y + .31)
    glEnd()
    glBegin(GL_POLYGON)
    for th in np.arange(0, 2 * pi, .001):
        x = r * sin(th)
        y = r * cos(th)
        glVertex2d(x + .09, y + .34)
    glEnd()
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Likes Please")
glutDisplayFunc(draw)
glutMainLoop()
