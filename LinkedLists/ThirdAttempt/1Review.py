"""
        Write code to remove duplicates from an unsorted linked list. 
        Followup:
        How would you solve this without a tempbuffer?
"""
from SinglyLinkedList import Node

#Iterates through list, uses hash set for value
def removeDuplicates(root):
    hashSet = set()
    hashSet.add(root.value)

    node = root.next
    prevNode = root

    while node:
        if node.value in hashSet:
            prevNode.next = node.next
        else:
            hashSet.add(node.value)
            prevNode = prevNode.next

        node = node.next

#Checks every element in list against the currentNode
#Using a nested while loop
def removeDuplicates2(root):
    while root:
        runnerNode = root.next
        prevNode = root

        while runnerNode:
            if root.value == runnerNode.value:
                prevNode.next = runnerNode.next
            else:
                prevNode = prevNode.next

            runnerNode = runnerNode.next

        root = root.next



headNode = Node(1, Node(2, 
                    Node(3, 
                        Node(2, 
                            Node(1, 
                                Node(5))))))

headNode2 = Node(1, Node(2, 
                    Node(3, 
                        Node(2, 
                            Node(1, 
                                Node(5))))))


headNode.printList()
removeDuplicates(headNode)
removeDuplicates2(headNode2)

headNode.printList()
headNode2.printList()

