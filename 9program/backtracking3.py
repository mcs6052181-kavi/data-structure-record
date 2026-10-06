class QueenProblem:

    def __init__(self, n):
        self.n = n
        self.board = [-1] * n
        self.solutions = []

    def safe(self, row, col):

        for previous_row in range(row):

            previous_col = self.board[previous_row]

            if previous_col == col:
                return False

            if abs(previous_col - col) == abs(previous_row - row):
                return False

        return True

    def backtrack(self, row):

        if row == self.n:

            solution = self.board.copy()
            self.solutions.append(solution)

            return

        for col in range(self.n):

            if self.safe(row, col):

                self.board[row] = col

                self.backtrack(row + 1)

                self.board[row] = -1

    def display(self):

        for number, solution in enumerate(self.solutions, 1):

            print("\nSolution", number)

            for row in range(self.n):

                for col in range(self.n):

                    if solution[row] == col:
                        print("Q", end=" ")
                    else:
                        print(".", end=" ")

                print()


n = int(input("Enter N: "))

obj = QueenProblem(n)

obj.backtrack(0)

obj.display()

print("\nTotal Solutions:", len(obj.solutions))