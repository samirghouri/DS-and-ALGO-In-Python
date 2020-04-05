class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list_data(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


# made an empty linkedlist
llist = LinkedList()
# assigning node_1 as head
llist.head = Node(1)
second = Node(2)
third = Node(3)

# llist.head        second              third
#      |                |                  |
#      |                |                  |
# +----+------+     +----+------+     +----+------+
# | 1  | None |     | 2  | None |     |  3 | None |
# +----+------+     +----+------+     +----+------+

llist.head.next = second

#  Now next of first Node refers to second.  So they
#     both are linked.

#     llist.head        second              third
#          |                |                  |
#          |                |                  |
#     +----+------+     +----+------+     +----+------+
#     | 1  |  o-------->| 2  | null |     |  3 | null |
#     +----+------+     +----+------+     +----+------+

second.next = third

#  Now next of second Node refers to third.  So all three
#     nodes are linked.

#     llist.head        second              third
#          |                |                  |
#          |                |                  |
#     +----+------+     +----+------+     +----+------+
#     | 1  |  o-------->| 2  |  o-------->|  3 | null |
#     +----+------+     +----+------+     +----+------+
llist.print_list_data()
