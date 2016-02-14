"""
    BFS Function for a directed or undirected graph
    Hector Ramos
    12/13/2015
"""

def bfs(root):
    if not root:
        return None

    q = []
    q.append(root)
    root.visited = True

    while q:
        node = q.pop(0)
        print "Currently at %s" %str(node.value) 

        for n in node.edgeList:
            if not n.visited:
                q.append(n)
                n.visited = True


class Node(object):
    def __init__(self, value = None, edgeList = []):
        self.value = value
        self.edgeList = edgeList
        self.visited = None


n0 = Node(0); n1 = Node(1)
n2 = Node(2); n3 = Node(3)
n4 = Node(4); n5 = Node(5)

n0.edgeList = [n1, n4, n5]
n1.edgeList = [n3, n4]
n2.edgeList = [n1]
n3.edgeList = [n2, n4]

bfs(n0)
