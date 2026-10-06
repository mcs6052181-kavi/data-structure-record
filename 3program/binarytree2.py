class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def create_tree(self):
        value = input("Enter node value (or -1 for no node): ")

        if value == "-1":
            return None

        node = Node(value)

        print("Enter left child of", value)
        node.left = self.create_tree()

        print("Enter right child of", value)
        node.right = self.create_tree()

        return node

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")


tree = BinaryTree()

print("Create Binary Tree")
root = tree.create_tree()

print("\nInorder:")
tree.inorder(root)

print("\nPreorder:")
tree.preorder(root)

print("\nPostorder:")
tree.postorder(root)