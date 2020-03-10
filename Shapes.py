######################################################################################################################
# Name: Norman Cook
# Date: 10/11/2019
# Description: Displays four different shapes using astericks 
#   based on height and width of the shape.
######################################################################################################################
# shape superclass for all shapes
class Shape(object):
  def __init__(self, width = 1, height = 1):
    self.width = width
    self.height = height

  def __str__(self):
    s = ""
    for i in range(self.height):
      s += "* " * self. width + "\n"
    return s

  # accessors and mutators
  @property
  def width(self):
    return self._width

  @width.setter
  def width(self, value):
    if (value == 0):
      value = 1
    if (value < 0):
      return
    self._width = value

  @property
  def height(self):
    return self._height

  @height.setter
  def height(self, value):
    if (value == 0):
      value = 1
    if (value < 0):
      return
    self._height = value

# defines a rectangle
class Rectangle(Shape):
  def __init__(self, width, height):
    Shape.__init__(self, width, height)

# defines a square
class Square(Shape):
  def __init__(self, width):
    height = width
    Shape.__init__(self, width, height)

# defines a triangle
class Triangle(Shape):
  def __init__(self, height):
    width = 1
    Shape.__init__(self, width, height)

  def __str__(self):
    s = ""
    for i in range(self.height, 0, -1):
      s += "* " * i + "\n"
    return s

# defines a parallelogram
class Parallelogram(Shape):
  def __init__(self, width, height):
    Shape.__init__(self, width, height)

  def __str__(self):
    s = ""
    for i in range(self.height, 0, -1):
      s += "  " * (i - 1) + "* " * self.width + "\n"
    return s

##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# create and display several shapes
r1 = Rectangle(12, 4)
print r1
s1 = Square(6)
print s1
t1 = Triangle(7)
print t1
p1 = Parallelogram(10, 3)
print p1
r2 = Rectangle(0, 0)
print r2
p1.width = 2
p1.width = -1
p1.height = 2
print p1

