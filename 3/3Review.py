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

#SetofStacks holds each stack in a node in a node linked list stack
#The nodes each hold a stack, the capacity it set at initialization
class SetofStacks(object):

    def __init__(self, capacity = 100):
        self.currentStack = None
        self.capacity = capacity

    def push(self, item):
        if not self.currentStack:
            self.currentStack = self.Node(Stack())
        elif self.currentStack.stack.length >= self.capacity:
            self.currentStack = self.Node(Stack(), self.currentStack)

        self.currentStack.stack.push(item)

    def pop(self):
        if not self.currentStack:
            return None
        elif self.currentStack.stack.isEmpty():
            self.currentStack = self.currentStack.next
            return self.pop()
        else:
            return self.currentStack.stack.pop()

    class Node(object):
        def __init__(self, stack, next = None):
            self.stack = stack 
            self.next = next


s = SetofStacks(25)

for x in xrange(75):
    s.push(x+1)

current = s.currentStack
while current:
    print "Stack:"
    current.stack.printStack()
    current = current.next

for x in xrange(60):
    s.pop()

current = s.currentStack
while current:
    print "Final Stacks:"
    current.stack.printStack()
    current = current.next