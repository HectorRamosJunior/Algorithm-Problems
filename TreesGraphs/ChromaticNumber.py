"""
    Chromatic Number Implementation for Graph Coloring
    Uses an adjacency matrix, returns list of nodes' colorings
    Hector Ramos
    4/1/2016
"""

# Checks the current vertex's adjacent vertexes to see if they are 
# The desired color. If so, the current vertex cannot be colored such.
def isSafe(vertex, color, vertex_colors, adjacency_matrix):
    for adjacent_vertex in xrange(len(adjacency_matrix[0])):
        if adjacency_matrix[vertex][adjacent_vertex]:
            if vertex_colors[adjacent_vertex] == color:
                return False

    return True

# Recursively calls itself to test every possible node coloring in the graph
# Within the scope of the max colors given. Changes the vertex_colors list
# by reference during operation. Returns True if possible, False if not.
def graph_coloring(vertex, max_colors, vertex_colors, adjacency_matrix):
    # If vertex index doesn't exist, all vertexes have been colored
    if vertex >= len(vertex_colors):
        return True

    for color in xrange(max_colors):
        if isSafe(vertex, color, vertex_colors, adjacency_matrix):
            vertex_colors[vertex] = color

            if graph_coloring(vertex + 1, max_colors, 
                                vertex_colors, adjacency_matrix):
                return True

            vertex_colors[vertex] = 0

    # There is no possible coloring of this vertex
    return False

# Finds the chromatic number for the given graph, and returns its 
# vertex coloring. Returns false if the chromatic number > # of vertexes.
def chromatic_number_coloring(adjacency_matrix):
    # Assumes graph has at least 1 edge
    chromatic_number = 2
    num_vertexes = len(adjacency_matrix[0])
    vertex_colors = []

    while chromatic_number <= num_vertexes:
        vertex_colors = [None for i in xrange(num_vertexes)]
        
        # If a valid graph coloration found, return vertex coloring
        if graph_coloring(0, chromatic_number,
                            vertex_colors, adjacency_matrix):
            print_vertex_colors(vertex_colors)
            return vertex_colors

        chromatic_number += 1

    # This shouldn't happen?
    return False

def print_vertex_colors(vertex_colors):
    color_dict = {}

    for i in xrange(len(vertex_colors)):
        if vertex_colors[i] not in color_dict:
            color_dict[vertex_colors[i]] = [i]
        else:
            color_dict[vertex_colors[i]].append(i)

    print "There are %d colors in this graph coloring." %len(color_dict)

    for color in color_dict:
        colored_nodes_string = ""

        for node in color_dict[color]:
            colored_nodes_string += str(node) + " "

        print "The following nodes are colored %s:" %str(color)
        print colored_nodes_string


if __name__ == "__main__":
    # Graph found at below URL:
    # http://i.imgur.com/5SFpchm.png
    adjacency_matrix = [[False for i in xrange(10)] for j in xrange(10)]
    matrix = adjacency_matrix

    matrix[0][1] = True; matrix[0][2] = True; matrix[0][5] = True
    matrix[1][0] = True; matrix[1][6] = True; matrix[1][7] = True
    matrix[2][0] = True; matrix[2][3] = True; matrix[2][8] = True
    matrix[3][2] = True; matrix[3][4] = True; matrix[3][7] = True
    matrix[4][3] = True; matrix[4][5] = True; matrix[4][6] = True
    matrix[5][0] = True; matrix[5][4] = True; matrix[5][9] = True
    matrix[6][1] = True; matrix[6][4] = True; matrix[6][8] = True
    matrix[7][1] = True; matrix[7][3] = True; matrix[7][9] = True
    matrix[8][2] = True; matrix[8][6] = True; matrix[8][9] = True
    matrix[9][5] = True; matrix[9][7] = True; matrix[9][8] = True

    vertex_colors = chromatic_number_coloring(adjacency_matrix)
 

