# Quick Select

# finding the kth smallest element


class QuickSelect(object):
    def __init__(self):
        pass

    def partition(self, array, start, end):
        pivot = array[end]
        pIndex = start
        for i in range(start, end):
            if array[i] < pivot:
                array[i], array[pIndex] = array[pIndex], array[i]
                pIndex = pIndex+1
        array[pIndex], array[end] = array[end], array[pIndex]
        return pIndex

    def quick_select(self, array, start, end, k):
        while start < end or start == end:
            pIndex = self.partition(array, start, end)
            if k == pIndex:
                return array[pIndex]
            elif k < pIndex:
                end = pIndex-1

            else:
                start = pIndex+1


a = [9, 5, 2, 8, 4]
# print(QuickSelect().quick_select(a, 0, 4, 0))
# print(QuickSelect().quick_select(a, 0, 4, 1))
print(QuickSelect().quick_select(a, 0, 4, 2))
print(QuickSelect().quick_select(a, 0, 4, 3))
print(QuickSelect().quick_select(a, 0, 4, 4))
