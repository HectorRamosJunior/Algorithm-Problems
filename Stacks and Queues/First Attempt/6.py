"""
	An animal shelter, which holds only dogs and cats, operates on a strictly
	"first in, first out" basis. People must either adopt the "oldest"
	(based on arrival time of all animals in the shelter) or they can select 
	whether they would prefer a dog or a cat (and receive the oldest animal of that type)
	They cannot select which specific animal they would like. Create the data structures
	to maintain this system and implement operations such as:
	enqueue, dequeueAny, dequeueDog, dequeueCat. 
	You may use the built-in LinkedList data structure.
"""

from random import randint

class Node(object):
	def __init__(self, number=None, prev=None, name=None):
		self.number = number
		self.name = name
		self.prev = prev
		self.next = None #Can't be defined yet!

	def __str__(self):
		return "#%s, Name is %s." %(str(self.number),str(self.name))


#Below is the implementation of a FIFO stack
class Stack(object):
	def __init__(self):
		self.topNode = None
		self.bottomNode = None

	def isEmpty(self):
		if self.topNode and self.bottomNode:
			return False
		else:
			return True

	def peek(self):
		if self.isEmpty():
			print "Stack is empty!"
			return None
		else:
			return self.bottomNode.number

	def push(self, number, name=None):
		if self.isEmpty():
			self.topNode = Node(number, name)
			self.bottomNode = self.topNode
		else:
			oldNode = self.topNode
			self.topNode = Node(number, oldNode, name)
			oldNode.next = self.topNode

	def pop(self):
		if self.isEmpty():
			print "Stack is empty!"
			return None
		elif self.topNode is self.bottomNode:
			poppedNode = self.topNode
			self.topNode = None
			self.bottomNode = None

			return poppedNode
		else:
			poppedNode = self.bottomNode

			self.bottomNode = self.bottomNode.next
			self.bottomNode.prev = None
			return poppedNode

	def printStack(self):
		node = self.topNode

		while node:
			print str(node)
			node = node.prev

		
class AnimalShelter(object):
	def __init__(self):
		self.catStack = Stack()
		self.dogStack = Stack()
		self.counter = 1

	def enqueue(self, animal=None, name=None):
		if animal != "Dog" and animal != "Cat":
			if randint(0,1) == 0:
				self.animal = "Cat"
			else:
				self.animal = "Dog"
		else:
			self.animal = animal 

		if not name:
			self.name = str(self.counter)
		else:
			self.name = name

		if self.animal == "Cat":
			self.catStack.push(self.counter, name)
		elif self.animal == "Dog":
			self.dogStack.push(self.counter, name)

		self.counter += 1


	def dequeueCat(self):
		if self.catStack.isEmpty():
			print "No cats in the shelter!"
			return None
		else:
			return self.catStack.pop()

	def dequeueDog(self):
		if self.dogStack.isEmpty():
			print "No dogs in the shelter!"
			return None
		else:
			return self.dogStack.pop()


	def dequeueAny(self):
		# Below are in case either or both animals are not present
		if self.catStack.isEmpty() and self.dogStack.isEmpty():
			print "No animals in the shelter!"
			return None
		elif self.catStack.isEmpty():
			return self.dogStack.pop()
		elif self.dogStack.isEmpty():
			return self.catStack.pop()


		# Below is how to find the oldest animal if both are present
		if self.catStack.peek() < self.dogStack.peek():
			return self.catStack.pop()
		elif self.dogStack.peek() < self.catStack.peek():
			return self.dogStack.pop()

		return "Error in DequeueAny!"

	def printShelter(self):
		self.catStack.printStack()
		print "End of Cats"

		self.dogStack.printStack()
		print "End of Dogs"


shelter = AnimalShelter()

for x in xrange(20):
	shelter.enqueue()

shelter.printShelter()

for x in xrange(10):
	shelter.dequeueAny()

shelter.printShelter()

for x in xrange(5):
	shelter.dequeueDog()

for x in xrange(5):
	shelter.dequeueCat()

shelter.printShelter()


