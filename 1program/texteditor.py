class TextEditor:
    
    def __init__(self):
        self.stack = []

    def add_action(self):
        action = input("Enter action: ")
        self.stack.append(action)
        print("Action added.")

    def undo(self):
        if len(self.stack) > 0:
            print("Undo:", self.stack.pop())
        else:
            print("Stack is empty.")

    def peek(self):
        if len(self.stack) > 0:
            print("Latest action:", self.stack[-1])
        else:
            print("Stack is empty.")

    def display(self):
        if len(self.stack) > 0:
            print("Actions:", self.stack)
        else:
            print("Stack is empty.")

    def menu(self):
        print("\n--- TEXT EDITOR ---")
        print("1. Add Action")
        print("2. Undo")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")


# Create object
editor = TextEditor()

while True:
    editor.menu()

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        editor.add_action()

    elif choice == "2":
        editor.undo()

    elif choice == "3":
        editor.peek()

    elif choice == "4":
        editor.display()

    elif choice == "5":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")