# program to check if a tree is a BST

# method 1


def isBST_check_1(root):
    # if root is null
    if root is None:
        return True
    # is left subtree of the root
    if root.left is not None and root.data < maxValue(root.left):
        return False
    # if right subtree of the root
    if root.right is not None and root.data > minValue(root.right):
        return False
    # if the left subtree or right subtree is not a bst
    if not isBST_check_1(root.left) or not isBST_check_1(root.right):
        return False

    # if passes all the conditions
    return True


def minValue(root):
    data = None
    while(root):
        data = root.data
        root = root.left
    return data


def maxValue(root):
    data = None
    while(root):
        data = root.data
        root = root.right
    return data

