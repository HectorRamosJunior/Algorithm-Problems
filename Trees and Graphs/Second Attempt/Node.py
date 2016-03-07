"""
    Node Class for Binary Trees
    Hector Ramos
    12/9/2015
"""

class Node(object):
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left 
        self.right = right
        self.parent = None

    def printTree(self):
        print self.value

        if self.left:
            self.left.printTree()
        if self.right:
            self.right.printTree()

    def __str__(self):
        return "Node with value: %s" % self.value