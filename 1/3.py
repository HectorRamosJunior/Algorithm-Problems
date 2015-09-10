"""
  Write a method to replace all spaces in a string with "%20". 
  You may assume that the string has sufficient space at the end to hold all additional characters,
  and that you are given the 'true length' of the string.
"""

#Alternative to test: iterate through string once, detect all empty spaces,
#Modify in seperate iteration... is that faster?


#Repeatedly concatenates new string with any deteceted discrepancies
def URLify(string):
	if(len(string) < 2): #Won't accept empty or 1 character strings
		return "String is too short!"
	else:
		URLified = ''

		for i in range(len(string)):
			if(string[i] == " "):
				URLified += "%20"
			else:
				URLified += string[i]
		return URLified

print URLify("a b c d e")
print URLify("a")
print URLify("  ")
print URLify("asdfasdfasf")