# Basic Plan of Action
# Make a minHeap
# take the root elements out and store it in some list one by one
# return the list


class HeapSort(object):
    def __init__(self):
        self.min_heap = MinHeap()

    def heap_sort(self, array):
        self.min_heap.build_heap(array)
        sort_array = []
        for i in range(len(array)):
            a = self.min_heap.delHeap()
            sort_array.append(a)
        return sort_array


class MinHeap(object):
    def __init__(self):
        self.list = [0]
        self.current_size = None
    # inserting into a heap

    def insert(self, k):
        self.list.appen(k)
        self.current_size = self.current_size+1
        self.swim(self.current_size)

    def swim(self, i):
        while i//2 > 0:
            if self.list[i] < self.list[i//2]:
                self.list[i], self.list[i//2] = self.list[i//2], self.list[i]
            i = i//2
    # deleting from the heap

    def delHeap(self):
        miniumum = self.list[1]
        self.list[1] = self.list[self.current_size]
        self.current_size = self.current_size-1
        self.list.pop()
        self.sink(1)
        return miniumum

    def sink(self, i):
        while 2*i < self.current_size or 2*i == self.current_size:
            middle_child = self.midChd(i)
            if self.list[i] > self.list[middle_child]:
                self.list[i], self.list[middle_child] = self.list[middle_child], self.list[i]
            i = middle_child

    def midChd(self, i):
        if 2*i+1 > self.current_size:
            return 2*i
        else:
            if self.list[2*i] < self.list[2*i+1]:
                return 2*i
            else:
                return 2*i+1

    def build_heap(self, array):
        i = len(array)//2
        self.list = [0]+array[:]
        self.current_size = len(array)
        while i > 0:
            self.sink(i)
            i = i-1

    def display(self):
        return self.list[1:]


a = [5, 2, 6, 3, 1, 97, 4, 0, 98, 12, 4]
# a = [1, 4, 3, 6, 8, 2]
obj = HeapSort().heap_sort(a)
print(obj)


# it is an inplace sorting algorithm with O(nlogn) worst case.
