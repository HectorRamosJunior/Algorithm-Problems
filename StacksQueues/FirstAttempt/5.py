"""
	Write a program to sort a stack such that the smallest items are on the top.
	You can use an additional temporary stack, but you may not copy the elements
	into any other data structure. (Such as an array). The stack suppors the following
	operations: push, pop, peek, isEmpty.
"""
"""
	Props to my girlfriend for coming up with this solution with my plate Analogy
"""

from random import randint

class Node(object):
	def __init__(self, data=None, prev=None):
		self.data = data
		self.prev = prev


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
			return self.lastNode.data

	def push(self, data):
		self.lastNode = Node(data, self.lastNode)

	def pop(self):
		if self.isEmpty():
			print "Stack is empty!"
			return None
		else:
			poppedNode = self.lastNode

			self.lastNode = self.lastNode.prev
			return poppedNode.data

	def printStack(self):
		node = self.lastNode
		while node:
			print node.data
			node = node.prev	

		print "End of Stack"

def sortStack(stack1):
	stack2 = Stack()

	while not stack1.isEmpty():
		tempVar = stack1.pop()
		counter = 0

		while tempVar:
			if stack2.isEmpty():
				stack2.push(tempVar)
				tempVar = None
			elif stack2.peek() < tempVar:
				stack2.push(tempVar)
				tempVar = None
			else:
				stack1.push(stack2.pop())
				counter += 1

		for x in xrange(counter):
			stack2.push(stack1.pop())
			counter -= 1

		


	node = stack2.lastNode
	while node:
		stack1.push(stack2.pop())
		node = node.prev


	return stack1


s = Stack()
for x in xrange(10):
	s.push(randint(0,100)) 

s.printStack()

sortStack(s)

s.printStack()