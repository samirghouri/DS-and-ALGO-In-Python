class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def append_to_list(self, data):
        """
        Definition to simply append to the linkedlist
        """
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        temp = self.head
        while(temp):
            if temp.next is None:
                temp.next = node
                break
            temp = temp.next

    def display(self):
        """
        Definition to display the linkedlist
        """
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def reverse_llist_iteration(self):
        """
        Definition to reverse a linkedlist
        """
        # self.head -> node1 -> node2 - > node3 -> node4 -> None
        # self.head -> node4 -> node3 -> node2 -> node1 -> None

        old_link = self.head
        list_of_nodes = list()
        new_link = None
        # adding all the nodes in a list
        while(old_link):
            temp = old_link
            list_of_nodes.append(temp)
            old_link = old_link.next
        list_of_nodes = list_of_nodes[::-1]
        # breaking the link of each node
        for each_node in list_of_nodes:
            each_node.next = None
        # linking all the node with each other
        for i in range(len(list_of_nodes)-1):
            list_of_nodes[i].next = list_of_nodes[i+1]
        self.head = list_of_nodes[0]

    def reverse_llist_recursive(self):
        """
        Definiton to reverse a linkedlist using recursion
        """
        # self.head -> node1 -> node2 - > node3 -> node4 -> None
        # self.head -> node4 -> node3 -> node2 -> node1 -> None

        if self.head is None:
            return
        self.recursion_util(self.head, None)

    def recursion_util(self, curr, prev):

       # If last node mark it head
        if curr.next is None:
            self.head = curr

            # Update next to prev node
            curr.next = prev
            return

        # Save curr.next node for recursive call
        next = curr.next

        # And update next
        curr.next = prev

        self.recursion_util(next, curr)


llist = Linkedlist()
llist.append_to_list(5)
llist.append_to_list(99)
llist.append_to_list(77)
llist.append_to_list(22)
llist.append_to_list(00)
llist.display()
print()
# llist.reverse_llist_iteration()
llist.reverse_llist_recursive()
llist.display()
