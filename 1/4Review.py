"""
  Given a string, write a function to check f it is a permutation of a palindrome.
  A palindrome is a word or phrase that is the same forwards and backwards.
  The palindrome does not have to be limited to dictionary words.
"""

#Gets a character dictionary of the string
#If string is even, every character count must be even
#Otherwise, one odd character count is allowed.
def permofPal(string):
    if len(string) < 2:
        return False

    charDict = getCharDict(string)

    #Sets placeholder if one odd is allowed
    if len(string)%2 == 0:
        oddCheck = False
    else:
        oddCheck = True

    #Checks dictionary for even counts of characters
    for c in charDict:
        if charDict[c] % 2 != 0:
            if not oddCheck:
                return False
            else:
                oddCheck = False

    return True

def getCharDict(string):
    d = {}

    for c in string:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1

    return d

s = "aaba ab"
print s, permofPal(s)