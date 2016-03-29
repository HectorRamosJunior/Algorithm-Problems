"""
    0,1 Knapsack Optimization Solution
    Employs a greedy algorithm to solve the problem
    Tests min weight, max value, and max value/weight lists together
    Hector Ramos
    3/29/2016
"""

# Returns a list of the items to take to optimize value when given
# A variety of items of certain weights to fit into a bag of weight X
# Employs a greedy algo for this, take the first highest metric if possible
# And go down the items in order of the metric fitting what's possible
def get_knapsack_list(node_list, max_weight):
    # Copy the list so as to not affect the original with sorts
    sorted_by_value = list(node_list)
    sorted_by_weight = list(node_list)
    sorted_by_ratio = list(node_list)

    # Set node metrics to value for merge sort, then sort
    set_nodes_metric(node_list, "value")
    sorted_by_value = merge_sort(sorted_by_value)
    
    # Set node metrics to weights for merge sort, then sort
    set_nodes_metric(node_list, "weight")
    sorted_by_weight = merge_sort(sorted_by_weight)
    # Reverse so elements weight ascend not descend
    sorted_by_weight.reverse()
    
    # Set node metrics to value/weight ratio for merge sort, then sort
    set_nodes_metric(node_list, "ratio")
    sorted_by_ratio =  merge_sort(sorted_by_ratio)

    # Fill knapsack lists greedily using the sorted lists
    value_knapsack = fill_knapsack(sorted_by_value, max_weight)
    weight_knapsack = fill_knapsack(sorted_by_weight, max_weight)
    ratio_knapsack = fill_knapsack(sorted_by_ratio, max_weight)

    # Assign sums for determining the knapsack to be output
    value_sum = get_sum(value_knapsack)
    weight_sum = get_sum(weight_knapsack)
    ratio_sum = get_sum(ratio_knapsack)

    # Determine best knapsack, return list of nodes in knapsack
    if value_sum >= weight_sum and value_sum >= ratio_sum:
        print "\nTaking by max values first most optimal.\n"
        return value_knapsack
    elif weight_sum >= value_sum and weight_sum >= ratio_sum:
        print "\nTaking by min weights first most optimal.\n"
        return weight_knapsack
    elif ratio_sum >= value_sum and ratio_sum >= weight_sum:
        print "\nTaking by max value/weight ratios first most optimal.\n"
        return ratio_knapsack

# Set the metric parameter of all node objects in the list to the 
# Specified metric of interest. This is so merge sort can handle the 3 cases
def set_nodes_metric(node_list, metric_of_interest):
    if metric_of_interest == "value":
        for node in node_list:
            node.metric = node.value
    elif metric_of_interest == "weight":
        for node in node_list:
            node.metric = node.weight
    elif metric_of_interest == "ratio":
        for node in node_list:
            node.metric = node.value / node.weight

# Greedy algorithm for filling the knapsack. Takes in a sorted list of nodes
# and takes the most wanted items first if possible as it iterates through
def fill_knapsack(sorted_list, max_weight):
    total_weight = 0

    output_list = []
    for node in sorted_list:
        if total_weight + node.weight <= max_weight:
            total_weight += node.weight
            output_list.append(node)

    return output_list

# Standard merge sort. Calls itself recursively.
def merge_sort(knapsack_list):
    if len(knapsack_list) <= 1:
        return knapsack_list

    middle_index = len(knapsack_list) / 2
    left = merge_sort(knapsack_list[:middle_index])
    right = merge_sort(knapsack_list[middle_index:])

    return merge(left, right)

# Standard merge, sorts the node items in descending order by metric
def merge(left, right):
    if not left:
        return right
    elif not right:
        return left

    output_list = []
    while left and right: 
        if left[0].metric >= right[0].metric:
            output_list.append(left.pop(0))
        elif right[0].metric > left[0].metric:
            output_list.append(right.pop(0))

    # Handle if elements in left or right list left over, append if so
    if left and not right:
        for i in xrange(len(left)):
            output_list.append(left.pop(0))
    # Handle if elements in right list left over
    elif right and not left:
        for i in xrange(len(right)):
            output_list.append(right.pop(0))

    return output_list

# Returns the total value of the items in the knapsack list
def get_sum(knapsack_list):
    total = 0
    for node in knapsack_list:
        total += node.value

    return total

class Node(object):
    def __init__(self, key, value, weight):
        self.key = key
        self.value = value
        self.weight = weight
        self.metric = None

# Returns a key string list representation of a list of nodes
def get_node_keys_as_list(node_list):
    output_string = ""
    for i in xrange(len(node_list)):
        if i == len(node_list) - 1:
            output_string += node_list[i].key + "."
        else:
            output_string += node_list[i].key + ", "

    return output_string

if __name__ == "__main__":
    # Knapsack problem values taken from below URL:
    # http://i.imgur.com/TOoWaI8.png
    node_list = [
                    Node("Green", 4, 12), Node("Blue", 2, 2),
                    Node("Grey", 2, 1), Node("Red", 1, 1),
                    Node("Yellow", 10, 4)
                ]

    knapsack_list = get_knapsack_list(node_list, 15)

    output_string = get_node_keys_as_list(knapsack_list)

    print "The knapsack consists of:\n", output_string
