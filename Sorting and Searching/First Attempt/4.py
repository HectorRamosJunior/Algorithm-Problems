"""
    You are given an array-like data structure Listy which lacks a size
    method. It does, however, have an elementAt(i) method that returns the
    element at index i in O(1)time. If i is beyond the bounds of the data
    structure, it returns -1. (For this reason, the data structure only
    supports positive integers.) Given a Listy which contains sorted, 
    positive integers, find the index at which an element x occurs. 
    If x occurs multiple times, you may return any index.
"""
from random import randint

class Listy(object):
    def __init__(self, array):
        self.array = array

    def elementAt(self, index):
        if index >= len(self.array):
            return -1
        return self.array[index]

# Implements modified binary search to find the wanted index
def findElementIndex(listy, x):
    index = 1
    upperBound = None
    lowerBound = 0

    # Defines the upperbound for the binary search
    while not upperBound:
        value = listy.elementAt(index)
        # Handle if element found at this stage
        if value == x:
            return index 

        # End condition met, upper bound defined
        if value == -1 or value > x:
            upperBound = index
        index = index * 2

    index = (upperBound + lowerBound) / 2

    # Implements binary search on the listy to find the index
    while listy.elementAt(index) != x:
        # If bounds 1 away, element does not exist in listy
        if upperBound - lowerBound == 1:
            return None

        value = listy.elementAt(index)
        # Handle moving upperBound down
        if value > x or value == -1:
            upperBound = index
            index = (lowerBound + upperBound) / 2
        # Handle moving lowerBound up
        elif value < x:
            lowerBound = index
            index = (lowerBound + upperBound) / 2

    return index

array = range(1,101)

# Randomize the array
for x in xrange(50):
    array.pop(randint(0, len(array) - 1))
print "Listy's array: \n", array

listyObject = Listy(array)

value = randint(1,100)
index = findElementIndex(listyObject, value)

print "The index for element %d is : %s" %(value, str(index))

