"""
    You are given two sorted arrays A and B, where A has enough buffer at 
    the end to hold B. Write a method to merge B into A in sorted order.
"""
from random import randint

def mergeArrays(arrayA, arrayB):
	indexA = len(arrayA) - 1
	indexB = len(arrayB) - 1

	# Create buffer for arrayB in list arrayA
	for x in xrange(len(arrayB)):
		arrayA.append(0)

	# Merging the arrays backward, currentIndex is the last element
	currentIndex = len(arrayA) - 1

	while currentIndex >= 0:
		# If both the arrays haven't been fully iterated through
		if indexA >= 0 and indexB >= 0:
			if arrayA[indexA] >= arrayB[indexB]:
				arrayA[currentIndex] = arrayA[indexA]
				currentIndex -= 1
				indexA -= 1
			elif arrayA[indexA] < arrayB[indexB]:
				arrayA[currentIndex] = arrayB[indexB]
				currentIndex -= 1
				indexB -= 1
		# If array B was fully iterated through
		elif indexA >= 0:
			arrayA[currentIndex] = arrayA[indexA]
			currentIndex -= 1
			indexA -= 1
		# If array A was fully iterated through
		elif indexB >= 0:
			arrayA[currentIndex] = arrayB[indexB]
			currentIndex -= 1
			indexB -= 1

	return arrayA

arrayA = range(20)
arrayB = range(20)

# Randomize arrays while keeping them sorted
for x in xrange(15):
	arrayA.pop(randint(0, len(arrayA) - 1))
	arrayB.pop(randint(0, len(arrayB) - 1))

print "ArrayA: ", arrayA
print "ArrayB: ", arrayB

print "\nMerged arrays: \n", mergeArrays(arrayA, arrayB)

