"""
		Implement an algorithm to find the kth to last element of a singly linked list
"""

from LinkedList import Node, print_list

def findKthLastNode(node, k):
  if k == 0:
    print "No such thing as 0th to last Node! Try 1 instead."
    return None
  elif not node.next:
    print "No node beyond the first in this list!"
    return None

  kthArray = []

  while(node):
    if len(kthArray) == k:
      kthArray.insert(0, node.data)
      kthArray.pop(k)
    else:
      kthArray.insert(0, node.data)

    node = node.next

  print kthArray
  if len(kthArray) != k:
    print "List too short!!"
    return None

  return kthArray[k-1]

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
print findKthLastNode(node1, 4)
