"""
    Imagine a (literal) stack of plates. If the stack gets too high, 
    it might topple. Therefore, in real life, we would likely start 
    a new stack when the previous exceeds some threshold. Implement a 
    data structure Setofstacks that mimics this. SetofStacks should 
    be composed of several stacks and should create a new stack once 
    the previous one exceeeds capacity. SetofStacks.push() and 
    SetofStacks.pop() should behave identally to a single stack.
    (That is, pop() should return the same values as it would if 
    there was just a single stack.)

    Followup:
    Implement a function popAt(int index) which preforms a pop 
    operation on a specific sub-stack.
"""
from Stack import Stack 

class SetofStacks(object):

    def __init__(self, capacity = 100):
        self.currentNode = None
        self.capacity = capacity

    def push(self, item):
        if not self.currentNode:
            self.currentNode = self.Node(Stack())
        elif self.currentNode.stack.length >= self.capacity:
            self.currentNode = self.Node(Stack(), self.currentNode)

        self.currentNode.stack.push(item)

    def pop(self):
        if not self.currentNode:
            return None
        elif self.currentNode.stack.isEmpty():
            self.currentNode = self.currentNode.next
            return self.pop()
        else:
            return self.currentNode.stack.pop()

    class Node(object):
        def __init__(self, stack, next = None):
            self.stack = stack 
            self.next = next


s = SetofStacks()

for x in xrange(300):
    s.push(x+1)

current = s.currentNode
while current:
    print "Stack:"
    current.stack.printStack()
    current = current.next

for x in xrange(190):
    s.pop()

current = s.currentNode
while current:
    print "Stack:"
    current.stack.printStack()
    current = current.next