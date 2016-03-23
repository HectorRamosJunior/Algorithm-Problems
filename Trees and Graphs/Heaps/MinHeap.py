"""
    Min Heap Class
    Hector Ramos
    3/22/2016
"""
# Binary Min Heap Using a Heap List
class MinHeap(object):
    def __init__(self, heap_list = []):
        # Assumes possibly heap_list input already structured properly
        self.heap_list = heap_list


    # Adds the new value to the leftmost element
    def add(self, value):
        # Add to the leftmost element
        self.heap_list.append(value)
        self.percolate_up()


    # Pops the min element from the heap (Top element by structure)
    def remove(self):
        if not self.heap_list:
            return None
        elif len(self.heap_list) == 1:
            return self.heap_list.pop()

        # Store min element before percolation
        output = self.heap_list[0]
        # Maintain P <= C heap structure
        self.percolate_down()

        return output


    # Percolate the leftmost element up the tree as necessary
    # To maintain Parent <= Child property of the tree
    def percolate_up(self):
        # The parent of a node(index) is found at (index - 1) / 2
        child_index = len(self.heap_list) - 1
        parent_index = (child_index - 1) / 2

        while parent_index >= 0:
            # If Parent <= Child, min heap maintained
            if self.heap_list[parent_index] <= self.heap_list[child_index]:  
                break

            # If Parent > Child swap the values
            temp = self.heap_list[child_index]
            self.heap_list[child_index] = self.heap_list[parent_index]
            self.heap_list[parent_index] = temp

            # Set child index equal to current parent, check if P <= C again
            child_index = parent_index
            parent_index = (child_index - 1) / 2


    # Percolate the leftmost element as the root down the tree as necessary
    # To maintain Parent <= Child property of the tree
    def percolate_down(self):
        # Set Heap root equal to leftmost element to maintain tree balance
        self.heap_list[0] = self.heap_list.pop()

        # To maintain Parent <= Child property of the tree
        # The children of a node(index) is found at (index * 2) + 1 or + 2
        parent_index = 0
        child_index1 = (parent_index * 2) + 1
        child_index2 = (parent_index * 2) + 2

        while child_index1 < len(self.heap_list):
            # First child will always be present in this loop
            min_child_index = child_index1

            # If second child is in the list bound, handle if value is min
            if child_index2 < len(self.heap_list):
                if self.heap_list[child_index2] < self.heap_list[child_index1]:
                    min_child_index = child_index2

            # If Parent <= Child holds, tree structure maintained
            if self.heap_list[parent_index] <= self.heap_list[min_child_index]:
                break 

            # Swap parent node with the min child node
            temp = self.heap_list[min_child_index]
            self.heap_list[min_child_index] = self.heap_list[parent_index]
            self.heap_list[parent_index] = temp

            # Iterate again with min child as the new parent_index
            parent_index = min_child_index
            child_index1 = (parent_index * 2) + 1
            child_index2 = (parent_index * 2) + 2

    # Print the current heap in pyramid fashion
    def print_heap(self):
        if not self.heap_list:
            print "Heap has no elements!"

        depthValues = []
        depth = 0
        counter = 0

        for i in xrange(len(self.heap_list)):
            depthValues.append(str(self.heap_list[i]))
            counter += 1
            
            # Depth max exceeded, print depth
            if counter == 2 ** depth:
                print " ".join(depthValues)
                depthValues = []
                depth += 1
                counter = 0

        # Cleanup any nodes in a not completed depth
        if depthValues:
            print " ".join(depthValues)




minHeap = MinHeap()

[minHeap.add(x) for x in reversed(xrange(20))]
minHeap.print_heap()

[minHeap.remove() for x in xrange(5)]
minHeap.print_heap()
