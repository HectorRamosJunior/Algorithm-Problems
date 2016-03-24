"""
    BST Class
    Hector Ramos
    12/9/2015
"""
# Class for a Binary Search Tree, nodes don't have links to parents
class BST(object):
    def __init__(self):
        self.root = None

    # Add a node with the given value to the BST accordingly
    def add(self, value):
        if not self.root:
            self.root = BST.Node(value)
            return

        current_node = self.root

        # Traverse tree until an appropiate leaf is found
        while True:
            # Traverse left if value smaller than current
            if value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = BST.Node(value)
                    break
            # Traverse right if value larger or equal to current
            elif value >= current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = BST.Node(value)
                    break

    # Implements BFS to return first node with the value specified
    # Returns tuple: (desired node, parent node)
    def lookup(self, value):
        prev_node = None
        current_node = self.root

        while current_node:
            if current_node.value == value:
                return current_node, prev_node

            prev_node = current_node
            if value > current_node.value:
                current_node = current_node.right
            elif value < current_node.value:
                current_node = current_node.left

        return None, None

    # Pops the first node's value in the tree (via bfs) with the given value
    # If none exist, returns none. Restructures BST to stay valid
    def remove(self, value):
        print "Deleting %s." % str(value)
        node, parent = self.lookup(value)
        if not node:
            return None

        # Handle if node to be deleted has no children
        if not (node.left or node.right):
            if node is self.root:  # Current Node is the root node
                self.root = None
            elif node is parent.left:
                parent.left = None
            elif node is parent.right:
                parent.right = None
        # Handle if node has only one child
        elif (node.left and not node.right) or (node.right and not node.left):
            # Set successor to proper child subtree
            if node.left:
                successor = node.left
            elif node.right: 
                successor = node.right

            # Replace node with successor via parent pointer
            if node is self.root:
                self.root = successor
            elif node is parent.left:
                parent.left = successor
            elif node is parent.right:
                parent.right = successor
        # Handle if node has both left and right childs
        elif node.left and node.right:
            # Find the "closest" value on the left
            # By going left once and then right until a leaf is hit
            left_closest = node.left
            left_closest_parent = node

            while left_closest.right:
                left_closest_parent = left_closest
                left_closest = left_closest.right

            # Find the "closest" value on the right
            # By going right once and then left until a leaf is hit
            right_closest = node.right
            right_closest_parent = node

            while right_closest.left:
                right_closest_parent = right_closest
                right_closest = right_closest.left

            # Take the closest of these and make it the current node's value
            # Fix the "closest" value node's parent to link to its successor
            if abs(value - left_closest.value) < abs(value - right_closest.value):
                closest_parent = left_closest_parent
                closest = left_closest
                successor = left_closest.left
            else:
                closest_parent = right_closest_parent
                closest = right_closest
                successor = right_closest.right

            # Set node value equal to closest left or right value
            node.value = closest.value
            # Set closest value's parent's subtree accordingly
            if closest is closest_parent.left:
                closest_parent.left = successor
            elif closest is closest_parent.right:
                closest_parent.right = successor

        return node.value

    # Prints BST depth by depth
    def print_tree(self):
        if not self.root:
            print "No tree!"
            return 
        q = [self.root]

        depth_list = []
        current_depth_count = 1
        next_depth_count = 0

        # BFS modified to print depth levels
        while q:
            current_depth_count -= 1
            node = q.pop(0)
            depth_list.append(node.value)

            if node.left:
                next_depth_count += 1
                q.append(node.left)
            if node.right:
                next_depth_count += 1
                q.append(node.right)

            # Current depth is finished
            if current_depth_count == 0:
                current_depth_count = next_depth_count
                next_depth_count = 0

                print depth_list
                depth_list = []

        print "\n"

    @staticmethod
    class Node(object):
        def __init__(self, value, left = None, right = None):
            self.value = value
            self.left = left
            self.right = right


bstObject = BST()

bst_list = [8, 3, 10, 1, 6, 14, 4, 7, 13]
for x in bst_list:
    bstObject.add(x)

bstObject.print_tree()

[(bstObject.remove(x), bstObject.print_tree()) for x in bst_list]

