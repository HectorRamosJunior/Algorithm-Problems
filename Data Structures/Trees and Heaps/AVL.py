"""
    AVL Tree Class
    Only handles insertions currently, will add deletion later
    Hector Ramos
    12/9/2015
"""

class AVLTree(object):
    def __init__(self):
        self.root = None


    def add(self, value, node = None):
        # If first time add was called, root doesn't exist
        if not node and not self.root:
            self.root = AVLTree.Node(value)
            return
        # Handle initial recursive call
        elif not node:
            node = self.root

        # Traverse tree to the left
        if value < node.value:
            # Recursively call traversal for updating later
            if node.left:
                self.add(value, node=node.left)
            else:
                node.left = AVLTree.Node(value, parent=node)
        # Traverse tree to the right
        elif value >= node.value:
            # Recursively call traversal for updating later
            if node.right:
                self.add(value, node=node.right)
            else:
                node.right = AVLTree.Node(value, parent=node)

        # Get subtree heights of current node
        left_height, right_height = self.get_subtree_heights(node)

        # Check if subtree is imbalanced
        if abs(left_height - right_height) > 1:
            # If the difference is positive, left subtree is larger
            if left_height - right_height > 0:
                self.rebalance_and_update_left(node)
            # If the difference is negative, right subtree is larger
            elif left_height - right_height < 0:
                self.rebalance_and_update_right(node)

            return

        # Update height of current node
        self.update_height(node)


    # Rebalances the left subtree, updates heights of moved nodes
    def rebalance_and_update_left(self, node):
        left_child = node.left
        # Get rotating node subtree heights
        left_height, right_height = self.get_subtree_heights(left_child)

        # If larger subtree is on inside, rotate it to be on the outside
        if right_height > left_height:
            self.rotate_around_parent(left_child.right)
            
            # Update rotated node heights
            left_child = node.left
            self.update_height(left_child.left)
            self.update_height(left_child)

        # Handle updating subtree on the outside
        rotated = self.rotate_around_parent(left_child)
        
        # Update rotated node heights
        self.update_height(rotated)
        self.update_height(rotated.right)


    # Rebalances the right subtree, updates heights of moved nodes
    def rebalance_and_update_right(self, node):
        right_child = node.right
        # Get rotating node subtree heights
        left_height, right_height = self.get_subtree_heights(right_child)

        # If larger subtree is on inside, rotate it to be on the outside
        if left_height > right_height:
            self.rotate_around_parent(right_child.left)

            
            # Update rotated node heights
            right_child = node.right
            self.update_height(right_child.right)
            self.update_height(right_child)

        # Handle updating subtree on the outside
        rotated = self.rotate_around_parent(right_child)
        
        # Update rotated node heights
        self.update_height(rotated)
        self.update_height(rotated.left)


    # Rotates child node around its parent node, returns new parent node
    # Assumes parent exists
    def rotate_around_parent(self, node):
        parent = node.parent 
        grandparent = parent.parent

        # Rotate node right
        if node is parent.left:
            parent.left = node.right
            # If handed off subtree exists, set new parent
            if node.right:
                node.right.parent = parent 

            node.right = parent
        # Rotate node left
        elif node is parent.right:
            parent.right = node.left
            # If handed off subtree exists, set new parent
            if node.left:
                node.left.parent = parent 

            node.left = parent

        # Set proper parent links
        node.parent = parent.parent
        parent.parent = node

        if not grandparent:
            self.root = node
        elif parent is grandparent.left:
            grandparent.left = node
        elif parent is grandparent.right:
            grandparent.right = node

        return node

        
    # Returns left and right subtree heights for given node
    def get_subtree_heights(self, node):
        # Define left and right heights. Null is 0 height
        if node.left:
            left_height = node.left.height
        else:
            left_height = 0
        if node.right:
            right_height = node.right.height
        else:
            right_height = 0

        return left_height, right_height


    # Updates the height of a node by looking at its subtrees
    def update_height(self, node):
        left_height, right_height = self.get_subtree_heights(node)

        node.height = max(left_height, right_height) + 1


    # Prints depths of tree list by list
    def print_tree(self):
        if not self.root:
            print "No tree!"
            return

        q = [self.root]

        depth_list = []
        current_depth_count = 1
        next_depth_count = 0

        # BFS
        while q:
            node = q.pop(0)
            depth_list.append((node.value, node.height))

            if node.left:
                q.append(node.left)
                next_depth_count += 1
            if node.right:
                q.append(node.right)
                next_depth_count += 1

            current_depth_count -= 1
            # If current depth is equal to zero, move to next depth
            if current_depth_count == 0:
                current_depth_count = next_depth_count
                next_depth_count = 0

                print depth_list
                depth_list = []

        # For newline
        print


    @staticmethod
    class Node(object):
        def __init__(self, value, height=1, parent=None, left=None, right=None):
            self.value = value
            # Height default to 1 since empty is height of 0
            self.height = height
            self.parent = parent
            self.left = left
            self.right = right


from random import randint

avl = AVLTree()
[avl.add(randint(1,100)) for x in xrange(100)]
avl.print_tree()