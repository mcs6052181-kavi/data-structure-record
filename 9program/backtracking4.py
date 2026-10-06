class NQueens:

    def __init__(self):
        self.n = 0
        self.board = []
        self.count = 0

    def create_board(self):
        self.n = int(input("Enter number of queens: "))
        self.board = [-1] * self.n
        self.count = 0

    def is_safe(self, row, col):

        for i in range(row):

            if self.board[i] == col:
                return False

            if abs(self.board[i] - col) == abs(i - row):
                return False

        return True

    def solve(self, row):

        if row == self.n:

            self.count += 1

            print("\nSolution", self.count)

            for i in range(self.n):

                for j in range(self.n):

                    if self.board[i] == j:
                        print("Q", end=" ")
                    else:
                        print(".", end=" ")

                print()

            return

        for col in range(self.n):

            if self.is_safe(row, col):

                self.board[row] = col

                self.solve(row + 1)

                self.board[row] = -1

    def display_solutions(self):

        if self.n == 0:
            print("Enter N first.")
            return

        self.solve(0)

        print("\nTotal Solutions:", self.count)


obj = NQueens()

while True:

    print("\n--- N QUEENS ---")
    print("1. Enter N")
    print("2. Display Solutions")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        obj.create_board()

    elif choice == 2:
        obj.display_solutions()

    elif choice == 3:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")