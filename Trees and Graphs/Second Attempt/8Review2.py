'''
    First Common Ancestor: 
    Design an algorithm and write code to find the first common ancestor
    of two nodes in a binary tree. Avoid storing additional nodes in a
    data structure. NOTE: This is not necessarily a BST.
'''
from Node import Node 

# Function assumes the nodes do not have links to their parents
# Descends from the tree branches in the the direction both nodes lie
# Once nodes are in different branches of a given node, it's the first ancestor
def firstCommonAncestor(root, node1, node2):
    containsNode1 = contains(root, node1)
    containsNode2 = contains(root, node2)

    # Makes sure the tree contains both node1 and node2
    if not (containsNode1 and containsNode2):
        return None

    # While True since both nodes in tree. Travels down the tree from root
    while True:
        # Handle if current root is either node
        if root is node1 or root is node2:
            return root

        # Checks which branch each node falls under with a bool
        leftBranchContainsNode1 = contains(root.left, node1)
        leftBranchContainsNode2 = contains(root.left, node2)

        # If both nodes are in different branches, root is the first ancestor
        if leftBranchContainsNode1 != leftBranchContainsNode2:
            return root
        # If both nodes are in the left branch, descend down the left branch
        elif leftBranchContainsNode1 and leftBranchContainsNode2:
            root = root.left
        # If both nodes are in the right branch, descend down the right branch
        elif not (leftBranchContainsNode1 and leftBranchContainsNode2):
            root = root.right



# Implements bfs to see if node2 is in root's tree
def contains(root, node):
    q = [root]

    while q:
        n = q.pop(0)

        # If node in tree, return True
        if n is node:
            return True

        if n.right:
            q.append(n.right)
        if n.left:
            q.append(n.left)


    return False


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

print "The first common ancestor is: %s" % firstCommonAncestor(n0, n4, n5)
print "The first common ancestor is: %s" % firstCommonAncestor(n0, n3, n4)
print "The first common ancestor is: %s" % firstCommonAncestor(n0, n3, n1)
print "The first common ancestor is: %s" % firstCommonAncestor(n0, n1, Node(0))