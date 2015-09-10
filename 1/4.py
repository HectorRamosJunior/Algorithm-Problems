"""
  Given a string, write a function to check if it is a permutation of a palindrome.
  A palindrome is a word or phrase that is the same forwards and backwards.
  The palindrome does not have to be limited to dictionary words.
"""

#Sorts the string, then checks if there are exactly two character counts
#of each character present, unless if the string's length is odd (one outlier)
def checkPermofPalindrome(string):
	if len(string) < 2:
		return False
	elif len(string) == 2: #all 2 character strings are palindromes
		return True
	elif len(string) == 3:
		string = sorted(string)
		if (string[1] != string[0] and
				string[1] != string [2]):
			return False	
		else:
			return True
	else:
		string = sorted(string)		#sort first
		if(len(string) % 2 == 0): 	#Even (all must be duplicates)
			check = 1
		else:						#Odd (one unique character allowed)
			check = 0

		#Check the first and last element, not done in loop below
		if string[0] != string[1]:
			check += 1
		if string[len(string)-1] != string[len(string)-2]:
			check += 1

		#Checks each character in the sorted string for characters without
		#dupicate on both sides. 
		for i in range(1,len(string)-1):
			if (string[i] != string[i-1] and 
					string[i] != string[i+1]):
				check += 1
			if check > 1:	
				return False

		return True
		

print checkPermofPalindrome("racecar")
print checkPermofPalindrome("cdefg")
print checkPermofPalindrome("aabbc")
print checkPermofPalindrome("abcd")
print checkPermofPalindrome("baab")
print checkPermofPalindrome("")
print checkPermofPalindrome("abc")
print checkPermofPalindrome("abb")
print checkPermofPalindrome("aa")
print checkPermofPalindrome("ab")
