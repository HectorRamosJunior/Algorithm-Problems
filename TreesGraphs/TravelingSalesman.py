"""
    Traveling Salesman Solution
    Employs Dijkstra's algorithm
    Hector Ramos
    3/28/2016
"""
import DijkstrasAlgorithm as dijk
from random import shuffle
import sys

# Tests random permutation orders of the given map
# Once a path hasn't been replaced by a more efficient one after
# len(nodes)^2 permutations, that permutation is returned
def traveling_salesman(node_list):
    # Assigns local node_list to a copy of the list to not modify original
    shuffled_list = list(node_list)
    shuffle(shuffled_list)

    tested_permutations = set()

    shortest_path_list = []
    shortest_path_test_count = 0
    shortest_path_weight = sys.maxint

    while shortest_path_test_count <= len(node_list)**2:
        tested_permutations.add(get_node_keys_as_string(shuffled_list))

        # Get total weight for new node visit order
        new_weight = 0
        for i in xrange(len(shuffled_list) - 1):
            dijk.dijkstra(shuffled_list[i], shuffled_list[i+1])
            new_weight += shuffled_list[i+1].weight

            # Resets the node weights in the graph for djikstra's algorithm
            for node in shuffled_list:
                node.weight = sys.maxint
                node.prev = None

        if new_weight < shortest_path_weight:
            shortest_path_weight = new_weight
            shortest_path_test_count = 0
            shortest_path_list = list(shuffled_list)
        else:
            shortest_path_test_count += 1

        new_permutation_attempts = 0
        while (get_node_keys_as_string(shuffled_list) in tested_permutations
                and new_permutation_attempts < len(node_list)**2):
            shuffle(shuffled_list)
            new_permutation_attempts += 1

        # End, take current shortest path if new list not found
        if new_permutation_attempts == 50:
            break


    print "The total weight of the shortest path is %d" % shortest_path_weight
    return shortest_path_list

# Returns a string of all the node keys in the list
def get_node_keys_as_string(shuffled_list):
    output_string = ""

    for node in shuffled_list:
        output_string += node.key

    return output_string


if __name__ == "__main__":
    # Graph used found at the below URL:
    # http://www.benjysbrain.com/Flask/tsp1.jpg
    nodeA = dijk.Node("A"); nodeB = dijk.Node("B")
    nodeC = dijk.Node("C"); nodeD = dijk.Node("D"); 
    nodeE = dijk.Node("E")

    nodeA.edge_list = [(nodeB, 25), (nodeC, 40), (nodeD, 15), (nodeE, 37)]
    nodeB.edge_list = [(nodeA, 25), (nodeC, 3), (nodeD, 25), (nodeE, 8)]
    nodeC.edge_list = [(nodeA, 40), (nodeB, 3), (nodeD, 4), (nodeE, 6)]
    nodeD.edge_list = [(nodeA, 15), (nodeB, 25), (nodeC, 4), (nodeE, 50)]
    nodeE.edge_list = [(nodeA, 37), (nodeB, 8), (nodeC, 6), (nodeD, 50)]

    node_list = [nodeA, nodeB, nodeC, nodeD, nodeE]

    shortest_path_list = traveling_salesman(node_list)

    output = []
    for node in shortest_path_list:
        output.append(node.key)

    print output
