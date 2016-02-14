"""
    Insertion Sort for lists
    Hector Ramos
    12/20/2015
"""
from random import shuffle

def insertionSort(array):
    for i in xrange(len(array) - 1):
        if array[i+1] >= array[i]:
            continue

        index = i
        while index >= 0 and array[index + 1] <= array[index]:
            array[index+1], array[index] = array[index], array[index+1]

            index -= 1      

array = range(1,101)

shuffle(array)
print array
insertionSort(array)
print array