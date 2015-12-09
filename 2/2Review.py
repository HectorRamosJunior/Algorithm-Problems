"""
        Implement an algorithm to find the kth to last element 
        of a singly linked list.
"""
from SinglyLinkedList import Node

#Uses a runner node k elements ahead; when runnerNode stops
#The slow node will have reached the kth element desired
def kthLastElement(root, k):
    if k < 1:
        return None

    runnerNode = root

    for x in xrange(k-1):
        runnerNode = runnerNode.next
        if not runnerNode:
            return None


    while True:
        if not runnerNode.next:
            return root 
        else:
            runnerNode = runnerNode.next
            root = root.next



headNode = Node(1, Node(2,
                    Node(3, 
                        Node(4,
                            Node(5,
                                Node(6,
                                    Node(7)))))))

headNode.printList()

print kthLastElement(headNode, 0)
print kthLastElement(headNode, 1)
print kthLastElement(headNode, 6)
print kthLastElement(headNode, 10)
