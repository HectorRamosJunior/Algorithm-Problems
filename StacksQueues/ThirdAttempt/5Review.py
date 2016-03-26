"""
    Write a program to sort a stack such that the smallest items are on 
    the top. You can use an additional temporary stack, but you may not 
    copy the elements into any other data structure. (Such as an array). 
    The stack suppors the following operations: push, pop, peek, isEmpty.
"""
from Stack import Stack 


#Uses one variable to hold onto the max node and place it at 
#the bottom of the stack. Then the second iteration does the same 
#but goes to the second to last element instead (last node is the max)
#Repeat until stack is sorted from smallest to biggest
def sortStack(stack):
    depth = getDepth(stack)
    unsorted = depth 
    tempStack = Stack()

    for i in xrange(depth):
        localMax = None
        counter = 0

        while counter < unsorted:
            if not localMax:
                localMax = stack.pop()
            elif stack.peek() > localMax:
                tempStack.push(localMax)
                localMax = stack.pop()
            else:
                tempStack.push(stack.pop())

            counter += 1


        stack.push(localMax)
        while not tempStack.isEmpty():
            stack.push(tempStack.pop())

        unsorted -= 1

def getDepth(stack):
    depth = 0
    tempStack = Stack()

    while not stack.isEmpty():
        depth += 1
        tempStack.push(stack.pop())

    while not tempStack.isEmpty():
        stack.push(tempStack.pop())

    return depth      



s = Stack()

pushList = [10, 5, 8, 32, 0, 50, 100, -8]          
[s.push(x) for x in pushList]

s.printStack()
sortStack(s)

print "\nSorted:"
s.printStack()