class Node(object):

	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

	def __str__(self):
		return str(self.data)

#	def get_data(self):
#		return self.data
#
#	def get_next(self):
#		return self.next
#
#	def set_next(self, new_next):
#		self.next = new_next
#
#	def set_data(self, data):
#		self.data = data

def print_list(node):
	while(node):
		print node
		node = node.next
	print "End"

