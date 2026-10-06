class PrinterQueue:

    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.front = -1
        self.rear = -1

    def enqueue(self):
        if self.rear == self.size - 1:
            print("Queue is full.")
            return

        job = input("Enter print job: ")

        if self.front == -1:
            self.front = 0

        self.rear += 1
        self.queue[self.rear] = job

        print("Print job added.")

    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue is empty.")
        else:
            print("Printing:", self.queue[self.front])
            self.front += 1

    def display(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue is empty.")
        else:
            print("Print Queue:")

            for i in range(self.front, self.rear + 1):
                print(self.queue[i])


q = PrinterQueue(5)

while True:
    print("\n--- PRINTER QUEUE ---")
    print("1. Add Print Job")
    print("2. Print Job")
    print("3. Display Queue")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        q.enqueue()
    elif choice == "2":
        q.dequeue()
    elif choice == "3":
        q.display()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")