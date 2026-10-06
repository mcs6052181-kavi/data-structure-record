class BookStack:
    def __init__(self):
        self.stack = []

    def push(self, book):
        self.stack.append(book)
        print(book, "added")

    def pop(self):
        if not self.stack:
            print("Stack is empty")
        else:
            print(self.stack.pop(), "removed")

    def peek(self):
        if not self.stack:
            print("Stack is empty")
        else:
            print("Top book:", self.stack[-1])

    def display(self):
        print("Books:", self.stack)


b = BookStack()

while True:
    print("\n--- BOOK STACK ---")
    print("1. Push Book")
    print("2. Pop Book")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        b.push(book)
    elif choice == 2:
        b.pop()
    elif choice == 3:
        b.peek()
    elif choice == 4:
        b.display()
    elif choice == 5:
        break
    else:
        print("Invalid choice")