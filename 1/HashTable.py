"""
Hash Table Implementation
Hector Ramos, 12/7/2015
"""
class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable(object):

    def __init__(self, capacity = 4):
        self.bucketList = [None for x in xrange(capacity)]
        self.capacity = capacity
        self.filled = 0


    def add(self, key, value):
        bucketAdded = HashTable.__add(self.bucketList, self.capacity, 
                                        key, value)

        if bucketAdded:        
            self.filled += 1
            if self.filled >= self.capacity*.75:
                self.resize()


    @staticmethod
    def __add(bucketList, capacity, key, value):
        index = hash(key) % capacity

        if not bucketList[index]:
            bucketList[index] = Node(key, value)
            return True
        else:
            node = bucketList[index]

            while True:
                if node.key == key:
                    node.value = value
                    break
                elif not node.next:
                    node.next = Node(key, value)
                    break
                else:
                    node = node.next
                    continue


    def resize(self):
        newBucketList = [None for x in xrange(self.capacity*2)]
        newCapacity = len(newBucketList)
        newFilled = 0

        for node in self.bucketList:
            while node:
                bucketAdded = HashTable.__add(newBucketList, 
                                                newCapacity, 
                                                node.key, node.value)

                if bucketAdded:
                    newFilled += 1

                node = node.next

        self.bucketList = newBucketList
        self.capacity = newCapacity
        self.filled = newFilled


    def get(self, key):
        index = hash(key) % self.capacity

        node = self.bucketList[index]
        while node:
            if node.key == key:
                return node.value

            node = node.next

        return None



    def remove(self, key):
        index = hash(key) % self.capacity

        node = self.bucketList[index]
        if node.key == key:
            self.bucketList[index] = node.next
        else:
            while node:
                if node.next == key:
                    node.next = node.next.next
                    break

                node = node.next



h = HashTable()

[h.add(x,x) for x in xrange(100)]

print h.bucketList
print h.capacity, h.filled

print [h.get(x) for x in xrange(100)]
[h.remove(x) for x in xrange(50)]
print [h.get(x) for x in xrange(100)]