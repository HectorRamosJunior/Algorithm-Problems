"""Find the longest increasing subsequence in the given array.
The subsequence's elements do not have to be adjacent indexes in the array.
They just need to increase by index and value.

This is a brute force solution.

Hector Ramos
4/3/2016
"""
max_list = []

# Runs through every possible subsequence with each starting index
def longest_increasing_subsequence(array):
    for i in xrange(len(array)):
        increasing_subsequence_helper(array, i)

    return max_list

# Runs through every possible subsequence iteration for given starting index
def increasing_subsequence_helper(array, current_index, current_list=[]):
    # Base case: Call is at the end of the array for current subsequence
    if current_index >= len(array):
        global max_list

        # Reassign global max_list if current list is longer
        if len(current_list) > len(max_list):
            max_list = current_list
            return

    # Recursively call every possible subsequence combination from 
    # Current index to the end of the array
    for i in xrange(current_index, len(array)):
        if not current_list or current_list[-1] < array[i]:
            # Copy list to not affect current one by reference
            new_list = list(current_list)
            new_list.append(array[i])

            increasing_subsequence_helper(array, i+1, new_list)


if __name__ == "__main__":
    array = [99, 0, 10, 2, 9, 4, 3, 5, 8, 7, 5]
    print longest_increasing_subsequence(array)

    array = [20, 3, 4, -2, -1, 0, 5, 8, 2, 3, 12, 7, 9, 10]
    print longest_increasing_subsequence(array)
