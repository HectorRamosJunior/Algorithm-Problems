"""
  Given a string, write a function to check f it is a permutation of a palindrome.
  A palindrome is a word or phrase that is the same forwards and backwards.
  The palindrome does not have to be limited to dictionary words.
"""

#Dictionary version for use of its hash table implementation again.
#Checks the character count dictionary for even counts of all characters
#Except if odd string length, one outlier allowed
def checkPermofPalindrome(string):
  if len(string) < 2:
    return False
  elif len(string) == 2: #All 2 character strings are palindromes
    return True
  else:
    dictionary = getCharacterCount(string)

    if len(string) % 2 == 0:  #Even String Length, no outliers
      oddCount = 1
    else:                     #Odd String length, one outlier allowed
      oddCount = 0

    #For each element in the dictionary, check if the character count is even
    #If it is odd, check if the threshold is met.
    for c in dictionary:
      if dictionary[c] % 2 != 0:
        if oddCount > 1:
          return False
        else:
          oddCount += 1

    return True


#Returns dictionary of character counts for each character present in string
def getCharacterCount(string):
  dictionary = {}

  for c in string:
    if not c in dictionary:
      dictionary[c] = 1
    else:
      dictionary[c] += 1

  return dictionary

print checkPermofPalindrome("racecar")
print checkPermofPalindrome("cdefg")
print checkPermofPalindrome("aabbc")
print checkPermofPalindrome("abcd")
print checkPermofPalindrome("baab")
print checkPermofPalindrome("")
print checkPermofPalindrome("abc")
print checkPermofPalindrome("abb")
print checkPermofPalindrome("aa")
print checkPermofPalindrome("ab")