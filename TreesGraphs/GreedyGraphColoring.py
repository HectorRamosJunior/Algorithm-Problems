"""
    Greedy Coloring Algorithm Implementation for Graph Coloring
    Uses the adjacency list within the vertex node objects.
    Returns dict of nodes in each color of the graph.
    Hector Ramos
    4/2/2016
"""

# Returns bool stating if any adjacent nodes of the input vertex
# Have the desired color for the given vertex node.
def is_safe(vertex, color):
    for adjacent_vertex in vertex.edge_list:
        if adjacent_vertex.color == color:
            return False

    return True

# Greedily colors each vertex node in the graph in order via 
# the given vertex_list. Returns a color dict of all nodes for each color
def graph_coloring(vertex_list):
    color_dict = {}

    for vertex in vertex_list:
        # Checks if any present colors in the graph can work for this vertex
        for color in color_dict:
            # Handle if this loop already colored the vertex
            if vertex.color:
                break
            # Handle if this vertex can be colored with a present color
            elif is_safe(vertex, color):
                vertex.color = color
                color_dict[color].append(vertex.key)

        # Appends new color to the vertex/color_dict if there were none valid
        if not vertex.color:
            new_color = len(color_dict) + 1
            # Assign new color to vertex, append new color to dict
            vertex.color = new_color
            color_dict[new_color] = [vertex.key]

    print_color_dict(color_dict)
    return color_dict

# Prints out the vertexes for each color in the graph's color_dict
def print_color_dict(color_dict):
    print "This graph has %d colors.\n" %len(color_dict)

    # Iterate through each color in the dictionary
    for color in color_dict:
        string_of_vertexes = ""

        # Add each vertex to string for the given color
        for vertex_key in color_dict[color]:
            string_of_vertexes += vertex_key + " "

        print "The nodes for color %d are:" %color
        print string_of_vertexes

class Vertex(object):
    def __init__(self, key, color=None, edge_list=[]):
        self.key = key
        self.color = color
        self.edge_list = edge_list


if __name__ == "__main__":
    # Graph used found in below URL:
    # http://i.imgur.com/5SFpchm.png
    v0 = Vertex("0"); v1 = Vertex("1"); v2 = Vertex("2")
    v3 = Vertex("3"); v4 = Vertex("4"); v5 = Vertex("5")
    v6 = Vertex("6"); v7 = Vertex("7"); v8 = Vertex("8")
    v9 = Vertex("9")

    v0.edge_list = [v1, v2, v5]
    v1.edge_list = [v0, v6, v7]
    v2.edge_list = [v0, v3, v8]
    v3.edge_list = [v2, v4, v7]
    v4.edge_list = [v3, v5, v6]
    v5.edge_list = [v0, v4, v9]
    v6.edge_list = [v1, v4, v8]
    v7.edge_list = [v1, v3, v9]
    v8.edge_list = [v2, v6, v9]
    v9.edge_list = [v5, v7, v8]

    vertex_list = [v0, v1, v2, v3, v4, v5, v6, v7, v8, v9]

    graph_coloring(vertex_list)
