"""
    Node class for Singly Linked Lists
    Hector Ramos
    12/7/2015
"""

class Node(object):

    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
        self.visited = False

    def __str__(self):
        return "Node's value is %s." %str(self.value)


    def printList(self):
        print "Printing list:"
        print self

        node = self.next
        while node:
            print node
            node = node.next

        print 

    def getListLength(self):
        length = 1

        node = self.next
        while node:
            length += 1 
            node = node.next

        return length


