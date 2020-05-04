# Implementing the binary search tree
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BST:
    def __init__(self):
        pass

    def insert(self, root, node):
        # if the root is empty
        if root is None:
            root = node
        # if root not empty
        else:
            if node.data < root.data:
                if root.left is None:
                    root.left = node
                else:
                    self.insert(root.left, node)
            elif node.data >= root.data:
                if root.right is None:
                    root.right = node
                else:
                    self.insert(root.right, node)

    def search(self, root, key):
        # condition to stop out recursion
        if root.data == key:
            return root
        if key < root.data:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def inorder_traversal(self, root):
        # some inorder traversal
        if root is not None:
            self.inorder_traversal(root.left)
            print(root.data)
            self.inorder_traversal(root.right)

    def preorder_traversal(self, root):
        # some preorder traversal
        if root is not None:
            print(root.data)
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        if root is not None:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.data)


node1 = Node(5)
node2 = Node(6)
node3 = Node(9)
node4 = Node(1)
node5 = Node(2)
node6 = Node(10)
obj = BST()
root = node1
obj.insert(root, node2)
obj.insert(root, node3)
obj.insert(root, node4)
obj.insert(root, node5)
obj.insert(root, node6)
print(obj.search(root, 10))
# obj.inorder_traversal(root)
# obj.preorder_traversal(root)
obj.postorder_traversal(root)

