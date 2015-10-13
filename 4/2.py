'''
	Minimal Trees:
	Given a sorted (increasing order) array with unique integer elements,
	write an algorithm to create a binary search tree with minimal height.
'''

class Node(object):
	def __init__(self, data=None):
		self.data = data
		self.left = None
		self.right = None

	def __str__(self):
		return str(self.data)


def minimalTrees(arr):
	if not arr:
		print "Array has no elements!"
		return None

	elif len(arr) == 1:
		return Node(arr[0])

	elif len(arr) == 2:
		root = Node(arr[1])
		root.left = Node(arr[0])
		return root

	elif len(arr) == 3:
		root = Node(arr[1])
		root.left = Node(arr[0])
		root.right = Node(arr[2])
		return root

	else:
		leftArray = []
		rightArray = []

		for x in xrange(len(arr)/2 -1):
			leftArray.append(arr[x])

		for y in xrange(len(arr)/2, len(arr)):
			rightArray.append(arr[y])

		root = Node(arr[len(arr)/2 -1])
		root.left = minimalTrees(leftArray)
		root.right = minimalTrees(rightArray)
		return root

def printTree(root):
	if not root:
		return "There's no root!"
	
	q = []
	q.append(root)

	currentRow = ""
	counter = 0
	threshold = 2

	while q:
		node = q.pop(0)
		currentRow += str(node) + " "

		counter += 1

		if counter == (threshold - 1) or counter == 1:
			print currentRow
			threshold *= 2
			currentRow = ""

		if node:
			q.append(node.left)
			q.append(node.right) 

	print currentRow

printTree(minimalTrees(range(1,11)))

