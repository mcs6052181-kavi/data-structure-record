class NQueens:

    def __init__(self, n):
        self.n = n
        self.board = [["."] * n for i in range(n)]
        self.count = 0

    def is_safe(self, row, col):

        # Check column
        for i in range(row):
            if self.board[i][col] == "Q":
                return False

        # Check left diagonal
        i = row - 1
        j = col - 1

        while i >= 0 and j >= 0:
            if self.board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        # Check right diagonal
        i = row - 1
        j = col + 1

        while i >= 0 and j < self.n:
            if self.board[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True

    def solve(self, row):

        if row == self.n:
            self.count += 1

            print("\nSolution", self.count)

            for row in self.board:
                print(" ".join(row))

            return

        for col in range(self.n):

            if self.is_safe(row, col):

                self.board[row][col] = "Q"

                self.solve(row + 1)

                self.board[row][col] = "."


n = int(input("Enter number of queens: "))

obj = NQueens(n)
obj.solve(0)

print("\nTotal Solutions:", obj.count)