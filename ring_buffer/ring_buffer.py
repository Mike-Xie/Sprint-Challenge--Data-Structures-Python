class RingBuffer:
    def __init__(self, capacity, items=[]):
        # replacing oldest instead of doing like a queue
        # forces us to keep track of index of element to replace 
        self.index = 0
        self.capacity = capacity
        self.items = list(items) 

    def append(self, item):
        # if full, replace item at index
        if len(self.items) == self.capacity:
        	self.items[self.index] = item
        else:
        # append when capacity not reached
        	self.items.append(item)
        # increment index by one mode length 
        self.index = (self.index + 1 ) % self.capacity

    def get(self):
        return self.items
