"""
    Write code to partition a linked list around a value x, such that all 
    nodes less than x come before all nodes greater or equal to x. If x
    is contained within the list, the values of x only need to be after
    the elements less than x. 
    Example: 3>5>8>5>10>2>1 [Pivot: 5] Output : 3>1>2>10>5>5>8
"""

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


from SinglyLinkedList import Node 

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