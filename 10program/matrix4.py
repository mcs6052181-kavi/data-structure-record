class JobAllocation:

    def __init__(self, cost):
        self.cost = cost
        self.n = len(cost)

        self.minimum = float("inf")
        self.answer = []

    def solve(self, employee, used, total, allocation):

        if employee == self.n:

            if total < self.minimum:
                self.minimum = total
                self.answer = allocation.copy()

            return

        for job in range(self.n):

            if job not in used:

                new_cost = total + self.cost[employee][job]

                if new_cost < self.minimum:

                    used.add(job)
                    allocation.append(job)

                    self.solve(
                        employee + 1,
                        used,
                        new_cost,
                        allocation
                    )

                    allocation.pop()
                    used.remove(job)

    def display(self):

        print("\nBest Allocation:")

        for i in range(self.n):

            print(
                "Employee", i + 1,
                "-> Job", self.answer[i] + 1
            )

        print("Minimum Cost:", self.minimum)


n = int(input("Enter number of employees/jobs: "))

cost = []

for i in range(n):

    row = list(map(int, input(
        "Enter cost for Employee " + str(i + 1) + ": "
    ).split()))

    cost.append(row)

obj = JobAllocation(cost)

obj.solve(0, set(), 0, [])

obj.display()