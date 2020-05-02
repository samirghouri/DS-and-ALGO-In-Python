class BinaryHeap:
    def __init__(self):
        # added 0 as we want the heap list to have start index 1
        self.heapList = [0]

    def insert(self, element):
        """
        --Most efficient way to insert in a heap is to append at the end of the heap.
        --This will violate the heap structure property but it can be taken care of. 
        """
        self.heapList.append(element)
        index_of_element = self.heapList.index(element)
        self.swim(index_of_element)

    def swim(self, i):
        while i >= 2:
            if self.heapList[i] < self.heapList[i//2]:
                self.heapList[i], self.heapList[i //
                                                2] = self.heapList[i//2], self.heapList[i]
            i = i//2

    def delete_min(self):
        """
        --Most efficient way to delete min is to remove the root elelment and replace it with an element at the end
        --This will again distort the heap structure so we will sink it down
        """
        min_element = self.heapList[1]
        last_element_index = len(self.heapList)-1
        self.heapList[1] = self.heapList[last_element_index]
        self.heapList.pop()
        self.sink(1)
        return min_element

    def sink(self, i):
        list_length = len(self.heapList)-1
        while 2*i <= list_length:
            min_child = self.min_child(i)
            if self.heapList[i] > self.heapList[min_child]:
                self.heapList[i], self.heapList[min_child] = self.heapList[min_child], self.heapList[i]
            i = min_child

    def min_child(self, i):
        list_length = len(self.heapList)-1
        if 2*i+1 > list_length:
            return 2*i
        else:
            if self.heapList[2*i] < self.heapList[2*i+1]:
                return 2*i
            else:
                return 2*i+1

    def build_heap(self, given_list):
        i = len(given_list)//2
        self.heapList += given_list
        while i > 0:
            self.sink(i)
            i = i-1

    def display(self):
        print(self.heapList[1:])


obj = BinaryHeap()
a = [1, 4, 3, 6, 8, 2]
obj.build_heap(a)
obj.display()
obj.insert(2)
obj.insert(7)
obj.display()
