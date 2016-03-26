"""
    Imagine a (literal) stack of plates. If the stack gets too high, 
    it might topple. Therefore, in real life, we would likely start 
    a new stack when the previous exceeds some threshold. Implement a 
    data structure Setofstacks that mimics this. SetofStacks should 
    be composed of several stacks and should create a new stack once 
    the previous one exceeeds capacity. SetofStacks.push() and 
    SetofStacks.pop() should behave identally to a single stack.
    (That is, pop() should return the same values as it would if 
    there was just a single stack.)

    Followup:
    Implement a function popAt(int index) which preforms a pop 
    operation on a specific sub-stack.
"""
from Stack import Stack 

#Added the function popAt to the Stack Class
class Stack(Stack):
    #Zero Indexed!
    def popAt(self, index):
        if index == 0:
            return self.pop()
        elif self.length < (index+1):
            return None 

        counter = 1
        prev = self.currentNode
        current = self.currentNode.next
        
        while current and (counter < index):
            counter += 1
            prev = current
            current = current.next 

        if not current:
            return None 

        prev.next = current.next
        return current.value 


#Uses Stack.popAt(index) to pop from the wanted stack.
#It then pushes the last index of each stack after the index to
#the previous stack before it; keeping them at max capacity
class SetofStacks(object):
    def __init__(self, capacity = 100):
        self.stackList = []
        self.capacity = capacity

    def push(self, item):
        if not self.stackList:
            self.stackList.append(Stack())
            self.push(item)
        elif self.stackList[-1].length == self.capacity:
            self.stackList.append(Stack())
            self.push(item)
        else:
            self.stackList[-1].push(item)

    def pop(self):
        if not self.stackList:
            return None 
        elif self.stackList[-1].isEmpty():
            self.stackList.pop()
            return self.pop()
        else:
            return self.stackList[-1].pop()

    #Zero Indexed!
    def popAt(self, index):
        length = len(self.stackList)

        if length < (index + 1):
            return None
        elif self.stackList[index].isEmpty():
            return None
        elif (index+1) == length:
            return self.pop()
        else:
            self.stackList[index].pop()

            for i in xrange(index + 1, length):
                last = self.stackList[i].length - 1    #Zero Indexed
                popped = self.stackList[i].popAt(last)

                if not popped:
                    self.stackList.pop()            #Pop Empty Stack
                else:
                    self.stackList[i-1].push(popped) 


s =  SetofStacks(5) #stack capacity set to 0 

for x in xrange(15):
    s.push(x+1)

s.popAt(0)

for stack in s.stackList:
    print "Stack:"
    stack.printStack()

s.popAt(2)

print 
for stack in s.stackList:
    print "Stack:"
    stack.printStack()





