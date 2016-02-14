"""
    You have two numbers represented by a linked list, where each node 
    contains a single digit. The digits are stored in reverse order, 
    such that the 1's digit is at the head of the list. Write a function 
    that adds the two numbers and returns the sum as a linked list.
    EX: (7>1>6) + (5>9>2) = 617+295  Output: 2>1>9 (912)
    Followup:
    Suppose the digits are stored in forward order. Repeat the problem.
    EX: (6>1>7) + (2>9>5) = 617+295 Output: 9>1>2 (912)
"""
from SinglyLinkedList import Node

#More or less the main function which oversees the __add and padLists
def sumLists(list1Node, list2Node):
    #Adds 0's to the front of the shorter list (necessary)
    (node1, node2) = padLists(list1Node, list2Node)

    #Generates the summed list
    (sumListNode, carry) = __sumLists(node1, node2)

    #Appends carry node to front of linked list if necessary
    if carry > 0:
        return Node(carry, sumListNode)
    else:
        return sumListNode


#Recursive call, returns tuple: (headNode, carry)
def __sumLists(node1, node2):
    if not(node1 and node2):
        return (None, 0) 


    (sumListNode, carry) = __sumLists(node1.next, node2.next)

    sumValue = node1.value + node2.value + carry
    carry = sumValue / 10
    sumValue = sumValue % 10

    return (Node(sumValue, sumListNode), carry)


#Adds 0's to the front of the shorter list to match lengths
def padLists(list1, list2):
    length1 = list1.getListLength()
    length2 = list2.getListLength()


    headNode = None
    node = None
    for x in xrange(abs(length1 - length2)):
        if not headNode:
            headNode = Node(0)
            node = headNode
        else:
            node.next = Node(0)
            node = node.next

    if length1 < length2:
        node.next = list1 
        return (headNode, list2)
    elif length1 > length2:
        node.next = list2 
        return (list1, headNode)
    else:
        return (list1, list2)



list1 = Node(9, Node(2, Node(6)))
list2 = Node(1, Node(7, Node(6, Node(9))))

sumLists(list1, list2).printList()