"""
    How would you design a stack which, in addition to push and pop, 
    has a function min which returns the minimum element? 
    Push, pop, and min should all operate in O(1) time.
"""

from Stack import Stack 

class minStack(Stack):

    def push(self, item):
        self.length += 1

        if not self.currentNode:
            self.currentNode = self.Node(item, item, None)

        else:
            if item < self.currentNode.min:
                nextNode = self.Node(item, item, self.currentNode)
            else:
                nextNode = self.Node(item, self.currentNode.min,
                                                    self.currentNode)

            self.currentNode = nextNode

    def min(self):
        if not self.currentNode:
            return None

        return self.currentNode.min 


    class Node(object):
        def __init__(self, value = None, minimum = None, next = None):
            self.value = value
            self.min = minimum
            self.next = next





s = minStack()

pushList = [10, 6, 5, 11, 0, 20, -1, 2]

for x in pushList:
    s.push(x)

print s.min()


for x in xrange(2):
    s.pop()

print s.min()


for x in xrange(2):
    s.pop()

print s.min()