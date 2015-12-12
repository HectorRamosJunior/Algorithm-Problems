"""
    Queue class for a LIFO Stack
    Hector Ramos
    12/9/2015
"""

class Queue(object):

    def __init__(self):
        self.firstNode = None
        self.lastNode = None
        self.length = 0

    def add(self, item):
        self.length += 1

        if not self.lastNode:
            self.lastNode = self.Node(item)
            self.firstNode = self.lastNode
        else:
            self.lastNode.next = self.Node(item)
            self.lastNode = self.lastNode.next 

    def remove(self):
        if not self.firstNode:
            return None

        self.length -= 1
        item = self.firstNode.value

        if self.firstNode is self.lastNode:
            self.lastNode = None

        self.firstNode = self.firstNode.next

        return item

    def peek(self):
        if self.firstNode:
            return self.firstNode.value
        else:
            return None

    def isEmpty(self):
        if self.firstNode:
            return False
        else:
            return True

    def getLength(self):
        return self.length

    def printQueue(self):
        if not self.firstNode:
            return "Empty!"

        node = self.firstNode

        while node:
            print node.value
            node = node.next

    class Node(object):
        def __init__(self, value = None, next = None):
            self.value = value
            self.next = next