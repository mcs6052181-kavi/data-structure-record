class CircularQueue:

    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full.")
            return

        name = input("Enter patient name: ")

        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = name
        print("Patient added.")

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty.")
            return

        print("Serving patient:", self.queue[self.front])

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

    def peek(self):
        if self.front == -1:
            print("Queue is empty.")
        else:
            print("Next patient:", self.queue[self.front])

    def display(self):
        if self.front == -1:
            print("Queue is empty.")
            return

        print("Patients:")

        i = self.front

        while True:
            print(self.queue[i])

            if i == self.rear:
                break

            i = (i + 1) % self.size


hospital = CircularQueue(5)

while True:
    print("\n--- HOSPITAL QUEUE ---")
    print("1. Add Patient")
    print("2. Serve Patient")
    print("3. Next Patient")
    print("4. Display Patients")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        hospital.enqueue()
    elif choice == "2":
        hospital.dequeue()
    elif choice == "3":
        hospital.peek()
    elif choice == "4":
        hospital.display()
    elif choice == "5":
        break
    else:
        print("Invalid choice.")