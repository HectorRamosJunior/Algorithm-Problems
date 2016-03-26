'''
	Given a binary tree, design an algorithm which creates a linked list
	of all the nodes at each depth 
	(eg.  If you have a tree with depth D, you'll have D linked lists.)
'''

class Node(object):
	def __init__(self, data = None, left = None):
		self.data = data
		self.left = left
		self.right = None

	def __str__(self):
		return str(self.data)

class Queue(object):
	def __init__(self):
		self.headNode = None
		self.footNode = None

	def push(self, data):
		if not self.headNode:
			self.headNode = Node(data)
			self.footNode = self.headNode
		else:
			self.footNode.right = Node(data, self.footNode)
			self.footNode = self.footNode.right	

	def pop(self):
		if not self.footNode:
			print "Queue is empty! Nothing to pop!"
			return None
		elif self.footNode is self.headNode:
			self.footNode = None
			self.headNode = None
		else:
			self.footNode = self.footNode.left
			self.footNode.right.left = None
			self.footNode.right = None

	def printQueue(self):
		node = self.headNode
		s = ""

		while node:
			s += str(node) + " "
			node = node.right

		return s 


def depthList1(root, counter = 0, depthArray = []):
	if counter + 1 > len(depthArray):
		depthArray.append(Queue())

	depthArray[counter].push(root)

	if root.left:
		depthList1(root.left, counter+1, depthArray)
	if root.right:
		depthList1(root.right, counter+1, depthArray)

	return depthArray	

def depthList2(root):
	if not root:
		print "root does not exist!"
		return None

	q = []
	q.append(root)

	depthArray = [Queue()]
	depth = 0

	currentLevelCount = 1
	nextLevelCount = 0

	while q:
		node = q.pop(0)
		currentLevelCount -= 1
		depthArray[depth].push(node)

		if node.left:
			q.append(node.left)
			nextLevelCount += 1
		if node.right:
			q.append(node.right)
			nextLevelCount += 1
		if currentLevelCount == 0:
			currentLevelCount = nextLevelCount
			depth += 1
			depthArray.append(Queue())
			nextLevelCount = 0

	return depthArray


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

depthArray = depthList1(node1)

for x in depthArray:
	print x.printQueue()

depthArray = depthList2(node1)
print "\n\n" 

for x in depthArray:
	print x.printQueue()