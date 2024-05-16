######################################################################################################################
# Name: Norman Cook
# Date: 7/31/2019
# Description: Creates a unique fraction class that handles the addition,
#   subtraction, multiplication, division, and reduction of fractions.
######################################################################################################################

# the fraction class
class Fraction(object):

  # initialize the fraction's numerator and denominator
  def __init__(self, num = 0, den = 1):
    self.num = num

    if (den == 0):
      den = 1
    self.den = den

    self.reduce()

  # method that adds two fractions together
  def __add__(self, other):
    num = (self.num * other.den) + (other.num * self.den)
    den = self.den * other.den
    sum = Fraction(num, den)
    sum.reduce()

    return sum

  # method that subtracts two fractions
  def __sub__(self, other):
    num = (self.num * other.den) - (other.num * self.den)
    den = self.den * other.den
    sum = Fraction(num, den)
    sum.reduce()
    
    return sum

  # method that multiplies two fractions
  def __mul__(self, other):
    num = self.num * other.num
    den = self.den * other.den
    sum = Fraction(num, den)
    sum.reduce()
    
    return sum

  # method that divides two fractions
  def __div__(self, other):
    num = self.num * other.den
    den = self.den * other.num
    sum = Fraction(num, den)
    sum.reduce()
    
    return sum

  # method that returns the denominator, numerator, and value of a fraction
  def __str__(self):
    return "{}/{} ({})".format(self.num, self.den, self.getReal())

  # method that reduces a fraction by its least common denominator
  def reduce(self):
    gcd = 1
    minimum = min(abs(self.num), abs(self.den))

    for i in range(2, minimum + 1):
      if (self.num % i == 0 and self.den % i == 0):
        gcd = i

    self.num /= gcd
    self.den /= gcd

    if (self.num == 0):
      self.den = 1

  # setters and getters
  @property
  def num(self):
    return self._num
  
  @num.setter
  def num(self, value):
    self._num = value
    
  @property
  def den(self):
    return self._den
  
  @den.setter
  def den(self, value):
    if (value != 0):
      self._den = value

  def getReal(self):
    return float(self.num) / self.den

# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the main part of the program
# create some fractions
f1 = Fraction()
f2 = Fraction(5, 8)
f3 = Fraction(3, 4)
f4 = Fraction(1, 0)

# display them
print "f1:", f1
print "f2:", f2
print "f3:", f3
print "f4:", f4

# play around
f3.num = 5
f3.den = 8
f1 = f2 + f3
f4.den = 88
f2 = f1 - f1
f3 = f1 * f1
f4 = f4 / f3

# display them again
print
print "f1:", f1
print "f2:", f2
print "f3:", f3
print "f4:", f4
