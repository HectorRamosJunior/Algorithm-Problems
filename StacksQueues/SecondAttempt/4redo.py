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

	def peek(self):
		if self.isEmpty():
			print "Stack is empty!"
			return None
		else:
			return self.lastNode

	def push(self, data):
		self.lastNode = Node(data, self.lastNode)

	def pop(self):
		if self.isEmpty():
			print "Stack is empty!"
			return None
		else:
			poppedNode = self.lastNode

			self.lastNode = self.lastNode.prev
			return poppedNode


class MyQueue(object):
	def __init__(self):
		self.stack = Stack()
		self.reversed = False

	def reverseStack(self):
		tempStack = Stack()
		node = self.stack.lastNode

		while node:
			tempStack.push(self.stack.pop())
			node = node.prev

		if self.reversed:
			self.reversed = True
		else:
			self.reversed = False

		self.stack = tempStack


	def peek(self):
		if self.reversed:
			self.reverseStack()

		return self.stack.peek()

	def push(self, data):
		if self.reversed:
			self.reverseStack()

		return self.stack.push(data)

	def pop(self):
		if self.stack.isEmpty():
			print "Queue is empty!"
			return None
		elif not self.reversed:
			self.reverseStack

		self.stack.pop()

	def printQueue(self):
		node = self.stack.lastNode

		if self.reversed:
			self.reverseStack()

		while node:
			print node
			node = node.prev 

		print "End of Queue"


q = MyQueue()

for x in xrange(10):
	q.push(x+1)

q.printQueue()

print "Peeked %s" %q.peek()

for x in xrange(4):
	q.pop()

print "Peeked %s" %q.peek()
q.printQueue()



