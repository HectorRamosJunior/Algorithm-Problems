"""
    Given two singly linked lists, determine if the two lists intersect.
    Return the intersecting node. Note that the intersection is defined
    based on reference, not value. That is, the kth node of the first 
    linked list is the same exact node (by reference) as the jth node 
    of the second linked list, then they are intersecting.
"""
from SinglyLinkedList import Node


def getInsersectingNode(list1, list2):
    (length1, lastNode1) = getLastNode(list1)
    (length2, lastNode2) = getLastNode(list2)

    #If the last nodes aren't the same, they don't intersect
    if not (lastNode1 is lastNode2):
        return None


    #The longer list needs to be pushed to be the same length
    if length1 > length2:
        for x in xrange(length1 - length2):
            list1 = list1.next
    elif length1 < length2:
        for x in xrange(length2 - length1):
            list2 = list2.next

    #Iterate through both lists checking if the node is the same
    while list1 and list2:
        if list1 is list2:
            return list1

        list1 = list1.next
        list2 = list2.next

    #This return shouldn't happen
    return "Error!" #Error


#Returns the lastNode of the list with the list length
def getLastNode(headNode):
    if not headNode:
        return (0, None) #length, lastNode

    length = 1
    while headNode.next:
        length += 1
        headNode = headNode.next

    return (length, headNode)


headNode1 = Node(4, Node(3, Node(2, Node(1))))
headNode2 = Node(7, Node(6, Node(5, headNode1)))

print getInsersectingNode(headNode1, headNode2)
print getInsersectingNode(headNode2, headNode1)

headNode3 = Node(1, Node(2, Node(3, Node(4))))

print getInsersectingNode(headNode1, headNode3)