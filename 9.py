def checkIfRotation(s1,s2):
  if len(s1) == len(s2):
    s1 += s1
    return isSubstring(s1, s2) #Given Function

  return False