'''
    Check Balanced:
    Implement a function to check if a binary tree is balanced.
    For the purposes of this question, a balanced tree is defined 
    to be a tree such that the heights of the two subtrees of any 
    node never differ by more than one.
'''
from Node import Node 


def checkBalanced(root):
    currentHeight = [root]
    depthCounter = 0

    #Tracks if the tree is a complete binary tree 
    completeTree = True  


    while currentHeight:
        nextHeight = []

        #If the current number of nodes in currentHeight isn't full,
        #The tree isn't a complete tree.
        if len(currentHeight) != (2 ** depthCounter):
            completeTree = False


        for node in currentHeight:
            if node:
                #If height isn't full, there can't be children
                if (node.left or node.right) and (not completeTree):
                    return False 
                if node.left:
                    nextHeight.append(node.left)
                if node.right:
                    nextHeight.append(node.right)

        depthCounter += 1
        currentHeight = nextHeight

    return True




root = Node(7, Node(1, 
                    Node(2), Node(3,
                                    Node(12))), 
                Node(4, 
                    Node(5), Node(6,
                                    Node(10,
                                            Node(11))))
                )


print checkBalanced(root)

root = Node(1, Node(2, 
                    Node(3), Node(4)), 
                Node(4, 
                    Node(5), Node(6))
                )

print checkBalanced(root)