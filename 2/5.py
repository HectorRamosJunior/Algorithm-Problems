"""
	You have two numbers represented by a linked list, where each node contains a single digit.
	The digits are stored in reverse order, such that the 1's digit is at the head of the list.
	Write a function that adds the two numbers and returns the sum as a linked list.
	EX: (7>1>6) + (5>9>2) = 617+295  Output: 2>1>9 (912)
"""

from LinkedList import Node, print_list


def addFunkyLists(node1,node2):
	total1 = getListSum(node1)
	total2 = getListSum(node2)
	total = total1 + total2
	print total #Check

	digitPlace = 1 #start at the ones digit
	if total < digitPlace: #Assumes only POSITIVE integers!
		return Node(total)


	currentNode = False #will be set to true along with the headNode
	while digitPlace <= total:
		newDigit = total % (digitPlace*10) #Removes unwanted digits to the left
		newDigit = (newDigit) / digitPlace #Removes unwanted digits to the right

		if currentNode:
			newNode = Node(newDigit)
			currentNode.next = newNode
			currentNode = currentNode.next

		else:
			currentNode = Node(newDigit)
			headNode = currentNode

		digitPlace = digitPlace*10

	return headNode


#Function adds the digits of the nodes in a list starting from the head
#The digit place is used for keeping the node's value in the proper digit
def getListSum(node):
	total = 0
	digitPlace = 1

	while node:
		total = total + node.data*digitPlace
		digitPlace = digitPlace*10
		node = node.next

	return total



nodeOne1 = Node(7)
nodeOne2 = Node(1)
nodeOne1.next = nodeOne2
nodeOne3 = Node(6)
nodeOne2.next = nodeOne3

nodeTwo1 = Node(5)
nodeTwo2 = Node(9)
nodeTwo1.next = nodeTwo2
nodeTwo3 = Node(2)
nodeTwo2.next = nodeTwo3


answerHeadNode = addFunkyLists(nodeOne1, nodeTwo1)
print_list(answerHeadNode)
