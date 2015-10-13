"""
	Implement a MyQueue class which implements a queue using two stacks.

	Definitions: Queue = FIFO stack, stack = LIFO stack 
	Make the functions peek(), isEmpty(), and push() and pop()
"""

class Node(object):
	def __init__(self, data=None, prev=None):
		self.data = data
		self.prev = prev

	def __str__(self):
		return str(self.data)


class Stack(object):
	def __init__(self):
		self.lastNode = None

	def isEmpty(self):
		if self.lastNode:
			return False
		else:
			return True

	def push(self, data):
		if self.isEmpty():
			self.lastNode = Node(data)
		else:
			self.lastNode = Node(data, self.lastNode)

	def pop(self):
		if self.isEmpty():
			print "Stack is empty!"
			return None
		else:
			poppedNode = self.lastNode
			if self.lastNode.prev:
				self.lastNode = self.lastNode.prev
			else:
				self.lastNode = None
			return poppedNode

	def peek(self):
		return self.lastNode

class MyQueue(object):
	def __init__(self):
		self.stack = Stack()

	def enqueue(self, data):
		self.stack.push(data)

	def dequeue(self):
		tempStack = Stack()

		while not self.stack.isEmpty():
			tempStack.push(self.stack.pop())

			while not self.stack.isEmpty():
				tempStack.push(self.stack.pop())

			dequeued = tempStack.pop()

			while not tempStack.isEmpty():
				self.stack.push(tempStack.pop())

			return dequeued

	def printQueue(self):
		tempNode = self.stack.lastNode

		while tempNode:
			print tempNode
			tempNode = tempNode.prev

		print "End of Queue"



q = MyQueue()

for x in xrange(100):
	q.enqueue(x+1)

q.printQueue()


for x in xrange(15):
	q.dequeue()

q.printQueue()



