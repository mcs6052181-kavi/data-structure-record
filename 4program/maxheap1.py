class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1

        while i > 0:
            parent = (i - 1) // 2

            if self.heap[parent] < self.heap[i]:
                self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
                i = parent
            else:
                break

    def delete(self):
        if len(self.heap) == 0:
            print("Heap is empty")
            return

        root = self.heap[0]
        last = self.heap.pop()

        if len(self.heap) > 0:
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

                if largest != i:
                    self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                    i = largest
                else:
                    break

        print("Deleted:", root)

    def display(self):
        print("Heap:", self.heap)


h = MaxHeap()

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter value: "))
    h.insert(value)

h.display()

h.delete()

h.display()