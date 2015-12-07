"""
  Write a method to replace all spaces in a string with "%20". 
  You may assume that the string has sufficient space at the end to hold all additional characters,
  and that you are given the 'true length' of the string.
"""

def URLify(s, length):
    string = list(s)
    spaces = 0

    for i in xrange(length):
        if s[i] == " ":
            spaces += 1



    index = (length + spaces * 2) - 1

    for i in xrange(length-1, -1, -1):
        if string[i] != " ":
            string[index] = string[i]
            index -= 1
        else:
            string[index] = "0"
            string[index-1] = "2"
            string[index-2] = "%"
            index -= 3
        print string

    return string

string = ["A"," ", "B", " ", "C", " ", " ", " ", " ", " ", " "]
print URLify(string, 5)