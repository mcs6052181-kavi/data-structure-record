class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class ExpressionTree:
    def build(self, expression):
        stack = []

        for item in expression.split():
            if item.isdigit():
                stack.append(Node(item))
            else:
                node = Node(item)
                node.right = stack.pop()
                node.left = stack.pop()
                stack.append(node)

        return stack.pop()

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


tree = ExpressionTree()

expression = input("Enter postfix expression with spaces: ")

root = tree.build(expression)

print("\nInorder:")
tree.inorder(root)

print("\nPreorder:")
tree.preorder(root)

print("\nPostorder:")
tree.postorder(root)

print("\nResult:", tree.evaluate(root))