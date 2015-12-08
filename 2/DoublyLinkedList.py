"""
    Node class for Doubly Linked Lists
    Hector Ramos
    12/7/2015
"""

class Node(object):

    def __init__(self, value = None, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next
        self.visited = False

    def __str__(self):
        return "This node's value is %s." %str(self.value)


    def printList(self, direction = "forward"):
        print "Printing list %s." %direction
        print self

        if direction == "forward":
            node = self.next

            while node:
                print node
                node = node.next

        elif direction == "backward":
            node = self.prev

            while node:
                print node
                node = node.prev

        print 


