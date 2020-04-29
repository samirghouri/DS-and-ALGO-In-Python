# Implementing a Min Binary Heap


class BinHeap():

    # since the entire binary heap can be represented by a single list
    # we use all the constuctor to initialise the list.
    def __init__(self):
        self.list = None  # assigning zero just to make the start index 1
        self.current_size = None

    # inserting in the heap but first
    # we need to nulllify the violation of the invariance

    def swim(self, i):
        while i//2 > 0:
            # i//2 represents the parent node
            # if the child node is smaller than the parent node
            if self.list[i] < self.list[i//2]:
                self.list[i], self.list[i//2] = self.list[i//2], self.list[i]
                i = i//2

    def insert(self, k):
        self.list.append(k)
        self.current_size = self.current_size+1
        self.swim(self.current_size)

    # Now we will look at when we what to delete the root node
    # we put the last node in place of the root node and sink it down
    # Before that we also need to maintain the invariance

    def sink(self, i):
        while i*2 < self.current_size:
            min_chd = self.minChild(i)
            if self.list[i] > self.list[min_chd]:
                self.list[i], self.list[min_chd] = self.list[min_chd], self.list[i]
            i = min_chd

    def minChild(self, i):
        if i*2+1 > self.current_size:
            return i*2
        else:
            if self.list[2*i] < self.list[i*2+1]:
                return i*2
            else:
                return i*2+1

    def delMin(self):
        minimum = self.list[1]
        self.list[1] = self.list[self.current_size]
        self.current_size = self.current_size-1
        self.list.pop()
        self.sink(1)
        return minimum

    def display(self):
        return self.list[1:]

    def build_heap(self, array):
        self.list = [0]+array
        self.current_size = len(array)
        i = self.current_size//2
        while i > 0:
            self.sink(i)
            i = i-1


a = [5, 2, 6, 3, 1, 97, 4]
obj = BinHeap()
obj.build_heap(a)
print(obj.display())
