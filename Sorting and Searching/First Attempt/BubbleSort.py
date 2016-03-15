"""
    Bubble Sort for lists
    Hector Ramos
    12/20/2015
"""
from random import shuffle

def bubbleSort(array):
    endIndex = len(array) - 1 

    while endIndex >= 0:
        for i in xrange(endIndex):  #Last index isn't iterated
            if array[i+1] < array[i]:
                array[i], array[i+1] = array[i+1], array[i]

        endIndex -= 1


array = range(1,101)

shuffle(array)
print array
bubbleSort(array)
print array
