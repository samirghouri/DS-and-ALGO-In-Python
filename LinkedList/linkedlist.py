
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is not None:
            node = self.head
            while(node):
                print(node.data)
                node = node.next
        else:
            return None

    def lenght(self):
        count = 0
        if self.head is not None:
            node = self.head
            while(node):
                count += 1
                node = node.next
        return count

    def append_in_beginning(self, data):
        """
        Definition to append at the beginning of the linkedlist
        """
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def append_in_end(self, data):
        """
        Definition to append at the end of the linkedlist
        """
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            temp_node = self.head
            while(temp_node):
                if temp_node.next is None:
                    temp_node.next = node
                    break
                temp_node = temp_node.next

    def append_at_postition(self, data, n):
        """
        Definition to append at a specified postion in linkedlist(n starts from 0)
        """
        lenght = self.lenght()
        if n > lenght:
            return
        node = Node(data)
        ''' head-> node1 -> node2 -> node3 -> node4 -> node5
        '''
        # store  the head
        temp = self.head

        # if the postion is the start
        if n == 0:
            self.head = node
            node.next = temp
            return

        for i in range(n-1):
            temp = temp.next

        # now the new node will be added to temp.next

        next = temp.next
        temp.next = node
        node.next = next

    def delete_node(self, n):
        """
        Definition to delete a node at nth position (n starts with 0)
        """
        length = self.lenght()
        if n > length-1:
            return
        # store head node
        temp_node = self.head

        # if head needs to be removed
        if n == 0:
            self.head = temp_node.next
            temp_node = None
            return
        """
        self.head -> n1 -> n2 -> n3 -> n4
                     0      1     2     3 
        """
        # Find the previous node of the node to be deleted
        for i in range(n-1):
            temp_node = temp_node.next
            if temp_node is None:
                break
        # temp_node.next is the node to be deleted
        # we store the rest of the node after temp_node.next in next
        next = temp_node.next.next

        temp_node.next = None
        temp_node.next = next


llist = Linkedlist()
llist.append_in_beginning(44)
llist.append_in_beginning(77)
llist.append_in_beginning(99)
llist.append_in_beginning(0)
llist.append_in_end(1)
llist.append_at_postition(5, 0)
llist.display()
print()
llist.delete_node(4)
llist.display()
