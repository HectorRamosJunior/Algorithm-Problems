def checkPermutation(string1,string2):
	if len(string1) != len(string2):
		return False
	else:
		dictionary1 = getCharacterCount(string1)
		dictionary2 = getCharacterCount(string2)

		for c in dictionary1:
			if (not c in dictionary2) or (dictionary1[c] != dictionary2[c]):
				return False

		return True




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