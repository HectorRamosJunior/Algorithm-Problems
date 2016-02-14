"""
    How would you design a stack which, in addition to push and pop, 
    has a function min which returns the minimum element? 
    Push, pop, and min should all operate in O(1) time.
"""
#The stack is assumed to be a Last In First Out stack, so this node is needed
class Node(object):
    def __init__(self, data=None, minValue=None, prev=None):
        self.data = data
        self.minValue = minValue
        self.prev = prev


#Implements a LIFO stack implementing a linked list. 
#Each node stores the local min of the nodes before it
#If the pop occurs and the local and global mins are the same,
#The global min is changed to the new local min of the current last node
class minStack(object):

    def __init__(self, data):
        self.firstNode = Node(data)
        self.minValue = self.firstNode.data
        self.lastNode = self.firstNode
        self.empty = False

    def push(self, data):
        if self.empty:
            self.firstNode = Node(data)
            self.minValue = self.firstNode.data
            self.lastNode = self.firstNode
            self.empty = False
        else:
            self.lastNode = Node(data, self.minValue, self.lastNode)
            if self.lastNode.data < self.minValue:
                self.minValue = self.lastNode.data

    def pop(self):
        if self.empty:
            print "Empty Stack! Nothing to pop!"
        elif self.firstNode is self.lastNode:
            self.firstNode = None
            self.lastNode = None
            self.minValue = None
            self.empty = True
        else:
            if self.minValue == self.lastNode.data:
                self.minValue = self.lastNode.minValue
            self.lastNode = self.lastNode.prev

    def getMin(self):
        return self.minValue

    def isEmpty(self):
        return self.empty

    def printStack(self):
        lastNode = self.lastNode
        while lastNode:
            print str(lastNode.data)
            lastNode = lastNode.prev
        print "End of Stack, printed last nodes first"


stack1 = minStack(10)
stack1.printStack()
stack1.push(5)
stack1.push(51)
stack1.push(16)
stack1.push(39)
stack1.push(100)
stack1.push(0)
stack1.push(5)
stack1.printStack()

print "The min value is " + str(stack1.getMin())

stack1.pop()
stack1.pop()
stack1.printStack()
print "The min value is " + str(stack1.getMin())

stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()
stack1.printStack()
print "The stack being empty is: " + str(stack1.isEmpty())

