class TicketQueue:

    def __init__(self):
        self.queue = []

    def enqueue(self):
        name = input("Enter customer name: ")
        self.queue.append(name)
        print("Customer added.")

    def dequeue(self):
        if len(self.queue) > 0:
            print("Serving:", self.queue.pop(0))
        else:
            print("Queue is empty.")

    def peek(self):
        if len(self.queue) > 0:
            print("Next customer:", self.queue[0])
        else:
            print("Queue is empty.")

    def display(self):
        print("Queue:", self.queue)


q = TicketQueue()

while True:
    print("\n--- TICKET COUNTER ---")
    print("1. Add Customer")
    print("2. Serve Customer")
    print("3. Next Customer")
    print("4. Display Queue")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        q.enqueue()
    elif choice == "2":
        q.dequeue()
    elif choice == "3":
        q.peek()
    elif choice == "4":
        q.display()
    elif choice == "5":
        break
    else:
        print("Invalid choice.")