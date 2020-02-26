class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, data):
        self.q.append(data)

    def dequeue(self):
        self.q.pop(0)

    def isEmpty(self):
        if len(self.q) == 0:
            return "Is Empty"

        else:
            return "Not Empty"

    def size_of_queue(self):
        return len(self.q)

    def show_queue(self):
        return self.q


obj = Queue()
obj.enqueue(1)
obj.enqueue(3)
obj.enqueue(5)
obj.enqueue(7)
obj.dequeue()
obj.dequeue()
obj.enqueue(2)
print(obj.show_queue())
