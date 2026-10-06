class Booking:
    def __init__(self, booking_id, customer, movie, seats):
        self.booking_id = booking_id
        self.customer = customer
        self.movie = movie
        self.seats = seats


class MovieSystem:
    def __init__(self):
        self.bookings = []

    def add_booking(self):
        bid = int(input("Enter Booking ID: "))
        customer = input("Enter Customer Name: ")
        movie = input("Enter Movie Name: ")
        seats = int(input("Enter Number of Seats: "))

        self.bookings.append(
            Booking(bid, customer, movie, seats)
        )

    def quick_sort(self, low, high):
        if low < high:
            p = self.partition(low, high)
            self.quick_sort(low, p - 1)
            self.quick_sort(p + 1, high)

    def partition(self, low, high):
        pivot = self.bookings[high].movie
        i = low - 1

        for j in range(low, high):
            if self.bookings[j].movie.lower() <= pivot.lower():
                i += 1
                self.bookings[i], self.bookings[j] = \
                    self.bookings[j], self.bookings[i]

        self.bookings[i + 1], self.bookings[high] = \
            self.bookings[high], self.bookings[i + 1]

        return i + 1

    def display(self):
        print("\nID  Customer  Movie  Seats")

        for b in self.bookings:
            print(b.booking_id, b.customer,
                  b.movie, b.seats)


system = MovieSystem()

n = int(input("Enter number of bookings: "))

for i in range(n):
    print("\nBooking", i + 1)
    system.add_booking()

print("\nBefore Sorting:")
system.display()

system.quick_sort(0, len(system.bookings) - 1)

print("\nAfter Sorting by Movie:")
system.display()