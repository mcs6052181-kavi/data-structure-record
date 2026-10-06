class TextEditor:
    def __init__(self):
        self.stack = []

    def write(self):
        text = input("Enter text: ")
        self.stack.append(text)
        print("Text Added")

    def undo(self):
        if self.stack:
            print("Undo:", self.stack.pop())
        else:
            print("Nothing to Undo")

    def last(self):
        if self.stack:
            print("Last Text:", self.stack[-1])


t = TextEditor()

while True:
    print("\n1.Write  2.Undo  3.Last  4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        t.write()
    elif ch == 2:
        t.undo()
    elif ch == 3:
        t.last()
    elif ch== 4:
        print("Exited")
    else:
        break