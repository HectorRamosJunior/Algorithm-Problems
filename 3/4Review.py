"""
    Implement a MyQueue class which implements a queue using two stacks.

    Make the functions peek, add, remove, size.
"""
from Stack import Stack 

class Queue(object):

    def __init__(self):
        self.newStack = Stack()
        self.oldStack = Stack()

    def add(self, item):
        self.newStack.push(item)

    def remove(self):
        if self.oldStack.isEmpty():
            self.transferStacks()

        return self.oldStack.pop()

    def peek(self):
        if self.oldStack.isEmpty():
            self.transferStacks()

        return self.oldStack.pop()

    def transferStacks(self):
        while not self.newStack.isEmpty():
            popped = self.newStack.pop()
            self.oldStack.push(popped)


q = Queue()

[q.add(x+1) for x in xrange(10)]
for x in xrange(5):
    print q.remove()

print "\n"
[q.add(x) for x in xrange(11,100)]
for x in xrange(10):
    print q.remove()


