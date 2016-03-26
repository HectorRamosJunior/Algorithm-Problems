"""
  There are three types of edits that can be performed on strings:
  Insert a character, Remove a character, and replace a character.
  Given two strings, write a function to check if they are one(or zero) edits away.
"""


def checkOneAway(s1,s2):
  #String's lengths can't differ by more than one
  if abs(len(s1) - len(s2) > 1): 
    return False

  #s1 is assumed to be the shorter string in the loop below
  if (len(s1) > len(s2)):
    s1, s2 = s2, s1

  index1 = 0
  index2 = 0
  difference = False #Clever way of checking if there is more than 1 discrepancy

  while(index1 < len(s1) and index2 < len(s2)):
    if(s1[index1] != s2[index2]):
      if difference: #2 discrepancies is the threshold
        return False

      difference = True

      #Push index on shorter string if lengths are both the same on a discrepancy
      if(len(s1) == len(s2)):
        index1 += 1

    else:
      index1 += 1 #If no error, push counter on the shorter string

    index2 += 1 #Always iterate through the longer string

  return True

print checkOneAway("abcd", "abcd")
print checkOneAway("abcd", "abc")
print checkOneAway("abcd", "abcde")
print checkOneAway("abcd", "abb")
print checkOneAway("abcd", "abc ")
print checkOneAway("abcd", "abc  ")
