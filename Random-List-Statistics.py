###########################################################################################
# Name: Norman Cook
# Date: 7/12/2019
# Description: Generate a random list within constraints and calculate the 
#   mean, median, and range of the list.
###########################################################################################
import random

# function that prompts the user for a list size, minimum and maximum values, creates the list, and returns it
# you must use the list functions discussed in class to add integers to the list
def fillList():
    length = input("How many random integers would you like to add to the list? ")
    minimum = input("What would you like the minimum value to be? ")
    maximum = input("What would you like the maximum value to be? ")
    count = 0
    newlist = []
    
    while (count < length):
        newlist.append(random.randrange(minimum, maximum + 1))
        count += 1
    return newlist

# function that receives the list as a parameter, and calculates and returns the mean
def mean(thelist):
    sum = 0
    for index in range(0, len(thelist)):
        sum += thelist[index]
    avg = float(sum) / len(thelist)
    return avg

# function that receives the list as a parameter, and calculates and returns the median
def median(thelist):
    for count in range(len(thelist) - 1, -1, -1):
        for index in range(0, count):
            value = thelist[index]
            if (value > thelist[index + 1]):
                placeholder = thelist[index + 1]
                thelist[index + 1] = thelist[index]
                thelist[index] = placeholder

    
    listdivide = len(thelist) / 2
    if (len(thelist) % 2 != 0):
        middle = thelist[listdivide]
    else:
        indexlower = thelist[listdivide - 1]
        indexhigher = thelist[listdivide]
        middle = (indexlower + indexhigher) / float(2)
    return middle

# function that receives the list as a parameter, and calculates and returns the range
def therange(thelist):
    maximum = minimum = thelist[0]
    
    for num in thelist:
        if (maximum < num):
            maximum = num
        if (minimum > num):
            minimum = num

    rangeoflist = maximum - minimum
    return rangeoflist


###############################################
# MAIN PART OF THE PROGRAM
# implement the main part of your program below
# comments have been added to assist you
###############################################
# create the list
nums = fillList()

# display the list
# there is no need to write/call your own function for this part
print ("The list: {}".format(nums))

# calculate and display the mean
print ("The mean of the list is {}.".format(mean(nums)))

# calculate and display the median
print ("The median of the list is {}.".format(median(nums)))

# calculate and display the range
print ("The range of the list is {}.".format(therange(nums)))
