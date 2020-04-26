# Merge Sort

#prerequisite is recurrsion

# divide arrays in two halves
# sort the two halves
# merge the two halves

# pseudo code for merge function
# merge(left_array,right_array,original_array)
# nL=len of left array,rL = len of right array
# while(i<nL and j<rl):
#    # if(L(i)<=R[j]) then O[k]=L(i) and increment i
#   # else then O[k]=R[j] and increment j
#    # finally increment k
# while(i<nL) then add all the elements of L in O
# while(j<rl) then add all the elements of R in O

# psedo code for mergesort
# mergesort(array):
# n - len(array)
# if n<2:
#     return array
# mid = n/2
# left_array = lenght of mid
# right_array = lenght of n -mid
# for i from 0 to mid:
#     append element from array to left_array
# for i from mid to n-1:
#     append element from array to right_array
# mergesor(left_array)
# mergesort(right_array)
# merge(left_array,right_array,array)


# Finally here we go

class MergeSort(object):
    def __init__(self):
        pass

    def merge(self, left_array, right_array, original_array):
        nL, nR = len(left_array), len(right_array)
        i, j, k = 0, 0, 0
        while i < nL and j < nR:
            if left_array[i] < right_array[j]:
                original_array[k] = left_array[i]
                i = i+1
            else:
                original_array[k] = right_array[j]
                j = j+1

            k = k+1
        while(i < nL):
            original_array[k] = left_array[i]
            i = i+1
            k = k+1
        while(j < nR):
            original_array[k] = right_array[j]
            k = k+1
            j = j+1

    def mergesort(self, original_array):
        n = len(original_array)
        if n < 2:
            return original_array
        mid = n//2
        left_array = []
        right_array = []
        for i in range(mid):
            left_array.append(original_array[i])
        for j in range(mid, n):
            right_array.append(original_array[j])
        self.mergesort(left_array)
        self.mergesort(right_array)
        self.merge(left_array, right_array, original_array)
        return original_array


# a = [1, 5, 2, 6, 9, 0]
a = [4, 2, 345, 6, 6, 68, 94, 3]

print(MergeSort().mergesort(a))
