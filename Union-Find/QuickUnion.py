class QuickUnion:

    def __init__(self, n):
        self.id = []
        for i in range(n):
            self.id.append(i)

    def root(self, i):
        while(i != self.id[i]):
            i = self.id[i]
        return i

    def find(self, p, q):
        return self.root(p) == self.root(q)

    def unite(self, p, q):
        a = self.root(p)
        b = self.root(q)
        self.id[a] = b
        print(self.id)


obj = QuickUnion(10)
obj.unite(3, 4)
obj.unite(4, 9)
obj.unite(8, 0)
obj.unite(2, 3)
obj.unite(5, 6)
obj.unite(5, 9)
print(obj.find(7, 1))
print(obj.find(9, 3))
obj.unite(7, 3)
obj.unite(4, 8)
print(obj.root(4))
obj.unite(6, 1)
print(obj.root(3))
