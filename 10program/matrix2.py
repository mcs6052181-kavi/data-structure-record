class Employee:

    def __init__(self, name):
        self.name = name


class JobAllocation:

    def __init__(self, employees, jobs, cost):
        self.employees = employees
        self.jobs = jobs
        self.cost = cost
        self.n = len(employees)

        self.best_cost = float("inf")
        self.best = []

    def bound(self, row, used):

        total = 0

        for i in range(row, self.n):

            minimum = float("inf")

            for j in range(self.n):

                if j not in used:
                    minimum = min(minimum, self.cost[i][j])

            total += minimum

        return total

    def branch(self, row, used, current, result):

        if row == self.n:

            if current < self.best_cost:
                self.best_cost = current
                self.best = result.copy()

            return

        if current + self.bound(row, used) >= self.best_cost:
            return

        for job in range(self.n):

            if job not in used:

                used.add(job)
                result.append(job)

                self.branch(
                    row + 1,
                    used,
                    current + self.cost[row][job],
                    result
                )

                result.pop()
                used.remove(job)

    def display(self):

        print("\n--- OPTIMAL JOB ALLOCATION ---")

        for i in range(self.n):

            job = self.best[i]

            print(
                self.employees[i],
                "->",
                self.jobs[job],
                "Cost =", self.cost[i][job]
            )

        print("\nMinimum Total Cost:", self.best_cost)


n = int(input("Enter number of employees: "))

employees = []
jobs = []

for i in range(n):
    employees.append(input("Enter Employee " + str(i + 1) + " name: "))

for i in range(n):
    jobs.append(input("Enter Job " + str(i + 1) + " name: "))

cost = []

print("\nEnter Cost Matrix:")

for i in range(n):

    row = list(map(int, input(
        "Cost for " + employees[i] + ": "
    ).split()))

    cost.append(row)

system = JobAllocation(employees, jobs, cost)

system.branch(0, set(), 0, [])

system.display()