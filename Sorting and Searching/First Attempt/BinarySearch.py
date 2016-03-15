"""
    Binary Search for lists
    Hector Ramos
    3/15/2015
"""
from random import randint

def binarySearch(array, value):
    lowerBound = 0
    upperBound = len(array) - 1

    while lowerBound <= upperBound:
        mid = (lowerBound + upperBound) / 2

        if array[mid] == value:
            return mid
        elif array[mid] > value:
            upperBound = mid - 1
        elif array[mid] < value:
            lowerBound = mid + 1

    return None

def binarySearchRecursive(array, value, lowerBound = None, upperBound = None):
    if not lowerBound and not upperBound:
        lowerBound = 0
        upperBound = len(array) - 1
    if lowerBound > upperBound:
        print lowerBound, upperBound
        return None

    mid = (lowerBound + upperBound) / 2

    if array[mid] == value:
        return mid
    elif array[mid] > value:
        return binarySearchRecursive(array, value, lowerBound, mid - 1)
    elif array[mid] < value:
        return binarySearchRecursive(array, value, mid + 1, upperBound)


array = range(1,101)

#Randomize Array
for x in xrange(50):
    array.pop(randint(0, len(array) - 1))

print array

value = randint(1,100)
output = binarySearch(array, value)
output2 = binarySearchRecursive(array, value)
print "Binary search for %d returned index %s." %(value, str(output))
print "Recusive Binary search for %d returned index %s." %(value, str(output2))
