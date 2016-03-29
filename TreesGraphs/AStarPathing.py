"""
    A* Pathfinding Algorithm.
    Uses manhattan distance for h cost, so path found isn't always shortest 
    Hector Ramos
    3/27/2016
"""
import sys

# Returns the shortest path found by using the A* algorithm.
# Assumes map is a non jagged 2d array
def get_shortest_path(matrix, start_node, end_node):
    print "Start node is %s, end node is %s." %(start_node.key, end_node.key)
    closed_set = set()
    open_set = set()

    current_node = start_node
    current_node.g_cost = 0
    set_node_h_cost(current_node, end_node)
    current_node.f_cost = current_node.h_cost

    # Proceed until shortest path is found, or end if no valid path
    while current_node and not current_node is end_node: 
        closed_set.add(current_node.key)
        print "Current: %s. G,H,F costs: %d %d %d." %(current_node.key, 
                                                        current_node.g_cost, 
                                                        current_node.h_cost, 
                                                        current_node.f_cost)

        current_x, current_y = current_node.matrix_indices

        # Updates nearby 8 nodes if shorter paths were found
        for i in xrange(-1,2):
            adjacent_x = current_x + i

            # If out of bounds, ignore and continue 
            if adjacent_x < 0 or adjacent_x >= len(matrix[0]):
                continue

            for j in xrange(-1, 2):
                adjacent_y = current_y + j 

                # If out of bounds, ignore and continue
                if adjacent_y < 0 or adjacent_y >= len(matrix):
                    continue

                adjacent_node = matrix[adjacent_x][adjacent_y]
                    
                # Ignore obstruction on map, or if already visited
                if not adjacent_node or adjacent_node.key in closed_set:
                    continue
                elif not adjacent_node in open_set:
                    open_set.add(adjacent_node)
                    set_node_h_cost(adjacent_node, end_node)

                # g movement cost is 14 if diagonal, 10 if cardinal
                if abs(i) == 1 and abs(j) == 1:
                    g_cost = current_node.g_cost + 14
                else:
                    g_cost = current_node.g_cost + 10

                f_cost = g_cost + adjacent_node.h_cost 

                # If path from current node is shorter, update
                if f_cost < adjacent_node.f_cost:
                    adjacent_node.g_cost = g_cost
                    adjacent_node.f_cost = f_cost
                    adjacent_node.prev_node = current_node

        current_node = get_min_cost_node(open_set)

    # There was no valid path
    if not current_node:
        print "No valid path!"
        return None

    shortest_path_list = []
    # Traverse shortest path backwards, appending to shortest_path_list
    while current_node:
        shortest_path_list.append(current_node.key)
        current_node = current_node.prev_node

    # Correct the list to go from start to end node
    shortest_path_list.reverse()
    
    return shortest_path_list

# Set node H cost to end node according to Manhattan distance
def set_node_h_cost(node, end_node):
    node_x, node_y = node.matrix_indices
    end_node_x, end_node_y = end_node.matrix_indices

    node.h_cost = abs(node_x - end_node_x)*10 + abs(node_y - end_node_y)*10

# Pops and returns the node in the open_set with the smallest f_cost
def get_min_cost_node(open_set):
    if not open_set:
        return None

    min_cost_node = None
    for node in open_set:
        if not min_cost_node or min_cost_node.f_cost > node.f_cost:
            min_cost_node = node

    open_set.remove(min_cost_node)
    return min_cost_node

class Node(object):
    def __init__(self, key, matrix_indices):
        self.key = key
        self.matrix_indices = matrix_indices
        self.prev_node = None
        self.g_cost = None
        self.h_cost = sys.maxint 
        self.f_cost = sys.maxint

    def __str__(self):
        return self.key

if __name__ == "__main__":
    from random import randint 
    
    # Map is represented as a 2d array of nodes.
    # For each index, nearby 8 indices are valid as long as index isn't Null
    game_map = [[Node(key=str(x)+str(y)+"  ", matrix_indices=(x,y)) for y in xrange(10)] for x in xrange(10)]

    # Set 25 random elements to None
    for i in xrange(75):
        game_map[randint(0,9)][randint(0,9)] = None 

    start_node, end_node = None, None
    while not start_node or not end_node:
        start_node = game_map[randint(0,9)][randint(0,9)]
        end_node = game_map[randint(0,9)][randint(0,9)]

    for row in game_map:
        row_list = []
        for node in row:
            row_list.append(str(node))

        print row_list

    print "The shortest path is: "
    print get_shortest_path(game_map, start_node, end_node)