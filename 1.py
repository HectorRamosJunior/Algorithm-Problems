def allUnique(string):
  uniqueChars = []
  for c in string:
    if uniqueChars.__len__() == 0:
      uniqueChars.append(c)
    else:
      if c in uniqueChars:
        return False
      else:
        uniqueChars.append(c)

  return True

allUnique("test")


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
