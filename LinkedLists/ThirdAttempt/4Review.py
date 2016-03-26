"""
    Write code to partition a linked list around a value x, such that all 
    nodes less than x come before all nodes greater or equal to x. If x
    is contained within the list, the values of x only need to be after
    the elements less than x. 
    Example: 3>5>8>5>10>2>1 [Pivot: 5] Output : 3>1>2>10>5>5>8
"""
from SinglyLinkedList import Node

#Forms two stacks while iterating the list:
#Elements smaller than the pivot, and elements greater or equal the pivot
#Then appends the smaller list to the bigger list (if both available) 
def partitionList(root, pivot):
    leftHeadNode = None
    rightHeadNode = None
    leftNode = None
    rightNode = None


    while root:
        if root.value < pivot:
            if not leftHeadNode:
                leftHeadNode = root
                leftNode = root
            else:
                leftNode.next = root
                leftNode = leftNode.next

        else:
            if not rightHeadNode:
                rightHeadNode = root
                rightNode = root
            else: 
                rightNode.next = root
                rightNode = rightNode.next

        root = root.next

    if rightNode:
        rightNode.next = None

    if leftHeadNode:
        leftNode.next = rightHeadNode

        return leftHeadNode
    else:
        return  rightHeadNode



headNode = Node(10, Node(1,
                Node(6,
                    Node(4,
                        Node(8,
                            Node(5,
                                Node(2,
                                    Node(9,
                                        Node(0)))))))))

headNode.printList()

partitionList(headNode, 5).printList()