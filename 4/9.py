'''
    BST Sequences: 
    A binary search tree was created by traversing through an array from
    left to right and inserting each element. Given a binary search tree
    with distinct elements, print all possible arrays that could have led
    to this tree.
'''

class Node(object):
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

def getSequences(root):
    if not root:
        return None

    left = getSequences(root.left)
    right = getSequences(root.right)
    results = []

    if left and right:
        for l in left:
            for r in right:
                results += combineLists(left, right, root.data)

    elif left and not right:
        for l in left:
            results += combineLists(left, right, root.data)

    elif right and not left:
        for r in right:
            results += combineLists(left right, root.data)

    else:
        return [root.data]

    return results


def combineLists(left, right, prefix):
