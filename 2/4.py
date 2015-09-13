"""
    Write code to partition a linked list around a value x, such that all 
    nodes less than x come before all nodes greater or equal to x. If x
    is contained within the list, the values of x only need to be after
    the elements less than x. 
    Example: 3>5>8>10>2>1 [Pivot: 5] Output : 3>1>2>10>5>5>8
"""

from LinkedList import Node, print_list

def partitionList(node, pivot):
    if not node.next:
        print "List is only one node long!"
        return node


    leftNode = False
    rightNode = False

    while node:
        newNode = Node(node.data)

        if newNode.data < pivot:
            if not leftNode:
                leftHeadNode = newNode
                leftNode = newNode
            elif leftNode:
                leftNode.next = newNode
                leftNode = leftNode.next

        elif newNode.data >= pivot:
            if not rightNode:
                rightHeadNode = newNode
                rightNode = newNode
            elif rightNode:
                rightNode.next = newNode
                rightNode = rightNode.next

        node = node.next

    if not leftNode:
        print "No values in list smaller than the pivot!"
        return rightHeadNode
    elif not rightNode:
        print "No values greater or equal to the pivot in list!"
        return leftHeadNode
    else:
        leftNode.next = rightHeadNode
        return leftHeadNode


node1 = Node(10)
node2 = Node(2)
node1.next = node2
node3 = Node(65416)
node2.next = node3
node4 = Node(111)
node3.next = node4
node5 = Node(0)
node4.next = node5
node6 = Node(6)
node5.next = node6
node7 = Node(5)
node6.next = node7

print "Original List" 
print_list(node1)

print "Partitioned List"
print_list(partitionList(node1, 11))
