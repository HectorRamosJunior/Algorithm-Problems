"""
		Write code to remove duplicates from an unsorted linked list. 
		Followup:
		How would you solve this without a tempbuffer?
"""

from LinkedList import Node, print_list

def removeListDuplicates(node):
	if not node.next:
		print "Unlinked list!"

	dataDict = {}
	dataDict[str(node)] = True
	prevNode = node
	node = node.next

	while(node):
		if str(node) in dataDict:
			print "Removing" + str(node)
			prevNode.next = node.next
		else:
			dataDict[str(node)] = True
			prevNode = node 
		node = node.next


node1 = Node(1)
node2 = Node(2)
node1.next = node2
node3 = Node(3)
node2.next = node3
node4 = Node(2)
node3.next = node4
node5 = Node(5)
node4.next = node5
node6 = Node(1)
node5.next = node6
node7 = Node(7)
node6.next = node7

print_list(node1)
removeListDuplicates(node1)
print_list(node1)
