"""
    Given two singly linked lists, determine if the two lists intersect.
    Return the intersecting node. Note that the intersection is defined
    based on reference, not value. That is, the kth node of the first linked
    list is the same exact node (by reference) as the jth node of the
    second linked list, then they are intersecting.
"""

from LinkedList import Node, print_list

def returnIntersectingNode(node1, node2):
    if not (node1.next and node2.next):
        print "One of the entered lists is only one node long!"
        return None

    listLength1 = getListLength(node1)
    listLength2 = getListLength(node2)

    if listLength1 > listLength2:
        longNode = node1
        shortNode = node2
    elif listLength2 > listLength1: 
        longNode = node2
        shortNode = node1
    
    listsDifference = abs(listLength2 - listLength1)

    while listsDifference != 0:
        longNode = longNode.next
        listsDifference -= 1

    while longNode and shortNode:
        if longNode is shortNode:
            return longNode
        else:
            longNode = longNode.next   
            shortNode = shortNode.next

    return False

def getListLength(node):
    counter = 0
    while node:
        counter += 1
        node = node.next

    return counter

nodeOne1 = Node(7)
nodeOne2 = Node(1)
nodeOne1.next = nodeOne2
nodeOne3 = Node(6)
nodeOne2.next = nodeOne3

nodeTwo1 = Node(5)
nodeTwo2 = Node(9)
nodeTwo1.next = nodeTwo2
nodeTwo3 = Node(2)
nodeTwo2.next = nodeTwo3

nodeOne1.next = nodeTwo1


answerNode = returnIntersectingNode(nodeOne1, nodeTwo1)
print_list(answerNode)