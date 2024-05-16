######################################################################
# Name: Norman Cook
# Date: 11/04/2019
# Description: Plots points on a canvas that follow the chaos game
#   method for creating a Sierpinski Triangle, Sierpinski Carpet, and
#   Hexagon fractal.
######################################################################
from Tkinter import *
from random import randint
import importlib

# import the fractal module
moduleName = 'fractalmodule'
importlib.import_module(moduleName)
from fractalmodule import *

# the coordinate system class: (0,0) is in the top-left corner
# inherits from the Canvas class of Tkinter
class ChaosGame(Canvas):
    # the constructor
    def __init__(self, window):
        Canvas.__init__(self, window, bg="white")
        self.pack(fill=BOTH, expand=1)

        # radius and color of midpoints and vertices
        self.point_radius = 0
        self.point_color = "black"
        self.vertex_radius = 2
        self.vertex_color = "red"

    # plots the fractal
    def make(self, f):
        # plot the Sierpinski Triangle fractal
        if (f == "SierpinskiTriangle"):
            t = SierpinskiTriangle()

            # plot the vertices
            for i in range(len(t.vertices)):
                point = t.vertices[i]
                color = self.vertex_color
                radius = self.vertex_radius
                self.plot_point(point, color, radius)

            # plot the first intermediate point from two vertices
            point = t.vertices[0].interpt(t.vertices[1], t.r)
            color = self.point_color
            radius = self.point_radius
            self.plot_point(point, color, radius)

            # plot the intermediate points
            for i in range(t.num_points - 1):
                random = randint(0, len(t.vertices) - 1)
                point = point.interpt(t.vertices[random], t.r)
                color = self.point_color
                radius = self.point_radius
                self.plot_point(point, color, radius)

        # plot the Sierpinski Carpet Fractal
        if (f == "SierpinskiCarpet"):
            c = SierpinskiCarpet()

            # plot the vertices
            for i in range(len(c.vertices)):
                point = c.vertices[i]
                color = self.vertex_color
                radius = self.vertex_radius
                self.plot_point(point, color, radius)

            # plot the first intermediate point from two vertices
            point = c.vertices[0].interpt(c.vertices[1], c.r)
            color = self.point_color
            radius = self.point_radius
            self.plot_point(point, color, radius)

            # plot the intermediate points
            for i in range(c.num_points - 1):
                random = randint(0, len(c.vertices) - 1)
                point = point.interpt(c.vertices[random], c.r)
                color = self.point_color
                radius = self.point_radius
                self.plot_point(point, color, radius)

        # plot the hexagon fractal
        if (f == "Hexagon"):
            h = Hexagon()

            # plot the vertices
            for i in range(len(h.vertices)):
                point = h.vertices[i]
                color = self.vertex_color
                radius = self.vertex_radius
                self.plot_point(point, color, radius)

            # plot the first intermediate point from two vertices
            point = h.vertices[0].interpt(h.vertices[1], h.r)
            color = self.point_color
            radius = self.point_radius
            self.plot_point(point, color, radius)

            # plot the intermediate points
            for i in range(h.num_points - 1):
                random = randint(0, len(h.vertices) - 1)
                point = point.interpt(h.vertices[random], h.r)
                color = self.point_color
                radius = self.point_radius
                self.plot_point(point, color, radius)

    # plots the points
    def plot_point(self, point, color, radius):
        self.create_oval(point.x, point.y, point.x + \
                         radius, \
                         point.y + radius, \
                         outline=color, \
                         fill=color)


################
# MAIN PROGRAM #
################

# the default size of the canvas is 600x520
WIDTH = 600
HEIGHT = 520

# constants for the canvas coordinates
MIN_X = 5
MAX_X = 585
MIN_Y = 5
MAX_Y = 505
MID_X = (MIN_X + MAX_X) / 2
MID_Y = (MIN_Y + MAX_Y) / 2

# the implemented fracals
FRACTALS = ["SierpinskiTriangle", "SierpinskiCarpet", "Hexagon"]

# create the fractals in indivdual windows
for f in FRACTALS:
    window = Tk()
    window.geometry("{}x{}".format(WIDTH, HEIGHT))
    window.title("2D Points...Plotted")
    # create the coordinate system as a Tkinter canvas inside the window
    c = ChaosGame(window)
    # make the current fractal
    c.make(f)
    # wait for the window to close
    window.mainloop()
