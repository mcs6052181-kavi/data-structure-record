class MovieBooking:

    def __init__(self, booking_id, name, movie):
        self.booking_id = booking_id
        self.name = name
        self.movie = movie

    def display(self):
        print(self.booking_id, self.name, self.movie)


def quick_sort(bookings):

    if len(bookings) <= 1:
        return bookings

    pivot = bookings[0].booking_id

    left = []
    middle = []
    right = []

    for b in bookings:
        if b.booking_id < pivot:
            left.append(b)
        elif b.booking_id == pivot:
            middle.append(b)
        else:
            right.append(b)

    return quick_sort(left) + middle + quick_sort(right)


bookings = []

n = int(input("Enter number of bookings: "))

for i in range(n):

    print("\nBooking", i + 1)

    bid = int(input("Enter Booking ID: "))
    name = input("Enter Customer Name: ")
    movie = input("Enter Movie Name: ")

    bookings.append(
        MovieBooking(bid, name, movie)
    )

print("\nBefore Sorting:")

for b in bookings:
    b.display()

bookings = quick_sort(bookings)

print("\nAfter Quick Sort:")

for b in bookings:
    b.display()