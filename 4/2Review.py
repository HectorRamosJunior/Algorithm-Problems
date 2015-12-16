'''
    Minimal Trees:
    Given a sorted (increasing order) array with unique integer elements,
    write an algorithm to create a binary search tree with minimal height.
'''
from Node import Node

#Recursively calls and divides the sorted array in half
#Less than root goes to the left tree, greater than to the right
def makeBST(array):
    if not array:
        return None

    length = len(array)
    if length == 1:
        node = Node(array[0], None, None)
    else:
        midpoint = length/2

        left = makeBST(array[ : midpoint - 1])
        right = makeBST(array[midpoint + 1 : length - 1])
        
        node = Node(array[midpoint], left, right)

    return node 


array = range(1,101)

root = makeBST(array)
root.printTree()