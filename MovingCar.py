from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *


def myInit():
    glMatrixMode(GL_PROJECTION)
    # glOrtho(-10, 10, -10, 10, -10, 10)
    gluPerspective(60, 1, .1, 50)
    gluLookAt(10, 10, 10, 0, 0, 0, 0, 1, 0)
    glClearColor(1, 1, 1, 1)


x = 0
angle = 0
add = .01


def draw():
    global x, angle, add
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(000, 0.000, 0)
    glBegin(GL_POLYGON)
    glVertex3d(-100, 0, -2)
    glVertex3d(30, 0, -2)
    glVertex3d(30, 0, 4)
    glVertex3d(-100, 0, 4)
    glEnd()
    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex3d(-38 - x, 0, 0)
    glVertex3d(-40 - x, 0, 0)
    glVertex3d(-40 - x, 0, 1.5)
    glVertex3d(-38 - x, 0, 1.5)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3d(-34 - x, 0, 0)
    glVertex3d(-36 - x, 0, 0)
    glVertex3d(-36 - x, 0, 1.5)
    glVertex3d(-34 - x, 0, 1.5)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3d(-30 - x, 0, 0)
    glVertex3d(-32 - x, 0, 0)
    glVertex3d(-32 - x, 0, 1.5)
    glVertex3d(-30 - x, 0, 1.5)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3d(-26-x, 0, 0)
    glVertex3d(-28-x, 0, 0)
    glVertex3d(-28-x, 0, 1.5)
    glVertex3d(-26-x, 0, 1.5)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3d(-22-x, 0, 0)
    glVertex3d(-24-x, 0, 0)
    glVertex3d(-24-x, 0, 1.5)
    glVertex3d(-22-x, 0, 1.5)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3d(-20-x, 0, 0)
    glVertex3d(-18-x, 0, 0)
    glVertex3d(-18-x, 0, 1.5)
    glVertex3d(-20-x, 0, 1.5)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3d(-14-x, 0, 0)
    glVertex3d(-16-x, 0, 0)
    glVertex3d(-16-x, 0, 1.5)
    glVertex3d(-14-x, 0, 1.5)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3d(-10-x, 0, 0)
    glVertex3d(-12-x, 0, 0)
    glVertex3d(-12-x, 0, 1.5)
    glVertex3d(-10-x, 0, 1.5)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3d(-6-x, 0, 0)
    glVertex3d(-8-x, 0, 0)
    glVertex3d(-8-x, 0, 1.5)
    glVertex3d(-6-x, 0, 1.5)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3d(-4-x, 0, 0)
    glVertex3d(-2-x, 0, 0)
    glVertex3d(-2-x, 0, 1.5)
    glVertex3d(-4-x, 0, 1.5)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3d(0-x, 0, 0)
    glVertex3d(2-x, 0, 0)
    glVertex3d(2-x, 0, 1.5)
    glVertex3d(0-x, 0, 1.5)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3d(6-x, 0, 0)
    glVertex3d(4-x, 0, 0)
    glVertex3d(4-x, 0, 1.5)
    glVertex3d(6-x, 0, 1.5)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3d(10-x, 0, 0)
    glVertex3d(8-x, 0, 0)
    glVertex3d(8-x, 0, 1.5)
    glVertex3d(10-x, 0, 1.5)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3d(12 - x, 0, 0)
    glVertex3d(14 - x, 0, 0)
    glVertex3d(14 - x, 0, 1.5)
    glVertex3d(12 - x, 0, 1.5)
    glEnd()
    glColor3f(1.000, 0.000, 0)
    glTranslate(x, 0, 0)
    glScale(1, .25, .5)
    glutWireCube(5)
    glLoadIdentity()


    glColor3f(1, 000, 0)
    glTranslate(x, 5 * .23, 0)
    glScale(.5, .2, .5)
    glutWireCube(5)
    glLoadIdentity()

    glColor3f(0, 1, 0)
    glTranslate(2.5 + x, -2.5 * .25, 2.5 * .5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(.125, .5, 12, 8)
    glLoadIdentity()

    glTranslate(2.5 + x, -2.5 * .25, - 2.5 * .5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(.125, .5, 12, 8)
    glLoadIdentity()

    glTranslate(-2.5 + x, -2.5 * .25, - 2.5 * .5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(.125, .5, 12, 8)
    glLoadIdentity()

    glTranslate(-2.5 + x, -2.5 * .25, 2.5 * .5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(.125, .5, 12, 8)
    glColor3f(1, 1.000, 0)
    glLoadIdentity()

    glTranslate(2.5 + x, 0, 1.5 * .5)
    glutSolidSphere(.3, 50, 50)
    glLoadIdentity()

    glTranslate(2.5 + x, 0, -1.5 * .5)
    glutSolidSphere(.3, 50, 50)
    glColor3f(0, 000, 0)




    if x >= 6 or x<=-18:
        add *= -1

    x += add
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Moving Car")
glutDisplayFunc(draw)
glutIdleFunc(draw)
myInit()
glutMainLoop()
