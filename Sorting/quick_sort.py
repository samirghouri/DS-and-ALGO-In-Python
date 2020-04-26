class QuickSort(object):
    def __init__(self):
        pass

    def quicksort(self, array, start, end):
        if start < end:
            pivot_index = self.partition(array, start, end)
            self.quicksort(array, start, pivot_index-1)
            self.quicksort(array, pivot_index+1, end)

    def partition(self, array, start, end):
        pivot = array[end]
        pivot_index = start
        for i in range(start, end):
            if array[i] <= pivot:
                array[i], array[pivot_index] = self.swap(
                    array[i], array[pivot_index])
                pivot_index = pivot_index+1
        array[pivot_index], array[end] = self.swap(
            array[pivot_index], array[end])
        return pivot_index

    @staticmethod
    def swap(a, b):
        temp = a
        a = b
        b = temp
        return a, b


a = [4, 2, 345, 6, 6, 68, 94, 3]
QuickSort().quicksort(a, 0, 7)
print(a)
