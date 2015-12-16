"""
    DFS Function for a directed or undirected graph
    Hector Ramos
    12/13/2015
"""

def dfs(root):
    if not root:
        return None

    root.visited = True
    for node in root.edgeList:
        if not node.visited:
            dfs(node)
    print "Current Node is %s." %str(root.value)


class Node(object):
    def __init__(self, value = None, edgeList = []):
        self.value = value
        self.edgeList = edgeList
        self.visited = None

n0 = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n0.edgeList = [n1, n4, n5]
n1.edgeList = [n3, n4]
n2.edgeList = [n1]
n3.edgeList = [n2, n4]

dfs(n0)
