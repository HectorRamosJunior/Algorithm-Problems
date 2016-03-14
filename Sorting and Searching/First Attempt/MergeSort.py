"""
    Merge Sort for lists
    Hector Ramos
    12/20/2015
"""
from random import shuffle

def mergeSort(array):
    if len(array) <= 1:
        return array

    mid = len(array)/2

    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])

    return merge(left, right)

def merge(left, right):
    leftIndex = 0
    rightIndex = 0

    leftLen = len(left)
    rightLen = len(right)

    newArray = []

    while leftIndex < leftLen or rightIndex < rightLen:
        if leftIndex < leftLen and rightIndex < rightLen:
            if left[leftIndex] <= right[rightIndex]:
                newArray.append(left[leftIndex])
                leftIndex += 1
            elif right[rightIndex] < left[leftIndex]:
                newArray.append(right[rightIndex])
                rightIndex += 1
        elif leftIndex >= leftLen:
            newArray.append(right[rightIndex])
            rightIndex += 1
        elif rightIndex >= rightLen:
            newArray.append(left[leftIndex])
            leftIndex += 1

    return newArray


array = range(1,101)

shuffle(array)
print array
print mergeSort(array)



