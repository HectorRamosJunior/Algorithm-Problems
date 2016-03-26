"""
    Given a directed graph, design an algorithm to find out
    whether there is a route between two nodes.
"""

#Runs a bidirectional bfs search from each root
#Checks if the root's bfs visited a node touched by the other's bfs
def routeBetweenNodes(root1, root2):
    q1 = [root1] 
    q2 = [root2]
    root1.visited1 = True
    root2.visited2 = True

    while q1 and q2:
        node1 = q1.pop(0)
        node2 = q2.pop(0)

        for n in node1.edgeList:
            if n.visited2:
                return True
            elif not n.visited1:
                q1.append(n)
                n.visited1 = True

        for n in node2.edgeList:
            if n.visited1:
                return True
            elif not n.visited2:
                q2.append(n)
                n.visited2 = True

    return False

#Contains visited1 and visited2 to keep track what root's 
#bfs has already visisted the given node
class Node(object):
    def __init__(self, value = None, edgeList = []):
        self.value = None
        self.edgeList = edgeList
        self.visited1 = False
        self.visited2 = False


n0 = Node(0); n1 = Node(1)
n2 = Node(2); n3 = Node(3)
n4 = Node(4); n5 = Node(5)

n0.edgeList = [n1, n4, n5]
n1.edgeList = [n3, n4]
n2.edgeList = [n1]
n3.edgeList = [n2, n4]

print routeBetweenNodes(n2, n5)
print routeBetweenNodes(n0, n2)


