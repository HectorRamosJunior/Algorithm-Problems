'''
	Validate BST: 
	Implement a function to check if a binary tree is a binary search tree.
'''

class Node(object):
	def __init__(self, data=None, left=None):
		self.data = data
		self.left = left
		self.right = None

	def __str__(self):
		return str(self.data)

def