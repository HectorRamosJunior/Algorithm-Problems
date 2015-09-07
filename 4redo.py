def checkPermofPalindrome(string):
  if len(string) < 2:
    return False
  elif len(string) == 2:
    return True
  else:
    dictionary = getCharacterCount(string)

    if len(string) % 2 == 0:
      oddCount = 1
    else:
      oddCount = 0

    for c in dictionary:
      if dictionary[c] % 2 != 0:
        if oddCount > 1:
          return False
        else:
          oddCount += 1

    return True



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