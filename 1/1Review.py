"""
  Implement an algorithm to determine if a string has all unique characters.
  What if you cannot use additional data structures?
"""

def isUnique(string):
    uniqueSet = set()

    for c in string:
        if c in uniqueSet:
            return False
        uniqueSet.add(c)

    return True


def isUnique2(string):
    for i in xrange(len(string)):
        for j in xrange(len(string)):
            if i == j:
                continue
            elif string[i] == string[j]:
                return False 

    return True

string = "asdfa"
print isUnique(string)
print isUnique2(string)

string = "asdf"
print isUnique(string)
print isUnique2(string)
