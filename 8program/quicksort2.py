class Booking:
    def __init__(self, booking_id, name, movie, seats):
        self.booking_id = booking_id
        self.name = name
        self.movie = movie
        self.seats = seats

    def display(self):
        print(self.booking_id, self.name, self.movie, self.seats)


class BookingSystem:
    def __init__(self):
        self.bookings = []

    def add_booking(self):
        booking_id = int(input("Enter Booking ID: "))
        name = input("Enter Customer Name: ")
        movie = input("Enter Movie Name: ")
        seats = int(input("Enter Seats: "))

        self.bookings.append(
            Booking(booking_id, name, movie, seats)
        )

    def partition(self, low, high):
        pivot = self.bookings[high].name
        i = low - 1

        for j in range(low, high):
            if self.bookings[j].name.lower() <= pivot.lower():
                i += 1
                self.bookings[i], self.bookings[j] = \
                    self.bookings[j], self.bookings[i]

        self.bookings[i + 1], self.bookings[high] = \
            self.bookings[high], self.bookings[i + 1]

        return i + 1

    def quick_sort(self, low, high):
        if low < high:
            p = self.partition(low, high)
            self.quick_sort(low, p - 1)
            self.quick_sort(p + 1, high)

    def display(self):
        for b in self.bookings:
            b.display()


system = BookingSystem()

n = int(input("Enter number of bookings: "))

for i in range(n):
    print("\nBooking", i + 1)
    system.add_booking()

print("\nBefore Sorting:")
system.display()

system.quick_sort(0, len(system.bookings) - 1)

print("\nSorted by Customer Name:")
system.display()