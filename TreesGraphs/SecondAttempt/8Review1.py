'''
    First Common Ancestor: 
    Design an algorithm and write code to find the first common ancestor
    of two nodes in a binary tree. Avoid storing additional nodes in a
    data structure. NOTE: This is not necessarily a BST.
'''
from Node import Node 

# Function assumes the nodes have links to their parents
# Moves up node1's parents, checks if parent's other child subtree
# contains node2. If it does, return that node as the ancestor.
def firstCommonAncestor(node1, node2):
    if node1 is node2:
        return node1

    # Check if node 1 is an ancestor of node2
    ancestor = checkSubTree(node1, node2)
    if ancestor:
        return node1 

    # Check if node 2 is an ancestor of node1
    ancestor = checkSubTree(node2, node1)
    if ancestor:
        return node2

    # Check's node1's parent branches to see if node1 and node2
    # are in seperate branches of the same root. If they are, 
    # return the parent node as it is the first common ancestor.
    while node1.parent:
        # If parent node doesn't have both branches, move on
        if node1.parent.left and node1.parent.right:
            if node1.parent.left is node1:
                ancestor = checkSubTree(node1.parent.right, node2)
            elif node1.parent.right is node1:
                ancestor = checkSubTree(node1.parent.left, node2)

        # If true, node1.parent is the first common ancestor
        if ancestor:
            return node1.parent

        node1 = node1.parent

    # No common ancestor
    return None

# Implements bfs to see if node2 is in root's tree
def checkSubTree(root, node2):
    q = [root]

    while q:
        n = q.pop(0)

        # If node2 in tree, return True
        if n is node2:
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


print "The first common ancestor is: %s" % firstCommonAncestor(n4, n5)
print "The first common ancestor is: %s" % firstCommonAncestor(n3, n4)
print "The first common ancestor is: %s" % firstCommonAncestor(n0, n3)
print "The first common ancestor is: %s" % firstCommonAncestor(n1, Node(0))
