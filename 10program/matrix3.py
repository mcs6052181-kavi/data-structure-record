class JobSystem:

    def __init__(self):
        self.n = 0
        self.cost = []
        self.best_cost = float("inf")
        self.best = []

    def input_data(self):

        self.n = int(input("Enter number of employees: "))

        print("\nEnter Cost Matrix:")

        for i in range(self.n):

            row = list(map(int, input(
                "Employee " + str(i + 1) + ": "
            ).split()))

            self.cost.append(row)

    def bound(self, row, used):

        total = 0

        for i in range(row, self.n):

            minimum = float("inf")

            for j in range(self.n):

                if j not in used:
                    minimum = min(minimum, self.cost[i][j])

            total += minimum

        return total

    def solve(self, row, used, total, result):

        if row == self.n:

            if total < self.best_cost:

                self.best_cost = total
                self.best = result.copy()

            return

        if total + self.bound(row, used) >= self.best_cost:
            return

        for job in range(self.n):

            if job not in used:

                used.add(job)
                result.append(job)

                self.solve(
                    row + 1,
                    used,
                    total + self.cost[row][job],
                    result
                )

                result.pop()
                used.remove(job)

    def display(self):

        print("\nOptimal Allocation:")

        for i in range(self.n):

            print(
                "Employee", i + 1,
                "-> Job", self.best[i] + 1,
                "Cost =", self.cost[i][self.best[i]]
            )

        print("Minimum Cost:", self.best_cost)


system = JobSystem()

while True:

    print("\n--- JOB ALLOCATION SYSTEM ---")
    print("1. Enter Cost Matrix")
    print("2. Find Minimum Cost")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:

        system.cost = []
        system.best = []
        system.best_cost = float("inf")

        system.input_data()

    elif choice == 2:

        if system.n == 0:
            print("Enter cost matrix first.")

        else:
            system.solve(0, set(), 0, [])
            system.display()

    elif choice == 3:

        print("Program ended.")
        break

    else:
        print("Invalid choice.")