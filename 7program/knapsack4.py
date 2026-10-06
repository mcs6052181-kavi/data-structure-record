class Item:
    def __init__(self, weight, profit):
        self.weight = weight
        self.profit = profit
        self.ratio = profit / weight


class Knapsack:
    def solve(self, items, capacity):

        items.sort(key=lambda x: x.ratio, reverse=True)

        total_profit = 0

        print("\nItems selected:")

        for item in items:

            if item.weight <= capacity:

                capacity -= item.weight
                total_profit += item.profit

                print(
                    "Weight:", item.weight,
                    "Profit:", item.profit
                )

            else:

                fraction = capacity / item.weight

                total_profit += item.profit * fraction

                print(
                    "Weight:", capacity,
                    "Fraction:", round(fraction, 2)
                )

                break

        print("\nMaximum Profit:", total_profit)


items = []

n = int(input("Enter number of items: "))

for i in range(n):

    weight = int(input("Enter weight: "))
    profit = int(input("Enter profit: "))

    items.append(Item(weight, profit))

capacity = int(input("Enter capacity: "))

k = Knapsack()

k.solve(items, capacity)