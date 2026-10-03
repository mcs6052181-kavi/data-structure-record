stack = []

while True:
    print("\n--- TEXT EDITOR ---")
    print("1. Add Action")
    print("2. Undo")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        action = input("Enter action: ")
        stack.append(action)
        print("Action added.")

    elif choice == 2:
        if stack:
            print("Undo:", stack.pop())
        else:
            print("Stack is empty.")

    elif choice == 3:
        if stack:
            print("Latest action:", stack[-1])
        else:
            print("Stack is empty.")

    elif choice == 4:
        print("Actions:", stack)

    elif choice == 5:
        break

    else:
        print("Invalid choice")
