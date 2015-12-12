"""
    Stack class for a FIFO Stack
    Hector Ramos
    12/9/2015
"""

class Stack(object):

    def __init__(self):
        self.currentNode = None
        self.length = 0

    def push(self, item):
        self.currentNode = self.Node(item, self.currentNode)
        self.length += 1

    def pop(self):
        if not self.currentNode:
            return None

        self.length -= 1
        item = self.currentNode.value
        self.currentNode = self.currentNode.next

        return item

    def peek(self):
        if not self.currentNode:
            return None

        return self.currentNode.value

    def isEmpty(self):
        if self.currentNode:
            return False
        else:
            return True

    def getLength(self):
        return self.length

    def printStack(self):
        if not self.currentNode:
            print "Empty!"

        node = self.currentNode

        while node:
            print node.value
            node = node.next

    class Node(object):
        def __init__(self, value = None, next = None ):
            self.value = value
            self.next = next
