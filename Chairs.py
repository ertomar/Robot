from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def init():
    glMatrixMode(GL_PROJECTION)
    gluPerspective(60, 1, 0.1, 50)
    gluLookAt(10, 10, 10, 0, 0, 0, 0, 1, 0)
    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT)


def draw_cube(size, x, y, z):
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glMatrixMode(GL_MODELVIEW)
    glScale(x, y, z)
    glutSolidCube(size)
    glPopAttrib()
    glPopMatrix()
    glLoadIdentity()


def drawChair():
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    # seat
    draw_cube(2, 3, .5, 2)
    # Back

    glTranslate(2, 2.5, -2.5)
    draw_cube(2, 3, 3, .5)
    glTranslate(-8, 2.5, -2.5)
    draw_cube(2, 3, 3, .5)

    # Legs
    glTranslate(4, -5, -4.5)
    draw_cube(1, .6, 6, .6)
    glTranslate(-7, -5, -4)
    draw_cube(1, .6, 6, .6)

    glTranslate(4, -5, 0)
    draw_cube(1, .6, 6, .6)
    glTranslate(-7, -5, 0)
    draw_cube(1, .6, 6, .6)

    glTranslate(-3, -5, 0)
    draw_cube(1, .6, 6, .6)
    glTranslate(-14, -5, 0)
    draw_cube(1, .6, 6, .6)

    glTranslate(-3, -5, -4.5)
    draw_cube(1, .6, 6, .6)
    glTranslate(-14, -5, -4.5)
    draw_cube(1, .6, 6, .6)

    glPopAttrib()
    glPopMatrix()


def drawChairs():
    glMatrixMode(GL_MODELVIEW)
    glColor3f(0, 1, 1)
    glTranslate(-7, 0, 0)
    drawChair()
    glLoadIdentity()
    glTranslate(2, 0, 0)
    drawChair()
    glLoadIdentity()
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Chairs")
glutDisplayFunc(drawChairs)
init()
glutMainLoop()
