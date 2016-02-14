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

#Sums lists using recursion, assumes digit next digit is the largest
def sumLists(list1Node, list2Node, carry = 0):
    if not (list1Node or list2Node or carry > 0):
        return None

    sumNode = Node(carry)
    list1Next = None
    list2Next = None 

    #Add the listNode only if necessary, this handles varying lengths
    if list1Node:
        sumNode.value += list1Node.value
        list1Next = list1Node.next 
    if list2Node:
        sumNode.value += list2Node.value
        list2Next = list2Node.next

    carry = sumNode.value/10
    sumNode.value = sumNode.value%10

    #hands off carry and next nodes of both lists recursively
    nextSumNode = sumLists(list1Next, list2Next, carry)
    #After node is received, take current node and put in front
    sumNode.next = nextSumNode

    return sumNode


list1 = Node(9, Node(2, Node(6)))
list2 = Node(1, Node(7, Node(6, Node(9))))

sumLists(list1, list2).printList()