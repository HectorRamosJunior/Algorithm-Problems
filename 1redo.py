def allUnique(string):
    if len(string) > 128:
      return False
    else:
      dictionary = {}

      for i in range(len(string)):
        if string[i] in dictionary:
          return False
        else:
          dictionary[string[i]] = True

      return True



print allUnique("Test")
print allUnique("TesT")
print allUnique("1231231231")
print allUnique("abcdefghijklmnopqrstuvwxyzA1234567890")