######################################################################
# Name: Norman Cook
# Date: 11/04/2019
# Description: Plots points on a canvas that follow the chaos game
#   method for creating a Sierpinski Triangle, Sierpinski Carpet, and
#   Hexagon fractal.
######################################################################
from Tkinter import *
import importlib

# the 2D point class
class Point(object):
    # the constructor
    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    # getters and setters
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def interpt(self, other, r):
        # make sure that the distance ratio is expressed from a
        # smaller component value to a larger one
        # first, the x-component
        rx = r
        if (self.x > other.x):
            rx = 1.0 - r
        # next, the y-component
        ry = r
        if (self.y > other.y):
            ry = 1.0 - r

        # calculate the new point's coordinates
        # the difference in the components (distance between the
        # points) is first scaled by the specified distance ratio
        # the minimum of the components is then added back in order
        # to obtain the coordinates in vetween the two points (and
        # not with respect to the origin)
        x = abs(self.x - other.x) * rx + min(self.x, other.x)
        y = abs(self.y - other.y) * ry + min(self.y, other.y)

        return Point(x, y)

class Fractal(Canvas):
    def __init__(self):
        # dimensions for the canvas
        self.dimensions = {}
        self.dimensions["MIN_X"] = 5
        self.dimensions["MAX_X"] = 585
        self.dimensions["MIN_Y"] = 5
        self.dimensions["MAX_Y"] = 505
        self.dimensions["MID_X"] = (self.dimensions["MAX_X"] - self.dimensions["MIN_X"]) / 2
        self.dimensions["MID_Y"] = (self.dimensions["MAX_Y"] - self.dimensions["MIN_Y"]) / 2

        # the default number of points to plot is 50,000
        self.num_points = 50000
        # the default distance ratio is 0.5 (halfway)
        self.r = 0.5
        # list of Point instances for the fractal
        self.vertices = []

    # getters and setters
    @property
    def dimensions(self):
        return self.dimensions

    @property
    def num_points(self):
        return self._num_points

    @num_points.setter
    def num_points(self, value):
        self._num_points = value

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, value):
        self._r = value

    @property
    def vertices(self):
        return self._vertices

    @vertices.setter
    def vertices(self, value):
        self._vertices = value

    # calculates the fractal's vertices on the canvas in the x direction
    def frac_x(self, r):
        return int((self.dimensions["MAX_X"] - \
                    self.dimensions["MIN_X"]) * r) + \
                    self.dimensions["MIN_X"]

    # calculates the fractal's vertices on the canvas in the y direction
    def frac_y(self, r):
        return int((self.dimensions["MAX_Y"] - \
                    self.dimensions["MIN_Y"]) * r) + \
                    self.dimensions["MIN_Y"]

# creates the Sierpinski Triangle
class SierpinskiTriangle(Fractal):
    def __init__(self):
        # inherit from the Fractal class
        Fractal.__init__(self)

        # values for sierpinski triangle
        self.num_points = 50000
        self.r = 0.5

        # calculate vertices
        vertice1 = Point(self.dimensions["MID_X"], self.dimensions["MIN_Y"])
        vertice2 = Point(self.dimensions["MIN_X"], self.dimensions["MAX_Y"])
        vertice3 = Point(self.dimensions["MAX_X"], self.dimensions["MAX_Y"])
        self.vertices = [vertice1, vertice2, vertice3]

    # getters
    @property
    def num_points(self):
        return self._num_points

    @property
    def r(self):
        return self._r

    @property
    def vertices(self):
        return self._vertices


class SierpinskiCarpet(Fractal):
    def __init__(self):
        # inherits from the Fractal class
        Fractal.__init__(self)

        # values for sierpinski Carpet
        self.num_points = 100000
        self.r = 0.66

        # calculates vertices
        vertice1 = Point(self.dimensions["MIN_X"], self.dimensions["MIN_Y"])
        vertice2 = Point(self.dimensions["MID_X"], self.dimensions["MIN_Y"])
        vertice3 = Point(self.dimensions["MAX_X"], self.dimensions["MIN_Y"])
        vertice4 = Point(self.dimensions["MIN_X"], self.dimensions["MID_Y"])
        vertice5 = Point(self.dimensions["MAX_X"], self.dimensions["MID_Y"])
        vertice6 = Point(self.dimensions["MIN_X"], self.dimensions["MAX_Y"])
        vertice7 = Point(self.dimensions["MID_X"], self.dimensions["MAX_Y"])
        vertice8 = Point(self.dimensions["MAX_X"], self.dimensions["MAX_Y"])
        self.vertices = [vertice1, vertice2, vertice3, vertice4, vertice5, vertice6, vertice7, vertice8]

    # getters
    @property
    def num_points(self):
      return self._num_points

    @property
    def r(self):
      return self._r

    @property
    def vertices(self):
      return self._vertices


class Hexagon(Fractal):
    def __init__(self):
        # inherits from the Fractal class
        Fractal.__init__(self)

        # values for Hexagon fractal
        self.num_points = 50000
        self.r = 0.665

        # calculates vertices
        vertice1 = Point(self.dimensions["MID_X"], self.dimensions["MIN_Y"])
        vertice2 = Point(self.dimensions["MIN_X"], self.frac_y(0.25))
        vertice3 = Point(self.dimensions["MAX_X"], self.frac_y(0.25))
        vertice4 = Point(self.dimensions["MIN_X"], self.frac_y(0.75))
        vertice5 = Point(self.dimensions["MAX_X"], self.frac_y(0.75))
        vertice6 = Point(self.dimensions["MID_X"], self.dimensions["MAX_Y"])
        self.vertices = [vertice1, vertice2, vertice3, vertice4, vertice5, vertice6]

    # getters
    @property
    def num_points(self):
      return self._num_points

    @property
    def r(self):
      return self._r

    @property
    def vertices(self):
      return self._vertices

