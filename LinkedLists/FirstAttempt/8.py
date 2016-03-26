"""
    Given a circular linked list, implement an algorithm that returns
    the node at the beginning of the loop.

    Definition: Circular linked lists
    A(corrupt) linked list in which a node's next pointer points to 
    an earlier node, so as to make a loop in the list.

    Example:
    A>B>C>D>E>C (Same C) Output: C
"""

from LinkedList import Node, print_list

def returnLoopedNode(node):
    if not node.next:
        print "Not a circular List!"
        return None
    elif not node.next.next:
        print "Not a circular List!"
        return None

    runnerNode = node.next.next

    while node and runnerNode:
        if node is runnerNode:
            return prevNode
        elif not runnerNode.next:
            print "Not a circular List!"
            return None
        elif not runnerNode.next.next:
            print "Not a circular List!"
            return None
        else:
            prevNode = node
            node = node.next
            runnerNode = runnerNode.next.next


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
node7.next = node3

print returnLoopedNode(node1)