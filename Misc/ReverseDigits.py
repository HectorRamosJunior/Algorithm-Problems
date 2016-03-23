"""
    Write code to reverse digits in an integer 
    without converting it to a string.
"""

def reverseDigits(num):
    digitList = []

    digitMod = 10
    digitDiv = 1

    while True:
        temp = num % digitMod
        temp = temp / digitDiv
        digitList.append(temp)

        if num % digitMod == num:
            break

        digitMod *= 10
        digitDiv *= 10

    reversedDigits = 0

    for i in xrange(len(digitList)):
        reversedDigits += (10**i) * digitList[-1 - i]

    return reversedDigits

num = 98502135
print reverseDigits(num)