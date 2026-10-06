class NQueens:

    def __init__(self, n):
        self.n = n
        self.board = [-1] * n
        self.count = 0

    def safe(self, row, col):

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

                print(" ".join(
                    "Q" if self.board[i] == j else "."
                    for j in range(self.n)
                ))

            return

        for col in range(self.n):

            if self.safe(row, col):

                self.board[row] = col

                self.solve(row + 1)

                self.board[row] = -1


n = int(input("Enter number of queens: "))

queens = NQueens(n)

queens.solve(0)

print("\nTotal number of solutions:", queens.count)