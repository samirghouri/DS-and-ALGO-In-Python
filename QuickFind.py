class QuickFind:
    id = []
    # __init__ stimulates the constructor in python.It is called when the class in instatiated.

    def __init__(self, n):
        self.n = n
        for i in range(self.n):
            self.id.append(i)

    def find(self, p, q):
        if self.id[p] == self.id[q]:
            return True
        else:
            return False

    def unite(self, p, q):
        pid = self.id[p]
        qid = self.id[q]
        for i in range(self.n):
            if self.id[i] == pid:
                self.id[i] = qid


obj = QuickFind(10)
obj.unite(1, 2)
obj.unite(2, 7)
obj.unite(3, 4)
obj.unite(4, 8)
obj.unite(8, 9)
obj.unite(0, 5)
obj.unite(5, 6)
print(obj.find(3, 6))
print(obj.find(2, 7))
obj.unite(6, 9)
print(obj.find(3, 6))
