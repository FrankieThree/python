####################################################################################
# Name: Norman Cook
# Date: 7/18/2019
# Description: Calculates the number of zeros when counting to a user defined number.
#   The time elapsed during calculation is also shown.
####################################################################################
from time import time

# establish variables
totalZeros = 0;
count = 1;

# calculates the bumber of zeros in a single number
def zeros_in_number(n):
  zeros = 0
  while n > 0:
    if (n % 10 == 0):
      zeros += 1
    n = n / 10
  return zeros
  
########
# MAIN #
########

# ask the user what number to count towards
number = input("What number do you want to count zeros to? ")

# start the timer
start_time = time()

# calculate the zeros when counting from 1
while (count <= number):
  totalZeros += zeros_in_number(count)
  count += 1

# end the timer
end_time = time()

# return how many zeros have been counted
print("The number of zeros written from 1 to {} is {}.".format(number, totalZeros))

# return the time this calculation elapsed
elapsed = end_time - start_time
print("This took {} seconds.".format(elapsed))
