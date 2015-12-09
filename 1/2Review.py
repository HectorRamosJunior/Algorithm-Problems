"""
  Given two strings, write a method to decide if one is a 
  permutation of the other.
"""
#Makes two dictionaries of each string, checks character counts
def checkPermutation(s1, s2):
    if len(s1) != len(s2): #If seperate lengths, always false
        return False

    d1 = getCharDict(s1)
    d2 = getCharDict(s2)

    if d1 == d2:
        return True
    else:
        return False

#Returns dictionary of the characters in the string and count
def getCharDict(string):
    d = {}

    for c in string:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1

    return d


s1 = "asdfa"
s2 = "fdasa"
print checkPermutation(s1, s2)
print checkPermutation("No", "Yes")
print checkPermutation("No", "Nooo")