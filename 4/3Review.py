'''
    Given a binary tree, design an algorithm which creates a linked list
    of all the nodes at each depth 
    (eg.  If you have a tree with depth D, you'll have D linked lists.)
'''
from Node import Node 

#Returns a list of lists for each given depth of the tree
def listofDepths(root):
    depthList = [[root]]
    counter = 0

    while True:
        depthList.append([]) #Next depth's list

        #Iterate through nodes in the current depth
        #If there are children, append to the new list
        for node in depthList[counter]:
            if node.left:
                depthList[counter+1].append(node.left)
            if node.right:
                depthList[counter+1].append(node.right)

        #If the list hasn't been appended to, pop it, end
        if not depthList[counter+1]:
            depthList.pop()
            break

        counter += 1


    return depthList


root = Node(7, Node(1, 
                    Node(2), Node(3)), 
                Node(4, Node(5), Node(6,
                                    Node(10))   
                                                ))

depthList = listofDepths(root)

print depthList
for nodes in depthList:
    for n in nodes:
        print n.value