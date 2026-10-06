class Knapsack:
    def solve(self, weights, profits, capacity):

        n = len(weights)

        dp = [[0] * (capacity + 1) for i in range(n + 1)]

        for i in range(1, n + 1):

            for w in range(capacity + 1):

                if weights[i - 1] <= w:

                    dp[i][w] = max(
                        profits[i - 1] + dp[i - 1][w - weights[i - 1]],
                        dp[i - 1][w]
                    )

                else:
                    dp[i][w] = dp[i - 1][w]

        selected = []

        w = capacity

        for i in range(n, 0, -1):

            if dp[i][w] != dp[i - 1][w]:

                selected.append(i)

                w = w - weights[i - 1]

        print("\nSelected Items:")

        for item in reversed(selected):
            print(
                "Item", item,
                "Weight =", weights[item - 1],
                "Profit =", profits[item - 1]
            )

        print("\nMaximum Profit:", dp[n][capacity])


weights = []
profits = []

n = int(input("Enter number of items: "))

for i in range(n):

    print("\nItem", i + 1)

    weight = int(input("Enter weight: "))
    profit = int(input("Enter profit: "))

    weights.append(weight)
    profits.append(profit)

capacity = int(input("\nEnter knapsack capacity: "))

k = Knapsack()

k.solve(weights, profits, capacity)