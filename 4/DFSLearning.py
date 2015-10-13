'''
	Depth First Search Learning Example
	My first implementation of this type of algorithm
'''

#Assumes directed graphs for now
class Node(object):
	def __init__(self, data):
		self.data = data
		self.edges = []
		self.visited = False

	def __str__(self):
		return str(self.data)

def depthFirstSearch(root):
	if not root:
		print "Current root does not exist!"
		return None
	elif root.visited:
		print "Root has already been visited!"
		return None

	root.visited = True
	print "Visited node with data %s." %str(root)

	if len(root.edges) > 0:
		for node in root.edges:
			if not node.visited:
				depthFirstSearch(node)

	return None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

node1.edges = [node2, node5]
node2.edges = [node3, node6]
node4.edges = [node1]
node5.edges = [node4, node6, node7]
node6.edges = [node7]
node7.edges = [node4]

depthFirstSearch(node1)

