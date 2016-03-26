"""
    Write a method to sort an array of strings so that all the anagrams
    are next to each other.
"""

def getCharDict(s):
    charDict = {}

    for c in s:
        if c not in charDict:
            charDict[c] = 1
        elif c in charDict:
            charDict[c] += 1

    return charDict

def sortAnagrams(array):
    if len(array) <= 1:
        return array

    mid = len(array)/2

    left = sortAnagrams(array[:mid])
    right = sortAnagrams(array[mid:])

    return merge(left, right)

def merge(left, right):
    if not left:
        return right
    if not right:
        return left

    newArray = [left.pop(0)]

    while left or right:
        while left and (getCharDict(left[0]) == getCharDict(newArray[-1])):
            newArray.append(left.pop(0))

        for x in xrange(len(right) - 1, -1, -1):
            if getCharDict(right[x]) == getCharDict(newArray[-1]):
                newArray.append(right.pop(x))

        if left and right:
            newArray.append(left.pop(0))
        elif right:
            for x in xrange(len(right)):
                newArray.append(right.pop(0))
        elif left:
            for x in xrange(len(left)):
                newArray.append(left.pop(0))

    return newArray

s = ["asdf", "a", "b", "test", "qwe", "fdsa", "c", "d", "ewq", "a"]

print "Before Anagram grouping: \n", s
print "After Anagram grouping: \n", sortAnagrams(s)