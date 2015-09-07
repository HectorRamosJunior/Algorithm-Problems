def checkOneAway(s1,s2):
  if abs(len(s1) - len(s2) > 1):
    return False

  if (len(s1) > len(s2)):
    s1, s2 = s2, s1

  index1 = 0
  index2 = 0
  difference = False

  while(index1 < len(s1) and index2 < len(s2)):
    if(s1[index1] != s2[index2]):
      if difference:
        return False

      difference = True

      if(len(s1) == len(s2)):
        index1 += 1

    else:
      index1 += 1

    index2 += 1

  return True

print checkOneAway("abcd", "abcd")
print checkOneAway("abcd", "abc")
print checkOneAway("abcd", "abcde")
print checkOneAway("abcd", "abb")
print checkOneAway("abcd", "abc ")
print checkOneAway("abcd", "abc  ")
