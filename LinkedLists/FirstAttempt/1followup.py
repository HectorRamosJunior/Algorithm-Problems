"""
    Write code to remove duplicates from an unsorted linked list. 
    Followup:
    How would you solve this without a tempbuffer?
"""

from LinkedList import Node, print_list

#Function uses two pointers to iterate through the list
#This is to avoid using another temp data structure
def removeListDuplicates(node1):
  if not node1.next:
    print "Unlinked list!"
    return node1

  #Outerloop keeps track of the item to check duplicates against
  while(node1):
    prevNode2 = node1
    node2 = node1.next #node2 always starts a step ahead of node1

    #node2 is the searching node, runs through the list ahead of node1
    while(node2):
      if(node1.data == node2.data):
        print "Removing " + str(node2)
        prevNode2.next = node2.next
      else:
        prevNode2 = node2

      node2 = node2.next
    node1 = node1.next

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