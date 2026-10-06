class Knapsack:
    def solve(self, weights, profits, capacity):

        n = len(weights)

        dp = [0] * (capacity + 1)

        for i in range(n):

            for w in range(capacity, weights[i] - 1, -1):

                dp[w] = max(
                    dp[w],
                    profits[i] + dp[w - weights[i]]
                )

        return dp[capacity]


weights = []
profits = []

n = int(input("Enter number of items: "))

for i in range(n):

    print("\nItem", i + 1)

    weights.append(
        int(input("Enter weight: "))
    )

    profits.append(
        int(input("Enter profit: "))
    )

capacity = int(input("\nEnter capacity: "))

k = Knapsack()

answer = k.solve(weights, profits, capacity)

print("\nMaximum Profit:", answer)