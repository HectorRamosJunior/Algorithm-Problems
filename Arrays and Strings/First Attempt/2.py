"""
  Given two strings, write a method to decide if one is a permutation of the other.
"""

#Sort the strings, then check if they are the same string sequentially.
def checkPermutation(string1,string2):
	if (len(string1) != len(string2)): #Different lengths return false
		return False
	elif len(string1) < 2: #Need more than 1 character to be a permutation
		return False
	else:
		string1 = sorted(string1)
		string2 = sorted(string2)

		for i in range(len(string1)):
			if string1[i] != string2[i]:
				return False

		return True


print checkPermutation("aada","daaa")
print checkPermutation("2134", "212")
print checkPermutation("2134", "4321")