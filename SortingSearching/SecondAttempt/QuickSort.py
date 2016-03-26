"""
    Quick Sort for lists
    Doesn't stack overflow unlike the first iteration!
    Hector Ramos
    03/25/2015
"""

# Initializes first call of the recursive quick_sort_helper function 
def quick_sort(array):
    if len(array) < 1:
        return 

    quick_sort_helper(array, 0, len(array) - 1)
    return array

# Sorts array with recursive subarray sorts around randomly selected pivots
def quick_sort_helper(array, start_index, end_index):
    # If subarray only 1 index long it's already sorted
    if end_index - start_index == 0:
        return

    # Define left and right iterators to ends of subarray
    left_index = start_index
    right_index = end_index

    # Randomly assign pivot to a subarray value 
    pivot = array[randint(start_index, end_index)]

    # Sorts the subarray around the pivot.
    # Sort is finished anytime the indexes pass each other (left > right)
    while left_index <= right_index:
        # Iterate left_index forward until an index >= pivot is found
        while array[left_index] < pivot and left_index <= right_index:
            left_index += 1
        # Iterate right_index backward until an index <= pivot is found
        while array[right_index] > pivot and left_index <= right_index:
            right_index -= 1

        # Catch if nested loops ended the sort (left > right)
        if left_index > right_index:
            break

        # Swap the values of the left and right indices
        array[left_index], array[right_index] = array[right_index], array[left_index]
        
        # Only iterate left and right indices if they'd stay in subarray range
        if left_index < end_index:
            left_index += 1
        if right_index > start_index:
            right_index -= 1

    # Recursively call on new subarrays formed around the pivot
    quick_sort_helper(array, start_index, right_index)
    quick_sort_helper(array, left_index, end_index)


from random import randint
array = []
[array.append(randint(1,100)) for x in xrange(100)]

print array
print quick_sort(array)