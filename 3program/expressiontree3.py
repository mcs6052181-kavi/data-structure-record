class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def create(self):
        self.root = Node(1)

        self.root.left = Node(2)
        self.root.right = Node(3)

        self.root.left.left = Node(4)
        self.root.left.right = Node(5)

        self.root.right.left = Node(6)
        self.root.right.right = Node(7)

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


class ExpressionTree:
    def build(self, postfix):
        stack = []

        for item in postfix.split():
            node = Node(item)

            if item in "+-*/":
                node.right = stack.pop()
                node.left = stack.pop()

            stack.append(node)

        return stack.pop()

    def evaluate(self, root):
        if root.left is None and root.right is None:
            return int(root.data)

        left = self.evaluate(root.left)
        right = self.evaluate(root.right)

        if root.data == "+":
            return left + right
        elif root.data == "-":
            return left - right
        elif root.data == "*":
            return left * right
        elif root.data == "/":
            return left / right


# Binary Tree
tree = BinaryTree()
tree.create()

print("----- BINARY TREE -----")

print("\n1. Inorder:")
tree.inorder(tree.root)

print("\n2. Preorder:")
tree.preorder(tree.root)

print("\n3. Postorder:")
tree.postorder(tree.root)


# Expression Tree
print("\n\n----- EXPRESSION TREE -----")

postfix = input("Enter postfix expression: ")

expression_tree = ExpressionTree()
root = expression_tree.build(postfix)

print("Expression Result:", expression_tree.evaluate(root))