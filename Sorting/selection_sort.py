class SelectionSort:
    def __init__(self):
        pass

    def sort(self, array):
        self.array = array
        for i in range(len(self.array)):
            min = i
            j = i+1
            for j in range(len(self.array)):
                if self.less(self.array[j], self.array[min]):
                    min = j
                    self.exchange(self.array, min, i)
        return self.array

    @staticmethod
    def less(x, y):
        if x > y:
            return True
        else:
            return False

    @staticmethod
    def exchange(a, i, j):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
        return a


x = [1, 1, 1, 3, 5, 7, 3, 6, 8, 82, 1]
obj = SelectionSort().sort(x)
print(obj)
