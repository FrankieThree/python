######################################################################################################################
# Name: Norman Cook
# Date: 9/20/2019
# Description: Plots a specified number of points at random positions filled with
#               a random color from a list.
######################################################################################################################
from Tkinter import *
from random import randint

# the 2D point class
class Point(object):
  def __init__(self, x=0.0, y=0.0):
    self.x = x
    self.y = y

  def __str__(self):
    return "({}, {})".format(self.x, self.y)

  @property
  def x(self):
    return self._x

  @x.setter
  def x(self, value):
    self._x = float(value)

  @property
  def y(self):
    return self._y

  @y.setter
  def y(self, value):
    self._y = float(value)

  # calculate the distance using two points  
  def dist(self, p2):
    distance = math.sqrt((p2.x - self.x)**2 + (p2.y - self.y)**2)
    return distance

  # calculate the midpoint between two points
  def midpt(self, p2):
    midx = (p2.x + self.x)/2
    midy = (p2.y + self.y)/2
    pnew = Point(midx, midy)
    return pnew

# the coordinate system class: (0,0) is in the top-left corner
# inherits from the Canvas class of Tkinter
class CoordinateSystem(Canvas):
  def __init__(self, master):
    Canvas.__init__(self, master, bg="white")
    self.pack(fill=BOTH, expand=1)

  # plots the number of points specified at random positions
  def plotPoints(self, numPoints):
    for num in range(numPoints):
      point = Point(randint(0, WIDTH), randint(0, HEIGHT))
      self.plot(point)

  # plots a point with a random color
  def plot(self, point):
    POINT_COLORS = [ "BLACK", "RED", "GREEN", "BLUE", "CYAN", "YELLOW", "MAGENTA" ]
    POINT_RADIUS = 0
    color = POINT_COLORS[randint(1, len(POINT_COLORS) - 1)]
    self.create_oval(point.x, point.y, point.x + POINT_RADIUS, point.y + POINT_RADIUS, outline=color, fill=color)
  
##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the default size of the canvas is 800x800
WIDTH = 800
HEIGHT = 800
# the number of points to plot
NUM_POINTS = 5000

# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("2D Points...Plotted")
# create the coordinate system as a Tkinter canvas inside the window
s = CoordinateSystem(window)
# plot some random points
s.plotPoints(NUM_POINTS)
# wait for the window to close
window.mainloop()
