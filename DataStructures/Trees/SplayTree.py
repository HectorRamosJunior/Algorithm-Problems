"""
    Splay Tree Class
    Only handles insertions currently, will add deletion later
    Hector Ramos
    03/25/2016
"""

class SplayTree(object):
    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = SplayTree.Node(value)
            return

        node = self.root
        new_node = None

        # Standard BST add algo, finds appropiate location to add node
        while not new_node:
            if value < node.value:
                if node.left:
                    node = node.left
                else:
                    new_node = SplayTree.Node(value, parent=node)
                    node.left = new_node
            elif value >= node.value:
                if node.right:
                    node = node.right
                else:
                    new_node = SplayTree.Node(value, parent=node)
                    node.right = new_node

        # Move recently added node top of tree
        self.splay(new_node)

    # Moves node to top of BST by calling tree rotations
    def splay(self, node):
        # Loop until node is the new root
        while not node is self.root:
            parent = node.parent
            grandparent = parent.parent 

            if grandparent:
                # Handle zig-zag (Node on inside of tree) Rotates to outside
                if node is parent.right and parent is grandparent.left:
                    self.rotate_around_parent(node)
                elif node is parent.left and parent is grandparent.right:
                    self.rotate_around_parent(node)
                # Handle zig-zig (Node on outside of tree) Rotates parent once
                elif node is parent.right and parent is grandparent.right:
                    self.rotate_around_parent(parent)
                elif node is parent.left and parent is grandparent.left:
                    self.rotate_around_parent(parent)

            # In all cases, last step is to rotate node (even if no grandparent)
            # Also handles defining the node as root for the object
            self.rotate_around_parent(node)

    # Rotates node around its parent, assumes parent exists
    def rotate_around_parent(self, node):
        parent = node.parent 
        grandparent = parent.parent

        # Handle right rotation
        if node is parent.left:
            parent.left = node.right
            # Redefine subtree parent if necessary
            if node.right:
                node.right.parent = parent
            node.right = parent
        # Handle left rotation
        elif node is parent.right:
            parent.right = node.left
            # Redefine subtree parent if necessary
            if node.left:
                node.left.parent = parent
            node.left = parent

        # Redfine parent parameters
        node.parent = grandparent
        parent.parent = node

        # No grandparent means parent was root, redefine root
        if not grandparent:
            self.root = node
        # Redefine grandparent link to new subtree head
        elif parent is grandparent.left:
            grandparent.left = node
        elif parent is grandparent.right:
            grandparent.right = node

    # Print tree depths list by list
    def print_tree(self):
        if not self.root:
            print "No Tree!"
            return 

        q = [self.root]

        depth_list = []
        current_depth_count = 1
        next_depth_count = 0

        # Implement modified BFS to print depths list by list
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
            # If current depth count is 0, print and move to next depth
            if current_depth_count == 0:
                current_depth_count = next_depth_count
                next_depth_count = 0

                print depth_list
                depth_list = []

        # For the new line
        print 

    @staticmethod
    class Node(object):
        def __init__(self, value, parent=None, left=None, right=None):
            self.value = value
            self.parent = parent 
            self.left = left
            self.right = right


from random import randint

splay = SplayTree()
[(splay.add(randint(1,100)), splay.print_tree()) for x in xrange(10)]
