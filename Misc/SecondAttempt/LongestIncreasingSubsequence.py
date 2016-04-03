"""Find the longest increasing subsequence in the given array.
The subsequence's elements do not have to be adjacent indexes in the array.
They just need to increase by index and value.

This is the dynamic programming solution.

Hector Ramos
4/3/2016
"""

# Dynamically Programmed. Stores the list of each index's largest 
# Subsequence as you go, looking backwards for the longest
def longest_increasing_subsequence(array):
    # Array of lists, will hold the longest increasing subsequence
    # at each array index possible for the given index's value.
    lis_list = [ [] for x in xrange(len(array)) ]

    # Goes through creating a longest_increasing_subsequence_list for
    # Each element in the array; this guarantees all longest subsequences
    for i in xrange(len(array)):
        for j in xrange(i):
            # Only look at previous lists that this one could append to
            if array[j] < array[i]:
                # If a previous lis + current index would be longer
                # Than the current list at i, copy j's list as i
                if len(lis_list[j]) + 1 > len(lis_list[i]):
                    lis_list[i] = list(lis_list[j])

        # Append the value of i to the end of the lis for this index
        lis_list[i].append(array[i])

    # Return the longest subsequence in the array of longest subsequences
    # For each possible element in the array
    longest_subsequence = []
    for subsequence in lis_list:
        if len(subsequence) > len(longest_subsequence):
            longest_subsequence = subsequence

    return longest_subsequence


if __name__ == "__main__":
    from random import randint

    array = [randint(-100, 100) for x in xrange(10)]

    print "The randomized given array to find the LIS in is :"
    print array

    longest_subsequence = longest_increasing_subsequence(array)
    print "\nThe LIS for the given array is: "
    print longest_subsequence
