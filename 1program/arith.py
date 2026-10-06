class ExpressionStack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()


class Calculator:
    def evaluate(self, expression):
        stack = ExpressionStack()

        for item in expression.split():
            if item.isdigit():
                stack.push(int(item))
            else:
                b = stack.pop()
                a = stack.pop()

                if item == '+':
                    stack.push(a + b)
                elif item == '-':
                    stack.push(a - b)
                elif item == '*':
                    stack.push(a * b)
                elif item == '/':
                    stack.push(a / b)

        return stack.pop()


expression = input("Enter expression with spaces: ")

calc = Calculator()
result = calc.evaluate(expression)

print("Result:", result)