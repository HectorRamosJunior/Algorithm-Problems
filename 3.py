def URLify(string):
	if(len(string) < 2):
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