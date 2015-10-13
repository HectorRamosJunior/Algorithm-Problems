'''
	Route Between Nodes:
	Given a directed graph, design an algorithm to find out whether 
	there is a route between two nodes.
'''

class Node(object):
	def __init__(self, data):
		self.data = data
		self.visited1 = False
		self.visited2 = False
		self.edges = []

	def __str__(self):
		return str(self.data)


def routeBetweenNodes(root1, root2):
	if not (root1 or root2):
		print "One of the entered nodes does not exist"
		return False
	elif root1 is root2:
		print "Both roots entered are the same node!"
		return True

	root1.visited1 = True
	q1 = root1.edges #queue array
	print "Search 1 starting at %s" %root1

	root2.visited2 = True
	q2 = root2.edges #queue array
	print "Search 2 starting at %s." %root2

	#Implement BFS on both roots at the same time 
	while q1 or q2:
		if q1:
			node1 = q1.pop(0)
			node1.visited1 = True
			print "Search 1 visited %s." %str(node1)

			for n in node1.edges:
				if not (n in q1 or n.visited1):
					q1.append(n)
		else:
			node1 = False

		if q2:
			node2 = q2.pop(0)
			node2.visited2 = True
			print "Search 2 visited %s." %str(node2)

			for n in node2.edges:
				if not (n in q2 or n.visited2):
					q2.append(n)
		else:
			node2 = False

		if node1:
			if node1.visited2:
				print "Found the connecting node at %s." %(node1)
				return True

		if node2:
			if node2.visited1:
				print "Found the connecting node at %s." %(node2)
				return True

	return False 

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

print routeBetweenNodes(node3, node6)