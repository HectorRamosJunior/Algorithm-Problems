"""
        Implement an algorithm to find the kth to last element of a singly linked list
"""

from LinkedList import Node, print_list


#RunnerNode Implementation solution
def findKthLastNode(node, k):
    if not node.next:
        print "List is only one element long"
        return node
    elif k < 1:
        print "Please enter an integer k 1 or larger"
        return node

    counter = 1
    runnerNode = node

    #In the loop below, node stays k elements behind the runner
    while node and runnerNode:
        if not runnerNode.next:
            if counter != k:
                print "List isn't k elements long"
                return node
            else:
                return node

        elif counter != k: #If Runner node not k elements away from node
            runnerNode = runnerNode.next
            counter += 1

        else: #If both conditions not met, move both up
            node = node.next
            runnerNode = runnerNode.next


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
