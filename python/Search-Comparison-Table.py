##########################################################################################
# Name: Norman Cook
# Date: 7/02/2019
# Description: Generates a table that compares the performance of sequential
#   search and binary search.
##########################################################################################
import math

# a function that displays the table
def display_table(listsize):
    print("n\tSeq\tBin\tPerf")
    print("-------------------------------")
    while (listsize <= maximum):
        Seq = sequential_average(listsize)
        Bin = binary_maximum(listsize)
        if Bin == 0:
            Perf = 0
        else:
            Perf = Seq / float(Bin)
            Perf = round(Perf)
            Perf = int(Perf)
        print("{}\t{}\t{}\t{}".format(str(listsize), str(Seq), str(Bin), str(Perf)))
        listsize += interval

# a function that calculates the average number of comparisons of a sequential search on a list of size n
# -input: the list size
# -output: the average number of comparisons
def sequential_average(listsize):
    seqavg = listsize / 2
    return seqavg

# a function that calculates the maximum number of comparisons of a binary search on a list of size n
# -input: the list size
# -output: the average number of comparisons
def binary_maximum(listsize):
    binmax = math.log((listsize + 1), 2)
    binmax = math.ceil(binmax)
    binmax = int(binmax)
    return binmax

###############################################
# MAIN PART OF THE PROGRAM
###############################################
# get user input for the minimum (make sure that it is >= 0)
while True:
    minimum = input("Minimum number of list items (>=0)? ")
    if (minimum >= 0):
        break
    print "*ERROR: Minimum must be >= 0!"
    
# get user input for the maximum (make sure that is is >= minimum)
while True:
    maximum = input("Maximum number of list items (>= min ({}))? ".format(minimum))
    if (maximum >= minimum):
        break
    print "*ERROR: Maximum must be >= minimum ({})!".format(minimum)
    
# get user input for the interval (make sure that it is >= 1)
while True:
    interval = input("The interval between each row of the table (>= 1)? ")
    if (interval >= 1):
        break
    print "*ERROR: Interval must be >= 1!"
    
# generate the table
display_table(minimum)
