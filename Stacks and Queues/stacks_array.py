class Stacks:
    def __init__(self):
        self.s = []

    def push(self, data):
        self.s.append(data)

    def pop(self):
        self.s.pop()

    def isEmpty(self):
        sz = len(self.s)
        if sz == 0:
            return 'Empty'
        else:
            return 'Not Empty'

    def stack_size(self):
        return len(self.s)

    def show_stack(self):
        return self.s


obj = Stacks()
obj.push(1)
obj.push(3)
obj.push(5)
obj.pop()
obj.push(7)
obj.push(9)
obj.pop()
print(obj.show_stack())
print(obj.stack_size())
print(obj.isEmpty())
