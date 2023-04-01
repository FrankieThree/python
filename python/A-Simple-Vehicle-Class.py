######################################################################################################################
# Name: Norman Cook
# Date: 08/05/2019
# Description: Implements a vehicle class with several other classes that 
#   inherit from the vehicle class. This includes a truck class, car 
#   class, dodge ram class, and honda civic class.
######################################################################################################################

# the vehicle class
# a vehicle has a year, make, and model
# a vehicle is instantiated with a make and model
class Vehicle(object):
  
  def __init__(self, make, model):
    self.make = make
    self.model = model
    self.year = 2000

  @property
  def year(self):
    return self._year

  @year.setter
  def year(self, value):
    self._year = 2000
    if (value <= 2018 and value >= 2000):
      self._year = value

  @property
  def make(self):
    return self._make

  @make.setter
  def make(self, value):
    self._make = value

  @property
  def model(self):
    return self._model

  @model.setter
  def model(self, value):
    self._model = value

# the truck class
# a truck is a vehicle
# a truck is instantiated with a make and model
class Truck(Vehicle):
  
  def __init__(self, make=None, model=None):
    self.make = make
    self.model = model

# the car class
# a car is a vehicle
# a car is instantiated with a make and model
class Car(Vehicle):
  
  def __init__(self, make=None, model=None):
    self.make = make
    self.model = model

# the Dodge Ram class
# a Dodge Ram is a truck
# a Dodge Ram is instantiated with a year
# all Dodge Rams have the same make and model
class DodgeRam(Truck):
  make = "Dodge"
  model = "Ram"
  
  def __init__(self, year = 2000):
    self.year = year

  def __str__(self):
    return "{} {} {}".format(self.year, self.make, self.model)
  
# the Honda Civic class
# a Honda Civic is a car
# a Honda Civic is instantiated with a year
# all Honda Civics have the same make and model
class HondaCivic(Car):
  make = "Honda"
  model = "Civic"
  
  def __init__(self, year = 2000):
    self.year = year

  def __str__(self):
    return "{} {} {}".format(self.year, self.make, self.model)
    
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the main part of the program
ram = DodgeRam(2016)
print ram

civic1 = HondaCivic(2007)
print civic1

civic2 = HondaCivic(1999)
print civic2
