"""
	Given a sorted array of n integers that have been rotated an unknown
	number of times, write code to find an element in the array. You may
	assume that the array was originally sorted in increasing order.
"""
from random import randint

# Quick function to rotate an array n spaces to the right
def rotate(array, n):
	return array[n:] + array[:n]

def searchRotated(array, value):
	if value == array[0]:
		return 0
	# Searches the array from the front in the larger value part of the 
	# rotation if value is larger than the first element
	elif value > array[0]:
		for i in xrange(len(array)):
			if value == array[i]:
				return i
			# If the current index is smaller than the first element,
			# The rotated array doesn't have the value in it 
			if array[i] < array[0]:
				return None
	# Searches the array from the back in the lower value part of the 
	# rotation if value is smaller than the first element
	elif value < array[0]:
		for i in xrange(len(array)):
			if value == array[-1 - i]:
				return len(array) - 1 - i
			# If the current index is larger than the first element,
			# The rotated array doesn't have the value in it 
			elif array[-1 - i] > array[0]:
				return None



arrayLength = 20
array = rotate(range(arrayLength), randint(0, arrayLength))

# Randomize array by removing 10 random elements
for x in xrange(arrayLength / 2):
	array.pop(randint(0, len(array) - 1))

print "Array: ", array

value = randint(0,9)

print "The index for value %d is: " % value
print searchRotated(array, value)