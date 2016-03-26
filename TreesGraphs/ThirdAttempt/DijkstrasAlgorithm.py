"""
    Dijkstra's Algorithm Implementation
    Hector Ramos
    3/25/2016
"""
import sys

# Dijkstra's Algorithm, returns shortest path. Assumes path exists. 
# Returns the nodes' keys on the path.
def dijkstra(start_node, end_node):
    start_node.weight = 0
    visited_node_set = set()
    
    current_node = start_node
    unvisited_node_dict = {}

    # Keep visiting shortest pathed nodes until end node is found
    while current_node is not end_node:
        # Shortest path from start_node to current node found
        visited_node_set.add(current_node.key)

        # Update unvisted nodes in current node's edge list if necessary
        for edge in current_node.edge_list:
            edge_node, edge_weight = edge

            # Possible weight change only if edge_node unvisited
            if not edge_node.key in visited_node_set:
                new_weight = current_node.weight + edge_weight
                
                # If this is the first time the edge_node was encountered
                if not edge_node.key in unvisited_node_dict:
                    unvisited_node_dict[edge_node.key] = edge_node 
                # If path from current node has lesser weight, modify
                if new_weight < unvisited_node_dict[edge_node.key].weight:
                    edge_node.weight = new_weight
                    edge_node.prev = current_node

        # Set current node to popped min weight node from the list
        current_node = pop_min_weight_node(unvisited_node_dict)

    # Now that shortest path is found, traverse backwards
    current_node = end_node
    path_list = []

    # start_node has no previous
    while current_node:
        path_list.append(current_node.key)
        current_node = current_node.prev

    # Reverse path list, since it traversed from end to start
    path_list.reverse()

    print "Total path weight is %d." % end_node.weight
    return path_list

# Returns the popped min weight node from the given dict
def pop_min_weight_node(unvisited_node_dict):
    if not unvisited_node_dict:
        return None

    min_key = None
    for key in unvisited_node_dict:
        if not min_key:
            min_key = key
        elif unvisited_node_dict[min_key].weight > unvisited_node_dict[key].weight:
            min_key = key

    return unvisited_node_dict.pop(min_key) 

class Node(object):
    def __init__(self, key, edge_list=[], weight=sys.maxint):
        self.key = key
        self.edge_list = edge_list
        self.weight = weight
        # Stores the shortest path connected node
        self.prev = None

# Graph taken from below URL
# http://www.reviewmylife.co.uk/data/2008/0715/dijkstras-graph.gif
nodeA = Node("A"); nodeB = Node("B"); nodeC = Node("C")
nodeD = Node("D"); nodeE = Node("E"); nodeF = Node("F"); 
nodeG = Node("G");

nodeA.edge_list = [(nodeC, 1), (nodeD, 2)]
nodeB.edge_list = [(nodeC, 2), (nodeF, 3)]
nodeC.edge_list = [(nodeA, 1), (nodeB, 2), (nodeD, 1), (nodeE, 3)]
nodeD.edge_list = [(nodeA, 2), (nodeC, 1), (nodeG, 1)]
nodeE.edge_list = [(nodeC, 3), (nodeF, 2)]
nodeF.edge_list = [(nodeB, 3), (nodeE, 2), (nodeG, 1)]
nodeG.edge_list = [(nodeD, 1), (nodeF, 1)]

print dijkstra(nodeA, nodeF)