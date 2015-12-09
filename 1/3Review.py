"""
  Write a method to replace all spaces in a string with "%20". 
  You may assume that the string has sufficient space at the 
  end to hold all additional characters, and that you are given the 
  'true length' of the string.
"""

#Iterates through the string backwards to replace spaces
def URLify(s, length):
    string = list(s) #Strings are immutable, so use a list
    spaces = 0 

    #Counts how many spaces in list to offset when iterating
    for i in xrange(length):
        if s[i] == " ":
            spaces += 1


    #Goes as far back in the list as necessary(adjusting for %20)
    index = (length + spaces * 2) - 1

    #Iterates through list backwards, moving characters
    #From the original list and appending %20 for spaces
    for i in xrange(length-1, -1, -1):
        if string[i] != " ":
            string[index] = string[i]
            index -= 1
        else:
            string[index] = "0"
            string[index-1] = "2"
            string[index-2] = "%"
            index -= 3 #Each space encountered takes 3 indexes
        print string

    return string

string = ["A"," ", "B", " ", "C", " ", " ", " ", " ", " ", " "]
print URLify(string, 5)