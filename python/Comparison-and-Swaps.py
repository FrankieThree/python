######################################################################################################################
# Name: Norman Cook
# Date: 7/21/2019
# Description: Plots the comparisons and swaps of four sorting algorithms
#   using the plot file. Algorithms include bubble sort, optimized bubble
#   sort, selection sort, and insertion sort. 
######################################################################################################################
from plot import *

# creates the list
def getList():
#	return [100, 5, 63, 29, 69, 74, 96, 80, 82, 12]
	return [82, 65, 93, 0, 60, 31, 99, 90, 31, 70]
#	return [63, 16, 78, 69, 36, 36, 3, 66, 75, 100]
#	return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#	return [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#	return [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]

# the bubble sort function
# input: a list of integers
# output: a number of comparisons and swaps
def bubbleSort(nums):
        comparisons = 0
        swaps = 0
        for end in range(len(nums), -1, -1):
                for index in range(0, end - 1):
                        if (nums[index] > nums[index + 1]):
                                holder = nums[index]
                                nums[index] = nums[index + 1]
                                nums[index + 1] = holder
                                swaps += 1
                        comparisons += 1
        return nums, comparisons, swaps

# the optimized bubble sort function
# input: a list of integers
# output: a number of comparisons and swaps
def optBubble(nums):
        comparisons = 0
        swaps = 0
        for end in range(len(nums), -1, -1):
                swapTracker = swaps
                for index in range(0, end - 1):
                        if (nums[index] > nums[index + 1]):
                                holder = nums[index]
                                nums[index] = nums[index + 1]
                                nums[index + 1] = holder
                                swaps += 1
                        comparisons += 1
                if (swapTracker == swaps):
                        break
        return nums, comparisons, swaps

# the selection sort function
# input: a list of integers
# output: a number of comparisons and swaps
def selectionSort(nums):
        comparisons = 0
        swaps = 0
        for index in range(len(nums) - 1):
                minimum = nums[index]
                minimumIndex = index
                for compIndex in range(index + 1, len(nums)):
                       if (minimum > nums[compIndex]):
                               minimum = nums[compIndex]
                               minimumIndex = compIndex
                       comparisons += 1
                holder = nums[index]
                nums[index] = minimum
                nums[minimumIndex] = holder
                swaps += 1
        return nums, comparisons, swaps
                        
# the insertion sort function
# input: a list of integers
# output: a number of comparisons and swaps
def insertionSort(nums):
        comparisons = 0
        swaps = 0
        for index in range(1, len(nums)):
                stored = nums[index]
                comparisons += 1
                for insertIndex in range(index, 0, -1):
                        comparisons += 1
                        if (stored >= nums[insertIndex - 1]):
                                updateIndex = insertIndex
                                break
                        elif (stored < nums[insertIndex - 1]):
                                swaps += 1
                                nums[insertIndex] = nums[insertIndex - 1]
                                updateIndex = insertIndex - 1
                nums[updateIndex] = stored
        return nums, comparisons, swaps

########
# MAIN #
########

# bubble sorting algorithm
sortedBubble, compsBubble, swapsBubble = bubbleSort(getList())
print "The list: {}".format(getList())
print "After bubble sort: {}".format(sortedBubble)
print "{} comparisons: {} swaps".format(compsBubble, swapsBubble)
print ""
bubble = [compsBubble, swapsBubble]

# optimized bubble sorting algorithm
sortedOptBubble, compsOptBubble, swapsOptBubble = optBubble(getList())
print "The list: {}".format(getList())
print "After optimized bubble sort: {}".format(sortedOptBubble)
print "{} comparisons: {} swaps".format(compsOptBubble, swapsOptBubble)
print ""
optimized = [compsOptBubble, swapsOptBubble]

# selection sorting algorithm
sortedSelection, compsSelection, swapsSelection = selectionSort(getList())
print "The list: {}".format(getList())
print "After selection sort: {}".format(sortedSelection)
print "{} comparisons: {} swaps".format(compsSelection, swapsSelection)
print ""
selection = [compsSelection, swapsSelection]

# insertion sorting algorithm
sortedInsertion, compsInsertion, swapsInsertion = insertionSort(getList())
print "The list: {}".format(getList())
print "After insertion sort: {}".format(sortedInsertion)
print "{} comparisons: {} swaps".format(compsInsertion, swapsInsertion)
insertion = [compsInsertion, swapsInsertion]

# plot each list using the plot python file
plot(bubble, optimized, selection, insertion)
