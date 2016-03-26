"""
  Assume you have a method isSubstring  which checks if one word is a subtring of another.
  Given two strings, s1 and s2, write code to checck if s2 is a rotation of s1 using only
  one call to isSubstring. (Example: Waterbottle is a rotation of erbottleWat.)
"""

#IF a string is "xy", "yx" would be the rotation
#"yxyx" has "xy" as a substring, so the string added by itself
#Gives you the original string at some point if it is only rotated.
def checkIfRotation(s1,s2):
  if len(s1) == len(s2):
    s1 += s1 #Add the base string twice to get all possible rotations
    return isSubstring(s1, s2) #Given Function

  return False