class Knapsack:
    def solve(self, weights, profits, capacity):

        n = len(weights)

        dp = [[0] * (capacity + 1) for i in range(n + 1)]

        for i in range(1, n + 1):

            for w in range(1, capacity + 1):

                if weights[i - 1] <= w:

                    dp[i][w] = max(
                        profits[i - 1] + dp[i - 1][w - weights[i - 1]],
                        dp[i - 1][w]
                    )

                else:
                    dp[i][w] = dp[i - 1][w]

        return dp[n][capacity]


weights = []
profits = []

n = int(input("Enter number of items: "))

for i in range(n):

    weight = int(input("Enter weight: "))
    profit = int(input("Enter profit: "))

    weights.append(weight)
    profits.append(profit)

capacity = int(input("Enter knapsack capacity: "))

k = Knapsack()

result = k.solve(weights, profits, capacity)

print("Maximum Profit:", result)