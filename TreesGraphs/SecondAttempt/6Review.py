'''
    Successor: 
    Write an algorithm to find the "next" node (i.e., in order Successor)
    of a given node in a binary search tree. You may assume that each 
    node has a link to its parent.
'''

# Returns the sucessor of the current node in the tree using
# in-order traversal (left, root, right)
def inOrderSuccessor(node):
    # Right child of current node is a successor
    if node.right:
        return node.right

    # Goes up the tree until the current node is the left child
    # of the parent node
    while True:
        if not node.parent:
            return None
        elif node is node.parent.left:
            return node.parent
        elif node is node.parent.right:
            node = node.parent


class Node(object):
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = None
    def __str__(self):
        return "Node %s" % str(self.data)


# Tree is as shows:
#         0
#     1       2
#   3       4   5
n0 = Node(0); n1 = Node(1)
n2 = Node(2); n3 = Node(3)
n4 = Node(4); n5 = Node(5)

n0.left = n1; n0.right = n2
n1.parent = n0; n2.parent = n0

n1.left = n3; n1.right = None
n3.parent = n1

n2.left = n4; n2.right = n5
n4.parent = n2; n5.parent = n2


print "The succsessor is: ", inOrderSuccessor(n0)
print "The succsessor is: ", inOrderSuccessor(n3)
print "The succsessor is: ", inOrderSuccessor(n4)
print "The succsessor is: ", inOrderSuccessor(n2)
print "The succsessor is: ", inOrderSuccessor(n5)