class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None


class Queue:
    def __init__(self):
        self.llist = Linkedlist()

    def enqueue(self, data):
        new_node = Node(data)
        if self.llist.head is None:
            self.llist.head = new_node
        else:
            node = self.llist.head
            while(node.next is not None):
                node = node.next
            node.next = new_node

    def dequeue(self):
        if self.llist.head is None:
            print('Queue is empty')
        else:
            temp = self.llist.head.data
            next_node = self.llist.head.next
            del self.llist.head.data
            self.llist.head = next_node
            print(temp)

    def display(self):
        start_node = self.llist.head
        while(start_node is not None):
            print(start_node.data)
            start_node = start_node.next


obj = Queue()
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(5)
obj.enqueue(8)
# obj.display()
obj.dequeue()
obj.dequeue()
obj.display()
