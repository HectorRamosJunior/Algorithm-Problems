"""
    Selection Sort for lists
    Hector Ramos
    12/20/2015
"""
from random import shuffle

def selectionSort(array):
    length = len(array)

    for i in xrange(length):
        localMin = None
        minIndex = None

        for j in xrange(i, length):
            if not localMin or array[j] < localMin:
                localMin = array[j]
                minIndex = j

        array[i], array[minIndex] = array[minIndex], array[i]

array = range(1,101)

shuffle(array)
print array
selectionSort(array)
print array