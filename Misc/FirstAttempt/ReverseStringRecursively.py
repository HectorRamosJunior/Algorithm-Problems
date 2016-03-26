"""
    Write code to reverse a string without using loops
"""

def reverse_string(s):
    if len(s) == 1:
        return s

    last_character = s[-1]
    newString = s[:len(s) - 1]

    if not newString:
        return last_character

    return last_character + reverse_string(newString)

print reverse_string("abcde")