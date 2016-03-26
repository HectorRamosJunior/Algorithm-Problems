"""
  Given two strings, write a method to decide if one is a permutation of the other.
"""

#Uses two dictionaries to store the character counts of each string
#Then compare dictionaries for discrepancies
def checkPermutation(string1,string2):
	if len(string1) != len(string2): #If the string's lengths are different, False
		return False
	else:
		dictionary1 = getCharacterCount(string1)
		dictionary2 = getCharacterCount(string2)

		for c in dictionary1:
			if (not c in dictionary2) or (dictionary1[c] != dictionary2[c]):
				return False

		return True



#Used to return the dictionary with each character count available
def getCharacterCount(string):
	dictionary = {}

	for c in string:
		if c not in dictionary:
			dictionary[c] = 1
		else:
			dictionary[c] += 1

	print dictionary
	return dictionary

print checkPermutation("aada","daaa")
print checkPermutation("2134", "212")
print checkPermutation("2134", "4321")
print checkPermutation("asdf", "fdxa")