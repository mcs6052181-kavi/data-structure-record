class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class ExpressionTree:
    def build_tree(self, postfix):
        stack = []

        for symbol in postfix.split():
            node = Node(symbol)

            if symbol in "+-*/":
                node.right = stack.pop()
                node.left = stack.pop()

            stack.append(node)

        return stack.pop()

    def evaluate(self, root):
        if root.left is None and root.right is None:
            return float(root.value)

        left = self.evaluate(root.left)
        right = self.evaluate(root.right)

        if root.value == "+":
            return left + right

        if root.value == "-":
            return left - right

        if root.value == "*":
            return left * right

        if root.value == "/":
            return left / right

    def inorder(self, root):
        if root:
            if root.left:
                print("(", end=" ")

            self.inorder(root.left)
            print(root.value, end=" ")
            self.inorder(root.right)

            if root.right:
                print(")", end=" ")


postfix = input("Enter postfix expression: ")

tree = ExpressionTree()
root = tree.build_tree(postfix)

print("\nExpression:")
tree.inorder(root)

print("\n\nEvaluation:", tree.evaluate(root))