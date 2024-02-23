# Buy and Sell a Share at most twice

from typing import List

class Solution:
    def maxProfit(self, n: int, price: List[int]) -> int:
        if n < 2:
            return 0
        
        left = [0] * n
        right = [0] * n
        
        # Calculate maximum profit from left to right
        min_price = price[0]
        for i in range(1, n):
            min_price = min(min_price, price[i])
            left[i] = max(left[i - 1], price[i] - min_price)
        
        # Calculate maximum profit from right to left
        max_price = price[n - 1]
        for i in range(n - 2, -1, -1):
            max_price = max(max_price, price[i])
            right[i] = max(right[i + 1], max_price - price[i])
        
        # Calculate maximum profit by combining left and right profits
        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, left[i] + right[i])
        
        return max_profit

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(sol.maxProfit(len(prices), prices))  # Output: 5
