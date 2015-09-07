def getStrCompressed(s):
  if len(s) < 2:
    return "String too short! Insert at least 2 characters!"

  newString = ''
  counter = 1

  for i in range(0, len(s)):
    if i == len(s) - 1:
      if s[i] == s[i-1]:
        counter += 1
        newString += s[i] + str(counter)
      else:
        newString += s[i] + "1"

    elif s[i] == s[i+1]:
      counter += 1

    else: 
      newString += s[i] + str(counter)
      counter = 1



  if len(s) <= len(newString):
    return s
  else:
    return newString


print getStrCompressed("abc")
print getStrCompressed("aaabbcccc")
print getStrCompressed("aaabbbc")
print getStrCompressed("")