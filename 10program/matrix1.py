class JobAllocation:

    def __init__(self, cost):
        self.cost = cost
        self.n = len(cost)
        self.best_cost = float("inf")
        self.best_assignment = []

    def calculate_bound(self, employee, assigned):
        bound = 0

        for i in range(employee, self.n):
            minimum = float("inf")

            for j in range(self.n):
                if j not in assigned:
                    minimum = min(minimum, self.cost[i][j])

            bound += minimum

        return bound

    def solve(self, employee, assigned, current_cost, assignment):

        if employee == self.n:

            if current_cost < self.best_cost:
                self.best_cost = current_cost
                self.best_assignment = assignment.copy()

            return

        bound = self.calculate_bound(employee, assigned)

        if current_cost + bound >= self.best_cost:
            return

        for job in range(self.n):

            if job not in assigned:

                assignment.append(job)
                assigned.add(job)

                self.solve(
                    employee + 1,
                    assigned,
                    current_cost + self.cost[employee][job],
                    assignment
                )

                assignment.pop()
                assigned.remove(job)

    def display(self):

        print("\nMinimum Cost:", self.best_cost)

        print("\nEmployee -> Job")

        for employee in range(self.n):
            print(
                "Employee", employee + 1,
                "-> Job", self.best_assignment[employee] + 1,
                "Cost =", self.cost[employee][self.best_assignment[employee]]
            )


n = int(input("Enter number of employees/jobs: "))

cost = []

print("\nEnter cost matrix:")

for i in range(n):
    row = list(map(int, input(
        "Enter costs for Employee " + str(i + 1) + ": "
    ).split()))

    cost.append(row)

system = JobAllocation(cost)

system.solve(0, set(), 0, [])

system.display()