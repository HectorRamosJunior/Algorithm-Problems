"""
  There are three types of edits that can be performed on strings:
  Insert a character, Remove a character, and replace a character.
  Given two strings, write a function to check if they are one(or zero) edits away.
"""

#Compares if the strings are one 'modification' away
def oneAway(s1, s2):
    if abs(len(s1) - len(s2)) > 1:  #Must be at most 1 apart
        return False
    elif s1 == s2:                  #If they're the same ignore
        return True
    elif abs(len(s1) - len(s2)) == 1:   
        diffLengths = True 
        if len(s1) < len(s2):
            (s1, s2) = (s2, s1)     #Code assumes s1 is longer
    else: 
        diffLengths = False

    index1 = 0; index2 = 0
    errorCheck = False              

    while index1 < len(s1) and index2 < len(s2):
        if s1[index1] != s2[index2]:
            if errorCheck:
                return False        #Only one discrepancy allowed
            errorCheck = True

            #If different lengths, the shorter string's character
            #Must match the next character of the longer string.
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