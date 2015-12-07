"""
  There are three types of edits that can be performed on strings:
  Insert a character, Remove a character, and replace a character.
  Given two strings, write a function to check if they are one(or zero) edits away.
"""

def oneAway(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    elif s1 == s2:
        return True
    elif abs(len(s1) - len(s2)) == 1:
        diffLengths = True
        if len(s1) < len(s2):
            (s1, s2) = (s2, s1)
    else: 
        diffLengths = False

    index1 = 0; index2 = 0
    errorCheck = False

    while index1 < len(s1) and index2 < len(s2):
        if s1[index1] != s2[index2]:
            if errorCheck:
                return False
            errorCheck = True

            if diffLengths:
                index1 += 1
            else:
                index1 += 1
                index2 += 1
        else:
            index1 += 1
            index2 += 1

    return True

print oneAway("aba", "ac")
print oneAway("Yes", "Yas")
print oneAway("Noo", "oo")