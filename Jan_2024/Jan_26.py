# Fractional Knapsack

from typing import List

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

class Solution:
    def fractionalKnapsack(self, W, arr, n):
        arr.sort(key=lambda item: item.value / item.weight, reverse=True)

        value = 0

        # Filling the knapsack
        for item in arr:
            if item.weight <= W:
                value += item.value
                W -= item.weight
            else:
                value += item.value * W / item.weight
                break

        return value

# Example usage:
solution = Solution()
n, W = map(int, input().split())
items = []
for _ in range(n):
    value, weight = map(int, input().split())
    items.append(Item(value, weight))

result = solution.fractionalKnapsack(W, items, n)

# Print the result
print(result)
