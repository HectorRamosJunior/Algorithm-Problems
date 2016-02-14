"""
    Implement a function to check if a linked list is a palindrome
"""
from SinglyLinkedList import Node

#Makes a new linked list that is the reverse of the input list
#Then iterates through both checking if they are equal
def isPalindrome(headNode):
    if not headNode.next:
        return False

    node = headNode
    reversedHeadNode = None

    while node:
        reversedHeadNode = Node(node.value, reversedHeadNode)
        node = node.next 

    while headNode and reversedHeadNode:
        if headNode.value != reversedHeadNode.value:
            return False

        reversedHeadNode = reversedHeadNode.next
        headNode = headNode.next

    return True


#Uses the slow and fast runner Node method to find the middle
#of the list. Once found, it compares the slow node iteration
#vs the stack [palindromes are the same going left and right
#from the middle character]
def isPalindrome2(headNode):
    if not headNode.next:
        return False

    slowNode = headNode 
    runnerNode = headNode
    palindromeList = [] #Stack of characters "left from the middle"

    #Finds middle character, appends left characters to stack
    while (runnerNode and runnerNode.next):
        palindromeList.append(slowNode.value)
        slowNode = slowNode.next
        runnerNode = runnerNode.next.next 

    if runnerNode: #If odd, the middle character doesn't "count"
        slowNode = slowNode.next


    #Checks if the left and right characters from the middle are 
    #equal iteratively, to see if the list is a palindrome
    while slowNode:
        if palindromeList.pop() != slowNode.value:
            return False

        headNode = headNode.next
        slowNode = slowNode.next

    return True 






headNode1 = Node("r", Node("a",
                        Node("c",
                            Node("e",
                                Node("c",
                                    Node("a",
                                        Node("r")))))))

headNode2 = Node("h", Node("e",
                        Node("c",
                            Node("t",
                                Node("o",
                                    Node("r"))))))

headNode3 = Node(1, Node(2, Node(2, Node(1))))
headNode4 = Node(1, Node(1))


print "Function 1"
print isPalindrome(headNode1)
print isPalindrome(headNode2)
print isPalindrome(headNode3)
print isPalindrome(headNode4) , "\n"

print "Function 2"
print isPalindrome2(headNode1)
print isPalindrome2(headNode2)
print isPalindrome2(headNode3)
print isPalindrome2(headNode4)
