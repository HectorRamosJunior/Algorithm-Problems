"""
  Implement an algorithm to determine if a string has all unique characters.
  What if you cannot use additional data structures?
"""

def allUnique(string):
  uniqueChars = []
  for c in string:
    if uniqueChars.__len__() == 0:
      uniqueChars.append(c)
    else:
      if c in uniqueChars:  #Checks if character already in uniqueChars
        return False
      else:
        uniqueChars.append(c)

  return True

allUnique("test")


#This function checks the character's nearby characters to see if they are the same.
#This requires sorting first.
def allUnique2(string):
  string = sorted(string)

  for c in range(0, string.__len__()):
    if c == 0:
      if string[c] == string[c+1]:
        return False
    elif c == string.__len__()-1:
      if string[c] == string[c-1]:
        return False
    else:
      if string[c] == string[c-1] or string[c] == string[c+1]:
        return False
  return True

allUnique2("Test")
