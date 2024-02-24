# Maximum Sum Problem

class Solution:
    def __init__(self):
        self.memo = {}

    def maxSum(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        
        if n == 0:
            return 0

        max_sum = max(n, self.maxSum(n // 2) + self.maxSum(n // 3) + self.maxSum(n // 4))
        self.memo[n] = max_sum
        return max_sum

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSum(10))  # Output: 12
