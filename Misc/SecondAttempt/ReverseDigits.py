"""
    Write code to reverse digits in an integer 
    without converting it to a string.

    This time, recursively!
"""

def reverse_digits(x):
    # Initialize recursive function.
    # The second value of the tuple is not needed.
    output, dummy_variable = reverse_digits_helper(x)

    return output

# Recursive function returns the tuple of output and digit_place
def reverse_digits_helper(x):
    # Hit the first digit, start unwinding
    if x / 10 == 0:
        return x, 1
    else:
        # Store the last digit until new digit place is known
        digit = x % 10
        # Remove digit stored for the recursive call
        x = x / 10

        # Get current reversed integer and digit_place for this call's digit
        output, digit_place = reverse_digits_helper(x)

        # Add stored digit to the Most Significant Bit
        output += digit * (10 ** digit_place)

        return output, (digit_place + 1)

print reverse_digits(1234567890)
