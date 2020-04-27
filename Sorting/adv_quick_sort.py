# algorithm quicksort(A, lo, hi):
#     if lo < hi then
#         p ← pivot(A, lo, hi)
#         left, right ← three-way-partition(A, p, lo, hi)

#         quicksort(A, lo, left - 1)
#         quicksort(A, right, hi)

# procedure three-way-partition(A, pivot, lo, hi):
#     l ← lo
#     r ← lo
#     u ← hi

#     while r ≤ u:
#         if A[r] < pivot:
#             swap A[l] and A[r]
#             l ← l + 1
#             r ← r + 1
#         else if A[r] > pivot:
#             swap A[r] and A[u]
#             u ← u - 1
#         else: // the element is equal to pivot
#             r ← r + 1
#     return l, r


class AdvQuickSort(object):
    def __init__(self):
        pass

    def three_way_paritition(self, a, pivot, low, high):
        mid = low
        while mid <= high:
            if a[mid] < pivot:
                a[mid], a[low] = a[low], a[mid]
                low += 1
                mid += 1
            elif a[mid] > pivot:
                a[mid], a[high] = a[high], a[mid]
                high -= 1
            elif a[mid] == pivot:
                mid += 1
        return low, mid

    def sort(self, array, low, high):
        if low < high:
            pivot = array[high]
            left, right = self.three_way_paritition(array, pivot, low, high)
            self.sort(array, low, left-1)
            self.sort(array, right, high)


array = [1, 4, 2, 4, 5, 20, 0, 2, 4, 2, 4, 5]
obj = AdvQuickSort()
obj.sort(array, 0, 11)
print(array)
