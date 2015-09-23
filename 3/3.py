"""
    Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
    Therefore, in real life, we would likely start a new stack when the previous exceeds some threshold.
    Implement a data structure Setofstacks that mimics this. SetofStacks should be composed of several
    stacks and should create a new stack once the previous one exceeeds capacity. 
    SetofStacks.push() and SetofStacks.pop() should behave identally to a single stack.
    (That is, pop() should return the same values as it would if there was just a single stack.)
    Followup:
    Implement a function popAt(int index) which preforms a pop operation on a specific sub-stack.
"""

class Node(object):
    def __init__(self, data=None, prev=None):
        self.data = data
        self.prev = prev


class Stack(object):
    def __init__(self, prev=None):
        self.prev = prev
        self.firstNode = None
        self.lastNode = None
        self.empty = True

    def push(self, data):
        if self.empty:
            self.firstNode = Node(data)
            self.lastNode = self.firstNode
            self.empty = False
        else:
            self.lastNode = Node(data, self.lastNode)

    def pop(self):
        if self.empty:
            print "Empty Stack!"
        elif self.lastNode is self.firstNode:
            self.firstNode = None
            self.lastNode = None
            self.empty = True
        else:
            self.lastNode = self.lastNode.prev

    def printStack(self):
        lastNode = self.lastNode
        while lastNode:
            print str(lastNode.data)
            lastNode = lastNode.prev
        print "End of Stack, printed last nodes first"



class SetofStacks(object):
    def __init__(self):
        self.firstStack = None
        self.lastStack = None
        self.empty = True
        self.nodeCount = 0
        self.stackCount = 0

    def push(self, data):
        if self.empty:
            self.firstStack = Stack()
            self.lastStack = self.firstStack
            self.empty = False
            self.lastStack.push(data)
            self.nodeCount += 1
            self.stackCount += 1
        elif self.nodeCount == 100:
            self.lastStack = Stack(self.lastStack)
            self.lastStack.push(data)
            self.nodeCount = 1
            self.stackCount += 1
        else:
            self.lastStack.push(data)
            self.nodeCount += 1

    def pop(self):
        if self.empty:
            print "Empty set!"
        elif self.nodeCount == 1:
            if self.lastStack.prev:
                self.lastStack = self.lastStack.prev
                self.nodeCount = 100
                self.stackCount -= 1
            else:
                self.firstStack = None
                self.lastStack = None
                self.empty = True
                self.nodeCount = 0
                self.stackCount = 0
        else:
            self.lastStack.pop()
            self.nodeCount -= 1

    def printSetofStacks(self):
        lastStack = self.lastStack

        while lastStack:
            lastStack.printStack()
            lastStack = lastStack.prev



set1 = SetofStacks()

for x in xrange(200):
    set1.push(x+1)

set1.printSetofStacks()

for y in xrange(120):
    set1.pop()

set1.printSetofStacks()





