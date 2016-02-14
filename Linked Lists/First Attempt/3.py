"""
		Implement an algorithm to delete a node in the middle of 
        a singly linked list given access only to that node
"""

from LinkedList import Node, print_list


def removeNodeFromList(node):
    if node.next:
        nextNode = node.next
        print "Deleted Node containing " + str(node)
        node.data = nextNode.data
        node.next = nextNode.next

    else:
        print "Can't delete currentnode, since it is the last in the list."


node1 = Node(1)
node2 = Node(2)
node1.next = node2
node3 = Node(3)
node2.next = node3
node4 = Node(4)
node3.next = node4
node5 = Node(5)
node4.next = node5
node6 = Node(6)
node5.next = node6
node7 = Node(7)
node6.next = node7

print_list(node1)
print removeNodeFromList(node6)
print_list(node1)
