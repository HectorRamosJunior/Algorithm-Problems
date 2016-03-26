'''
	Depth First Search Learning Example
	My first implementation of this type of algorithm
'''

#Assumes directed graphs for now
class Node(object):
	def __init__(self, data):
		self.data = data
		self.visited = False
		self.edges = []
		self.next = None #Placeholder for the queue

	def __str__(self):
		return str(self.data)


def breadthFirstSearch(root):
	if not root:
		print "Current node doesn't exist!"
		return None
	elif root.visited:
		print "Current node has already been visited!"
		return None

	root.visited = True
	print "Visited node with data %s." %str(root)

	queue = []
	for node in root.edges:
		queue.append(node)


	while queue:
		currentNode = queue.pop(0)
		currentNode.visited = True
		print "Visited node with data %s." %str(currentNode)

		for node in currentNode.edges:
			if not (node in queue or node.visited):
				queue.append(node)

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

breadthFirstSearch(node1)



