class Knapsack:
    def __init__(self):
        self.items = []

    def add_item(self, weight, profit):
        ratio = profit / weight
        self.items.append((weight, profit, ratio))

    def solve(self, capacity):
        self.items.sort(key=lambda x: x[2], reverse=True)

        total_profit = 0

        for weight, profit, ratio in self.items:

            if capacity >= weight:
                capacity -= weight
                total_profit += profit

                print("Taken item:", weight, profit)

            else:
                fraction = capacity / weight
                total_profit += profit * fraction

                print("Taken fraction:", round(fraction, 2))

                capacity = 0
                break

        print("Maximum Profit:", total_profit)


k = Knapsack()

n = int(input("Enter number of items: "))

for i in range(n):
    weight = int(input("Enter weight: "))
    profit = int(input("Enter profit: "))

    k.add_item(weight, profit)

capacity = int(input("Enter knapsack capacity: "))

k.solve(capacity)