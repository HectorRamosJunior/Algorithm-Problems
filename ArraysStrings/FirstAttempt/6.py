"""
  Implement a method to perform basic string compression using the counts of repeated characters.
  For example, the string "aabcccccaaa" would become "a2b1c5a3". If the "compressed" string would not
  become smaller than the original string, your method should return the original string. 
  You can assume the string only has Upper and Lowercase letters (a-z).
"""


def getStrCompressed(s):
  if len(s) < 2:
    return "String too short! Insert at least 2 characters!"

  newString = ''
  counter = 1

  for i in range(len(s)):

    #If on the last character, check the previous character
    if i == len(s) - 1:
      if s[i] == s[i-1]:
        counter += 1
        newString += s[i] + str(counter)
      else:
        newString += s[i] + "1"

    elif s[i] == s[i+1]:
      counter += 1

    #If the current character and future character differ,
    #Print out current character with the count of it so far
    else: 
      newString += s[i] + str(counter)
      counter = 1


  #prints out the shorter string
  if len(s) <= len(newString):
    return s
  else:
    return newString


print getStrCompressed("abc")
print getStrCompressed("aaabbcccc")
print getStrCompressed("aaabbbc")
print getStrCompressed("")