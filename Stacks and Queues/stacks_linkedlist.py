class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None


class Stack:
    def __init__(self):
        self.llist = Linkedlist()

    def isEmpty(self):
        if self.llist.head is None:
            print('stack is empty')
        else:
            print('Not empty')

    def push(self, data):
        node = Node(data)
        if self.llist.head is None:
            self.llist.head = node
        else:
            a = self.llist.head
            while(a.next is not None):
                a = a.next
            a.next = node

    def pop(self):
        a = self.llist.head
        if a == None:
            print('null')
        else:
            while a.next is not None:
                previous_a = a
                a = a.next
            temp = a.data
            del a
            previous_a.next = None
            print(temp)

    def size_of_stack(self):
        data_list = []
        a = self.llist.head
        while a is not None:
            data_list.append(a.data)
            a = a.next
        print(len(data_list))

    def display(self):
        temp = self.llist.head
        while(temp):
            print(temp.data)
            temp = temp.next


obj = Stack()
obj.push(1)
obj.push(3)
obj.push(7)
obj.push(9)
# obj.display()
obj.pop()
obj.pop()
# obj.display()
obj.push(5)
obj.push(8)
obj.push(0)
obj.display()
obj.size_of_stack()
