"""
    Max Heap Class
    Hector Ramos
    3/23/2016
"""
# Binary MaxHeap Data Structure
class MaxHeap(object):
    # Assumes heaplist if entered is max heap structured
    def __init__(self, heap_list = []):
        self.heap_list = heap_list

    # Adds a new element to the heap, percolates it up if necessary
    def add(self, value):
        # Add the element to the leftmost element available
        self.heap_list.append(value)
        # Restructure the heap if necessary to hold Parent >= Child true
        self.percolate_up()


    # "Pops" the top of the heap for the max value, maintains structure
    def remove(self):
        if not self.heap_list:
            return None
        elif len(self.heap_list) == 1:
            return self.heap_list.pop()

        # Store the top element to return after heap structure is maintained
        output = self.heap_list[0]
        # Set Heap root equal to leftmost element to maintain tree balance
        self.heap_list[0] = self.heap_list.pop()

        # Restructure the heap to keep balance after root is popped
        self.percolate_down()

        return output


    # Percolate the last element up the heap if necessary
    # To maintain the Parent >= Child property
    def percolate_up(self):
        # Parents of the current index are found at (index - 1) / 2
        current_index = len(self.heap_list) - 1
        parent_index = (current_index - 1) / 2

        while parent_index >= 0:
            # Heap structure holds P >= C true
            if self.heap_list[parent_index] >= self.heap_list[current_index]:
                break

            # Swap the parent and child node values
            temp = self.heap_list[current_index]
            self.heap_list[current_index] = self.heap_list[parent_index]
            self.heap_list[parent_index] = temp

            # Set current_index to the parent_index, loop to hold P >= C
            current_index = parent_index
            parent_index = (current_index - 1) / 2


    # Percolate the last element down the heap from the root
    # This maintains the heap balance and structure
    def percolate_down(self):
        # Children of the current index are located at (index * 2) +1 or +2
        current_index = 0
        child_index1 = (current_index * 2) + 1
        child_index2 = (current_index * 2) + 2

        while child_index1 < len(self.heap_list):
            # Set max child index to child 1 as it's always present
            max_child_index = child_index1

            # If Second child exists, set max child to max of the two
            if child_index2 < len(self.heap_list):
                if self.heap_list[child_index2] > self.heap_list[child_index1]:
                    max_child_index = child_index2

            # If P >= C, heap structure maintained
            if self.heap_list[current_index] >= self.heap_list[max_child_index]:
                break

            # Swap the current node with the larger child node
            temp = self.heap_list[max_child_index]
            self.heap_list[max_child_index] = self.heap_list[current_index]
            self.heap_list[current_index] = temp

            # Set the current_index to the max_child_index
            # To iterate the loop again and hold P >= C true
            current_index = max_child_index
            child_index1 = (current_index * 2) + 1
            child_index2 = (current_index * 2) + 2


    # Print each depth as a list
    def print_heap(self):
        if not self.heap_list:
            print "No elements in heap!"
            return

        # Necessary tools to distinguish depthLists in the heap list
        depthList = []
        depth = 0
        counter = 0

        for x in self.heap_list:
            depthList.append(x)
            counter += 1

            if counter == 2 ** depth:
                print depthList
                depthList = []
                depth += 1
                counter = 0

        # Cleanup if last depth not complete
        if depthList:
            print depthList

        print "\n"



maxHeap = MaxHeap()

[maxHeap.add(x) for x in xrange(20)]
maxHeap.print_heap()

[maxHeap.remove() for x in xrange(5)]
maxHeap.print_heap()




