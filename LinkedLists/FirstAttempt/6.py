"""
    Implement a function to check if a linked list is a palindrome
"""

from LinkedList import Node, print_list

def checkListPalindrome(node):
    if not node.next:
        print "List is only one node!"
        return False

    charArray = []
    while node:
        charArray.append(str(node))
        node = node.next

    for i in xrange(len(charArray)/2):
        if charArray[0+i] != charArray[len(charArray) - 1 - i]:
            return False

    return True

node1 = Node("r")
node2 = Node("a")
node1.next = node2
node3 = Node("c")
node2.next = node3
node4 = Node("e")
node3.next = node4
node5 = Node("c")
node4.next = node5
node6 = Node("a")
node5.next = node6
node7 = Node("r")
node6.next = node7

print_list(node1)
print checkListPalindrome(node1)
