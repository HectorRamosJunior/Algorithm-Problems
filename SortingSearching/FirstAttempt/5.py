"""
    Given a sorted array of strings that is interspersed with empty 
    strings, write a method to find the index of a given string.
    EX: ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
    Input: "ball"               Output: 4
"""

# Implements a modified binary search to find the wanted string index
def sparseSearch(array, s):
    index = 0
    lowerBound = None
    upperBound = None

    # Define lowerBound starting index
    while index < len(array):
        if array[index] != "":
            if array[index] == s:   # Handle if given string caught here
                return index

            lowerBound = index
            break
        index += 1

    # Define upperBound starting index
    index = len(array) - 1
    while index >= 0:
        if array[index] != "":
            if array[index] == s:   # Handle if given string caught here
                return index

            upperBound = index
            break
        index -= 1

    # Handle if bounds could not be defined
    if lowerBound == None or upperBound == None:
        return None
    # Handle if the bounds index the same location
    if upperBound == lowerBound:
        return None


    # Implement binary search to find the wanted index
    index = (lowerBound + upperBound) / 2
    while True:
        # Assign middle index nearest non empty string
        if array[index] == "":
            
            # Search nearby elements for non empty strings
            counter = 1
            while True:
                # Handle if reassignment crosses the bounds
                if index - counter <= lowerBound or index + counter >= upperBound:
                    return None
                elif array[index - counter] != "":
                    index = index - counter
                    break
                elif array[index + counter] != "":
                    index = index + counter 
                    break

                counter += 1

        # Implement standard binary search from here
        if array[index] == s:
            return index
        elif array[index] < s:
            lowerBound = index
            index = (lowerBound + upperBound) / 2
        elif array[index] > s:
            upperBound = index 
            index = (lowerBound + upperBound) / 2

        # Handle if bounds met by new index
        if index <= lowerBound or index >= upperBound:
            return None




array = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
print array

s = "car"
output = sparseSearch(array, s)
print "The index for string %s is at index %s." %(s, str(output))

s = "ball"
output = sparseSearch(array, s)
print "The index for string %s is at index %s." %(s, str(output))

s = "dad"
output = sparseSearch(array, s)
print "The index for string %s is at index %s." %(s, str(output))