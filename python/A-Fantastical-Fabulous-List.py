###########################################################################################
# Name: Norman Cook
# Date: 7/07/2019
# Description: Generates a list of integers that are provided by the user. Returns the
#       original list, the length of this list, the minimum value, the maximum value, a
#       reversed version of the list, and a sorted version of the list.
###########################################################################################

# function that:
# (1) prompts the user for a list size
# (2) prompts the user for the integers to store in the list (corresponding to the list size)
# (3) creates the list
# (4) returns the list
def fillList():
    newList = []
    length = input("How many integers would you like to add to the list? ")
    while (len(newList) < length):
        newItem = input("Enter an integer: ")
        newList.append(newItem)
    return newList

###############################################
# MAIN PART OF THE PROGRAM
# implement the main part of your program below
# comments have been added to assist you
###############################################
# create the list
nums = fillList()

# display information about the list using the list functions discussed in class
# there is no need to write/call your own functions here
print("The original list: " + str(nums))
print("The length of the list is {}.".format(len(nums)))
print("The minimum value in the list is {}.".format(min(nums)))
print("The maximum value in the list is {}.".format(max(nums)))
nums.reverse()
print("The reversed list: " + str(nums))
nums.sort()
print("The sorted list: " + str(nums))
