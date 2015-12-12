"""
    An animal shelter, which holds only dogs and cats, operates on a 
    strictly "first in, first out" basis. People must either adopt 
    the "oldest" (based on arrival time of all animals in the shelter)
    or they can select whether they would prefer a dog or a cat 
    (and receive the oldest animal of that type) They cannot select 
    which specific animal they would like. 

    Create the data structures to maintain this system and implement 
    operations such as: enqueue, dequeueAny, dequeueDog, dequeueCat. 
    You may use the built-in LinkedList data structure.
"""
from Queue import Queue
from random import randint

class ShelterQueue(object):

    def __init__(self):
        self.dogQueue = Queue()
        self.catQueue = Queue()
        self.id = 0

    def enqueue(self, pet, name):
        petTuple = (self.id, name)

        if pet == "dog":
            self.dogQueue.add(petTuple)
        elif pet == "cat":
            self.catQueue.add(petTuple)

        self.id += 1

    def dequeueAny(self):
        firstDog = self.dogQueue.peek()
        firstCat = self.catQueue.peek()

        if (not firstDog) and (not firstCat):
            return None
        elif not firstCat:
            return self.dogQueue.remove()[1]
        elif not firstDog:
            return self.catQueue.remove()[1]
        elif firstDog[0] < firstCat[0]:
            return self.dogQueue.remove()[1]
        elif firstCat[0] < firstDog[0]:
            return self.catQueue.remove()[1]

    def dequeueDog(self):
        if self.dogQueue.isEmpty():
            return None
        return self.dogQueue.remove()[1]

    def dequeueCat(self):
        if self.catQueue.isEmpty():
            return None
        return self.catQueue.remove()[1]


q = ShelterQueue()

for x in xrange(20):
    if randint(0,1) == 0:
        print "Queue Dog %d" %x 
        q.enqueue("dog", x+1)
    else:
        print "Queue Cat %d" %x 
        q.enqueue("cat", x+1)


print "\nDequeueing Dogs:"
for x in xrange(5):
    print q.dequeueDog()

print "\nDequeueing Cats:"
for x in xrange(5):
    print q.dequeueCat()

print "\nDequeueing Any:"
for x in xrange(20):
    print q.dequeueAny()





