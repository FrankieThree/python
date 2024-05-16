###########################################################################################
# Name: Norman Cook
# Date: 06/23/2019
# Description: A program that calculates and returns the minimum value, maximum value, mean,
#   median, mode, and range of three integers.
###########################################################################################


# function that prompts the user to enter an integer and returns it
def integer():
    integer = input("Enter an integer: ")
    return integer


# function that receives three integers as parameters and returns the minimum of the three
def minimum(integer1, integer2, integer3):
    if (integer1 <= integer2 and integer1 <= integer3):
        return integer1
    elif (integer2 <= integer1 and integer2 <= integer3):
        return integer2
    else:
        return integer3


# function that receives three integers as parameters and returns the maximum of the three
def maximum(integer1, integer2, integer3):
    if (integer1 >= integer2 and integer1 >= integer3):
        return integer1
    elif (integer2 >= integer1 and integer2 >= integer3):
        return integer2
    else:
        return integer3  


# function that receives three integers as parameters, and calculates and returns the mean
def mean(integer1, integer2, integer3):
    mean = (integer1 + integer2 + integer3) / 3.0
    return mean


# function that receives three integers as parameters, and calculates and returns the median
def median(integer1, integer2, integer3):
    if (integer1 <= integer2 and integer1 >= integer3):
        return integer1
    elif (integer1 >= integer2 and integer1 <= integer3):
        return integer1
    
    if (integer2 <= integer1 and integer2 >= integer3):
        return integer2
    elif (integer2 >= integer1 and integer2 <= integer3):
        return integer2
    
    if (integer3 <= integer1 and integer3 >= integer2):
        return integer3
    elif (integer3 >= integer1 and integer3 <= integer2):
        return integer3


# function that receives three integers as parameters, and calculates and returns the mode
def mode(integer1, integer2, integer3):
    if (integer1 == integer2):
        return integer1
    elif (integer3 == integer2):
        return integer3
    elif (integer1 == integer3):
        return integer1
    else:
        return "undefined"


# function that receives three integers as parameters, and calculates and returns the range
def range0(integer1, integer2, integer3):
    if (integer1 <= integer2 and integer1 <= integer3):
        mi = integer1
    elif (integer2 <= integer1 and integer2 <= integer3):
        mi = integer2
    else:
        mi = integer3

    if (integer1 >= integer2 and integer1 >= integer3):
        ma = integer1
    elif (integer2 >= integer1 and integer2 >= integer3):
        ma = integer2
    else:
        ma = integer3  
    return ma - mi


###############################################
# MAIN PART OF THE PROGRAM
# implement the main part of your program below
# comments have been added to assist you
###############################################

# get three integers from the user
integer1 = integer()
integer2 = integer()
integer3 = integer()

# determine and display the minimum value
minimum = minimum(integer1, integer2, integer3)
print("The minimum value is {}.").format(minimum)

# determine and display the maximum value
maximum = maximum(integer1, integer2, integer3)
print("The maximum value is {}.").format(maximum)

# calculate and display the mean
mean = mean(integer1, integer2, integer3)
print("The mean is {}.").format(mean)

# calculate and display the median
median = median(integer1, integer2, integer3)
print("The median is {}.").format(median)

# calculate and display the mode
mode = mode(integer1, integer2, integer3)
print ("The mode is {}.").format(mode)

# calculate and display the range
range0 = range0(integer1, integer2, integer3)
print ("The range is {}").format(range0)
