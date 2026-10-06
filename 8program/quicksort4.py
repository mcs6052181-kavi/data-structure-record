class Booking:
    def __init__(self, bid, name, movie, seats):
        self.bid = bid
        self.name = name
        self.movie = movie
        self.seats = seats

    def display(self):
        print(self.bid, self.name, self.movie, self.seats)


class MovieTicketSystem:

    def __init__(self):
        self.bookings = []

    def add_booking(self):
        bid = int(input("Enter Booking ID: "))
        name = input("Enter Customer Name: ")
        movie = input("Enter Movie Name: ")
        seats = int(input("Enter Seats: "))

        self.bookings.append(
            Booking(bid, name, movie, seats)
        )

        print("Booking added successfully.")

    def display(self):
        if len(self.bookings) == 0:
            print("No bookings available.")
            return

        print("\nID  Name  Movie  Seats")

        for b in self.bookings:
            b.display()

    def quick_sort(self, low, high):
        if low < high:
            p = self.partition(low, high)
            self.quick_sort(low, p - 1)
            self.quick_sort(p + 1, high)

    def partition(self, low, high):
        pivot = self.bookings[high].bid
        i = low - 1

        for j in range(low, high):
            if self.bookings[j].bid <= pivot:
                i += 1
                self.bookings[i], self.bookings[j] = \
                    self.bookings[j], self.bookings[i]

        self.bookings[i + 1], self.bookings[high] = \
            self.bookings[high], self.bookings[i + 1]

        return i + 1

    def sort(self):
        if len(self.bookings) > 0:
            self.quick_sort(0, len(self.bookings) - 1)
            print("Bookings sorted successfully.")


system = MovieTicketSystem()

while True:

    print("\n--- MOVIE TICKET BOOKING SYSTEM ---")
    print("1. Add Booking")
    print("2. Display Bookings")
    print("3. Sort using Quick Sort")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        system.add_booking()

    elif choice == 2:
        system.display()

    elif choice == 3:
        system.sort()

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice.")