'''
    Validate BST: 
    Implement a function to check if a binary tree is a binary search tree.

    Note to future self:
    This is the question that got my first interview with Bloomberg,
    went to the final round of interviews up to head of R&D.
'''
from Node import Node
import sys

def validateBST(node, localMin = -sys.maxint, localMax = sys.maxint):
    if not node:
        return True
    elif node.value < localMin or node.value > localMax:
        return False

    left = validateBST(node.left, localMin, node.value)
    right = validateBST(node.right, node.value, localMax)

    if not (left and right):
        return False

    return True



root = Node(5, 
                Node(3,
                        Node(2), Node(4)),
                Node(7,
                        Node(6), Node(8))
                                            )

print validateBST(root)

root = Node(5, 
                Node(3,
                        Node(2), Node(4)),
                Node(7,
                        Node(6), Node(0))
                                            )

print validateBST(root)




