'''
	Check Balanced:
	Implement a function to check if a binary tree is balanced.
	For the purposes of this question, a balanced tree is defined to be a tree such that
	the heights of the two subtrees of any node never differ by more than one.
'''

class Node(object):
	def __init__(self, data = None, left = None):
		self.data = data
		self.left = left
		self.right = None

	def __str__(self):
		return str(self.data)


def checkBalanaced(root):
	if not root:
		return None

	q = [root]
	depth = 0
	endLevel = None
	currentLevelCount = 1
	nextLevelCount = 0

	while q:
		if endLevel and endLevel < (depth - 1):
			return False

		node = q.pop(0)
		currentLevelCount -= 1

		if node.left:
			q.append(node.left)
			nextLevelCount += 1
		if node.right:
			q.append(node.right)
			nextLevelCount += 1
		if not (node.left or node.right):
			if not endLevel:
				endLevel = depth



		if currentLevelCount == 0:
			currentLevelCount = nextLevelCount
			nextLevelCount = 0
			depth += 1

	return True


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

print checkBalanaced(node1)



