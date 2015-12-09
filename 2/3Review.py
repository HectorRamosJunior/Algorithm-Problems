"""
        Implement an algorithm to delete a node in the middle of 
        a singly linked list given access only to that node
"""
from SinglyLinkedList import Node

#A cute trick, just copies the next node in the list
#removes the next node in the list, "deletes" itself
def removeNode(node):
    if node.next:
        node.value = node.next.value
        node.next = node.next.next
    else:
        return None


headNode = Node(1, Node(2,
                    Node(3, 
                        Node(4,
                            Node(5,
                                Node(6))))))

middleNode = headNode

for x in xrange(3):
    middleNode = middleNode.next
print middleNode

headNode.printList()
removeNode(middleNode)
headNode.printList()
