def checkPermofPalindrome(string):
	if len(string) < 2:
		return False
	elif len(string) == 2:
		return True
	elif len(string) == 3:
		string = sorted(string)
		if (string[1] != string[0] and
				string[1] != string [2]):
			return False	
		else:
			return True
	else:
		string = sorted(string)
		if(len(string) % 2 == 0):
			check = 1
		else:
			check = 0

		if string[0] != string[1]:
			check += 1
		if string[len(string)-1] != string[len(string)-2]:
			check += 1

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
