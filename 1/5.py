"""
  There are three types of edits that can be performed on strings:
  Insert a character, Remove a character, and replace a character.
  Given two strings, write a function to check if they are one(or zero) edits away.
"""

""" Unfortunately, Had to look at solutions. But was 
  Frustratingly close; got caught up on trying to iterate
  both at the same time properly with different lengths. """


#Unfinished code, look at 5redo.py
def checkOneAway(s1,s2):
  if abs(len(s1) - len(s2) > 1):
    return False
  else:
    if len(s1) < len(s2):
      s1 + " "
    elif len(s2) < len(s1):
      s2 + " "

    s1Pos = 0
    s2Pos = 0
    diffs = 0

    while(s1Pos < len(s1)):
      if (s1[s1Pos] != s2[s2Pos]):
        diffs += 1
        if (s2Pos < len(s2) - 2):
          if (s1[s1Pos] == s2[s2Pos +1 ]):
            s1Pos += 1

    


