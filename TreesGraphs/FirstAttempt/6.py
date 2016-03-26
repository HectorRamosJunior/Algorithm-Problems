'''
    Successor: 
    Write an algorithm to find the "next" node (i.e., in order Successor)
    of a given node in a binary search tree. You may assume that each 
    node has a link to its parent.
'''

class Node(object):
    def __init__(self, data = None, parent = None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None


    def makeChildren(self, leftNode = None, rightNode = None):
        if leftNode:
            self.left = leftNode
            leftNode.parent = self
        if rightNode:
            self.right = rightNode
            rightNode.parent = self


def getSuccessor(root):
    if root.left:
        return root.left
    elif root.right:
        return root.right
    elif not root.parent:
        return "No successor available"
    elif root.parent.left is root:
        return root.parent
    else:
        isRight = True

        while isRight:
            if root.parent:
                if root.parent.left == root:
                    return root.parent
                else:
                    root = root.parent
        
        return "No successor available."