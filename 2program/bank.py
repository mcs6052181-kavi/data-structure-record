class Bank:
    def __init__(self):
        self.queue = []

    def add(self):
        name = input("Enter customer name: ")
        self.queue.append(name)

    def remove(self):
        if self.queue:
            print("Serving:", self.queue.pop(0))
        else:
            print("Queue Empty")

    def display(self):
        print("Customers:", self.queue)


b = Bank()

while True:
    print("\n1.Add  2.Serve  3.Display  4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        b.add()
    elif ch == 2:
        b.remove()
    elif ch == 3:
        b.display()
    elif ch == 4:    
        print("excited")
    else:
        break