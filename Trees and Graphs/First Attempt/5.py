'''
	Validate BST: 
	Implement a function to check if a binary tree is a binary search tree.
'''

class Node(object):
	def __init__(self, data=None, left=Nnoe):
		self.data = data
		self.left = left
		self.right = None

	def __str__(self):
		return str(self.data)

def validateBST(root, localMax = 99999, localMin = -1):
    if (root.data > localMax) or (root.data < localMin):
        return False

    print "At Root valued %s" %root.data
    left = True
    right = True

    if root.left:
        left = validateBST(root.left, root.data, localMin)
    if root.right:
        right = validateBST(root.right, localMax, root.data)
    else:
        return True

    if not (left and right):
        return False
    else: 
        return True

node1 = Node(8)
node2 = Node(3)
node3 = Node(10)
node4 = Node(1)
node5 = Node(6)
node6 = Node(14)
node7 = Node(4)
node8 = Node(7)
node9 = Node(13)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
node5.left = node7
node5.right = node8
node6.left = node9


print validateBST(node1)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
node10 = Node(10)

node1.left = node2
node1.right = node3
node2.left = node4
node3.left = node5
node3.right = node6
node6.left = node7
node6.right = node8
node8.right = node9
node9.right = node10

print validateBST(node1)