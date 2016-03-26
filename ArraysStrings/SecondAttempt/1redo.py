"""
  Implement an algorithm to determine if a string has all unique characters.
  What if you cannot use additional data structures?
"""


#Dictionary(Hash Table) implementation.
#Characters are added to the dictionary if they are unique, if not, return False.
def allUnique(string):
    if len(string) > 128: #Can't be longer than standard ASCII characters allowed
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