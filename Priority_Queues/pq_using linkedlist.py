# A priority queue is a queue in which each item is
# assigned a priority and items with a higher priority
#  are removed before those with a lower priority, irrespective
# of when they were added. Integer values are used for the priorities
#  with a smaller integer value having a higher priority. In an unbounded
#  priority queue, there are no limits on the range of integer values that
# can be used for the priorities.

# • PriorityQueue(): Creates a new empty unbounded priority queue.

# • isEmpty(): Returns a boolean value indicating whether the queue is empty.

# • length(): Returns the number of items currently in the queue.

# • enqueue(item, priority): Adds the given item to the queue by inserting
# it in the proper position based on the given priority.

# • dequeue(): Removes and returns the next item from the queue, which is the
# item with the highest priority. If two or more items have the same priority,
#  those items are removed in FIFO order. An item cannot be dequeued from an empty queue.

# • peek(): Returns a copy of the next item in the queue, without removing the item.
#  The next item is the same value that would be returned by the dequeue operation.
#  An item cannot be dequeued from an empty queue.


class Node:
    def __init__(self, data, priority):
        self.data = data
        self.next = None
        self.priority = priority


class LinkedList:
    def __init__(self):
        self.head = None


class PriorityQueue:
    def __init__(self):
        self.llist = LinkedList()

    def enqueue(self, data, priority):
        node = Node(data, priority)
        # checking if head is None
        if self.llist.head is None:
            self.llist.head = node
        else:
            # checking for the priority of the head
            temp = self.llist.head
            if temp.priority > node.priority:
                node.next = temp
                self.llist.head = node
            else:
                while temp.next:
                    # checking for the whole linked list except the head
                    if temp.next.priority > node.priority or temp.next is None:
                        node.next = temp.next
                        temp.next = node
                        break
                    else:
                        temp = temp.next
                # adding the highest priority node to the end
                if node.next is None:
                    temp.next = node

    def dequeue(self):
        temp = self.llist.head
        if temp is not None:
            self.llist.head = temp.next
            del temp.data
            del temp.priority

    def display(self):
        temp = self.llist.head
        while temp is not None:
            print(temp.data)
            temp = temp.next


obj = PriorityQueue()
obj.enqueue(34, 4)
obj.enqueue(65, 2)
obj.enqueue(77, 3)
obj.enqueue(20, 1)
obj.enqueue(78, 8)
obj.enqueue(5, 7)
obj.enqueue(4, 6)
obj.enqueue(88, 5)
obj.display()
print("")
obj.dequeue()
obj.dequeue()
obj.display()
