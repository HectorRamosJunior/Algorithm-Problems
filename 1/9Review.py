"""
  Assume you have a method isSubstring  which checks if one word is a 
  subtring of another. Given two strings, s1 and s2, write code to 
  checck if s2 is a rotation of s1 using only one call to isSubstring. 
  (Example: Waterbottle is a rotation of erbottleWat.)
"""

def checkRotation(s1, s2):
    s3 = s2 + s2    #the middle will form the proper word again
                    #erbottleWaterbottleWat as shown.

    return (s1 in s3) #Basically isSubstring (<3 Python)


print checkRotation("Waterbottle", "erbottleWat")
print checkRotation("Nope", "Yerp")






