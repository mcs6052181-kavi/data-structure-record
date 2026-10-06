class JobAllocation:

    def __init__(self, cost):
        self.cost = cost
        self.best_cost = 999999
        self.best = []

    def solve(self, employee, used, total, allocation):

        if employee == 3:

            if total < self.best_cost:
                self.best_cost = total
                self.best = allocation.copy()

            return

        for job in range(3):

            if job not in used:

                used.add(job)
                allocation.append(job)

                self.solve(
                    employee + 1,
                    used,
                    total + self.cost[employee][job],
                    allocation
                )

                allocation.pop()
                used.remove(job)

    def display(self):

        print("\nEmployee  Job  Cost")

        for i in range(3):

            job = self.best[i]

            print(
                i + 1,
                "       ",
                job + 1,
                "   ",
                self.cost[i][job]
            )

        print("\nMinimum Cost:", self.best_cost)


cost = [
    [9, 2, 7],
    [6, 4, 3],
    [5, 8, 1]
]

system = JobAllocation(cost)

system.solve(0, set(), 0, [])

system.display()