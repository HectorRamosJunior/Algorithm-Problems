'''
    First Common Ancestor: 
    Design an algorithm and write code to find the first common ancestor
    of two nodes in a binary tree. Avoid storing additional nodes in a
    data structure. NOTE: This is not necessarily a BST.
'''

class CommonAncestor(object):
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.n1Found = False
        self.n2Found = False

    def findAncestor(self):
        result = self.findAncestorHelper()
        if result:
            if self.n1Found and self.n2Found:
                return result
        else:
            return None

    def findAncestorHelper(self, root):
        if root.left:
            left = self.findAncestorHelper(root.left)
        if root.right:
            right = self.findAncestorHelper(root.right)

        if self.n1 is root:
            self.n1Found = True
            return root
        elif self.n2 is root:
            self.n2Found = True
        else:
            if left and right:
                return root
            elif left:
                return left
            elif right:
                return right
            else:
                return None