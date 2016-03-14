"""
    Quick Sort for lists
    Hector Ramos
    1/21/2015
"""
from random import shuffle, randint

def quickSort(array, startIndex = None, endIndex = None):
    if not (startIndex and endIndex):
        startIndex = 0
        endIndex = len(array) - 1
    elif startIndex >= endIndex:
        return None

    pivotValue = array[randint(startIndex, endIndex)]
    leftIndex = startIndex
    rightIndex = endIndex

    while True:
        while leftIndex <= rightIndex and array[leftIndex] <= pivotValue:
            leftIndex += 1
        while rightIndex >= leftIndex and array[rightIndex] >= pivotValue:
            rightIndex -= 1

        if rightIndex < leftIndex:
            break
        else:
            array[leftIndex], array[rightIndex] = array[rightIndex], array[leftIndex]
            leftIndex += 1
            rightIndex -= 1

    #Left Partition
    quickSort(array, startIndex, leftIndex)
    #Right Partition
    quickSort(array, rightIndex, endIndex)

array = range(1,10)

shuffle(array)
print array
quickSort(array)
print array