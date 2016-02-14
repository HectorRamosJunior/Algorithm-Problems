'''
    Validate BST: 
    Implement a function to check if a binary tree is a binary search tree.
'''
from Node import Node 

#Keeps track of the last in-order node's value in this DFS function
lastValue = None

def isBST(node):
    if not node:
        return True

    #Needed to take the global variable in by reference
    global lastValue


    if not isBST(node.left):
        return False

    #If current node is less than previous in order node, not a BST
    if lastValue and (node.value <= lastValue):
            return False

    #Last value checked was current node's
    lastValue = node.value

    if not isBST(node.right):
        return False


    return True




root = Node(5, 
                Node(3,
                        Node(2), Node(4)),
                Node(7,
                        Node(6), Node(8))
                                            )

print isBST(root)

root = Node(5, 
                Node(3,
                        Node(2), Node(4)),
                Node(7,
                        Node(6), Node(0))
                                            )

print isBST(root)
