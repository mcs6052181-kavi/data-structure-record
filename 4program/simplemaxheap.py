class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)

        i = len(self.heap) - 1

        while i > 0:
            parent = (i - 1) // 2

            if self.heap[i] > self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def delete(self):
        if not self.heap:
            print("Heap is empty")
            return

        deleted = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last

            i = 0

            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                largest = i

                if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                    largest = left

                if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                    largest = right

                if largest == i:
                    break

                self.heap[i], self.heap[largest] = \
                    self.heap[largest], self.heap[i]

                i = largest

        print("Deleted:", deleted)

    def display(self):
        print("Heap:", self.heap)


h = MaxHeap()

while True:

    print("\n--- MAX HEAP ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        h.insert(value)

    elif choice == 2:
        h.delete()

    elif choice == 3:
        h.display()

    elif choice == 4:
        print("Program ended")
        break

    else:
        print("Invalid choice")