"""
    Red Black Tree Class
    Hector Ramos
    12/9/2015
"""

class RedBlackTree(object):
    def __init__(self):
        self.root = None


    def add(self, value):
        # Set root equal to new node, set root equal to black
        if not self.root:
            self.root = RedBlackTree.Node(value)
            self.rebalance(self.root)
            return

        current_node = self.root

        # Add new element to BST
        while True:
            # Traverse left if value less than current_node
            if value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    new_node = RedBlackTree.Node(value, parent=current_node)
                    current_node.left = new_node
                    break
            elif value >= current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    new_node = RedBlackTree.Node(value, parent=current_node)
                    current_node.right = new_node
                    break

        # Check if any violations occured and corrects the tree
        self.rebalance(new_node)


    # Checks insertion cases for violations and rebalances if so
    def rebalance(self, node):
        # Case 1: node is root and is not black
        if not node.parent:
            node.color = False
            print "Case 1 enacted on node %d." % node.value
            return

        parent = node.parent

        # Case 2: if the parent color is black, tree is valid
        if not parent.color:
            print "Case 2 enacted on node %d." % node.value
            return

        grandparent = parent.parent

        # Get the uncle node
        if parent is grandparent.right:
            uncle = grandparent.left
        elif parent is grandparent.left:
            uncle = grandparent.right

        # Case 3: if Node, Uncle and Parent are red
        if uncle and parent.color and uncle.color:
            # Set grandparent to Red, Parent and Uncle to black
            print "Case 3 enacted on node %d." % node.value
            grandparent.color = True
            parent.color = False
            uncle.color = False

            # Recursively call on grandparent (possible violation)
            self.rebalance(grandparent)
            return  # Tree is valid

        # Handle Cases 4 and 5 which require tree rotations
        # Cases 4 and 5 have the parent as red and uncle as black
        self.pivot_and_rebalance(node, parent, grandparent)


    # Handle insertion cases 4 and 5
    def pivot_and_rebalance(self, node, parent, grandparent):
        # Check if the node is on the inside of the subtree
        if parent is grandparent.left and node is parent.right:
            node_on_inside = True
        elif parent is grandparent.right and node is parent.left:
            node_on_inside = True
        else:
            node_on_inside = False

        # Case 4: Parent is red and Uncle is black, node on inside of tree
        if node_on_inside:
            print "Case 4 enacted on node %d." % node.value
            # Rotate node around parent to make node on outside of tree
            self.rotate_node_around_parent(node)

            # Reassign parent and node to reflect rotation
            # Case 4 hands off to Case 5 after rotating node to outside
            parent, node = node, parent

        # Case 5: Parent is red and Uncle is black, node on outside of tree
        # Case 5 calls for rotating the parent around its grandparent
        self.rotate_node_around_parent(parent)

        # After rotation, set rotated parent to black, grandparent to red
        parent.color = False
        grandparent.color = True
        print "Case 5 enacted on node %d." % node.value


    # Function assumes node has a parent
    def rotate_node_around_parent(self, node):
        parent = node.parent
        grandparent = parent.parent

        # Rotate node right
        if node is parent.left:
            parent.left = node.right
            node.right = parent
        # Rotate node left
        elif node is parent.right:
            parent.right = node.left
            node.left = parent

        # Handle grandparent reassignment to 'new' parent node
        if grandparent and parent is grandparent.right:
            grandparent.right = node
        elif grandparent and parent is grandparent.left:
            grandparent.left = node
        # If no grandparent, parent was root, reassign
        else:
            self.root = node


    # Prints the tree by depth
    def print_tree(self):
        if not self.root:
            print "No Tree!"
            return 

        q = [self.root]

        depth_list = []
        current_depth_count = 1
        next_depth_count = 0

        while q:
            node = q.pop(0)
            depth_list.append(node.value)

            if node.left:
                q.append(node.left)
                next_depth_count += 1
            if node.right:
                q.append(node.right)
                next_depth_count += 1

            current_depth_count -= 1
            if current_depth_count == 0:
                current_depth_count = next_depth_count
                next_depth_count = 0

                print depth_list
                depth_list = []


    @staticmethod
    class Node(object):
        def __init__(self, value, color=True, left=None, 
                    right=None, parent=None):
            self.value = value
            # Boolean for Red/Black coloration. True is Red, False is Black
            self.color = color 
            self.left = left
            self.right = right
            self.parent = parent


rbt = RedBlackTree()

[rbt.add(x) for x in xrange(1,7)]

rbt.print_tree()