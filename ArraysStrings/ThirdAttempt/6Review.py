"""
  Implement a method to perform basic string compression using the counts of repeated characters.
  For example, the string "aabcccccaaa" would become "a2b1c5a3". If the "compressed" string would not
  become smaller than the original string, your method should return the original string. 
  You can assume the string only has Upper and Lowercase letters (a-z).
"""

#Uses a string buffer list for building efficiency
def compressString(string):
    if len(string) <= 1:
      return string

    strList = []
    charCount = 0

    for i in xrange(len(string)):
        charCount += 1

        if i+1 >= len(string) or string[i] != string[i+1]:
            strList.append(string[i] + str(charCount))
            charCount = 0

    compressed = "".join(strList)

    if len(compressed) < len(string):
        return compressed
    else: 
        return string


print compressString("aaabbbccdddddeeeeeed")
print compressString("abc")