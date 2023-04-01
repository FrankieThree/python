############################################
# Name: Norman Cook
# Date: 06-19-2019
# Description: Collects the name and age of the user by calling functions in
#   main part of the program.
###########################################################################################

# function that prompts the user for a name and returns it
def name():
    name = input("Please enter your name: ")
    return name

# function that receives the user's name as a parameter, and prompts the user for an age and returns it
def age(name) :
    age = input("How old are, {}? ".format(name))
    return age

# function that receives the user's name and age as parameters and displays the final output
def output(name, age) :
    print "Hi, {}.  You are {} years old.  Twice your age is {}.".format(name, age, age * 2)


###############################################
# MAIN PART OF THE PROGRAM
# implement the main part of your program below
# comments have been added to assist you
###############################################

# get the user's name
name = name()

# get the user's age
age = age(name)

# display the final output
output(name, age)
