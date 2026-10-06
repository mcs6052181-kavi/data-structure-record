import heapq

heap = []

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter value: "))
    heapq.heappush(heap, value)

print("Heap after insertion:", heap)

deleted = heapq.heappop(heap)

print("Deleted element:", deleted)

print("Heap after deletion:", heap)