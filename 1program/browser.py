class Browser:

    def __init__(self):
        self.stack = []

    # Push operation
    def visit(self):
        page = input("Enter website: ")
        self.stack.append(page)
        print("Website visited:", page)

    # Pop operation
    def back(self):
        if len(self.stack) > 1:
            page = self.stack.pop()
            print("Going back from:", page)
            print("Current page:", self.stack[-1])
        elif len(self.stack) == 1:
            print("No previous page.")
        else:
            print("Browser history is empty.")

    # Peek operation
    def current(self):
        if len(self.stack) > 0:
            print("Current page:", self.stack[-1])
        else:
            print("Browser history is empty.")

    # Display stack
    def display(self):
        if len(self.stack) == 0:
            print("Browser history is empty.")
        else:
            print("\nBrowser History:")
            for i in range(len(self.stack) - 1, -1, -1):
                print(self.stack[i])


# Create Browser object
browser = Browser()

while True:

    print("\n==============================")
    print("       BROWSER HISTORY")
    print("==============================")
    print("1. Visit Website")
    print("2. Back")
    print("3. Current Page")
    print("4. Display History")
    print("5. Exit")
    print("==============================")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        browser.visit()

    elif choice == "2":
        browser.back()

    elif choice == "3":
        browser.current()

    elif choice == "4":
        browser.display()

    elif choice == "5":
        print("Exiting Browser...")
        break

    else:
        print("Invalid choice. Please enter 1 to 5.")