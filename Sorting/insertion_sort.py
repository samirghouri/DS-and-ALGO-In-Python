class InsertionSort:
    def __init__(self):
        pass

    def sort(self, array):
        n = len(array)
        for i in range(n):
            j = i
            while(j != 0):
                if array[j] < array[j-1]:
                    self.exchange(array, j, j-1)
                    j = j-1
                else:
                    break
        return array

    @staticmethod
    def exchange(a, x, y):
        temp = a[x]
        a[x] = a[y]
        a[y] = temp
        return a


x = [554, 6, 44, 6, 8]
obj = InsertionSort().sort(x)
print(obj)
