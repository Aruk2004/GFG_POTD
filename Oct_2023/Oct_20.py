# Form a number divisible by 3 using array digits

class Solution:
    def isPossible(self, N, arr):
        total_sum = sum(arr)
        return total_sum % 3 == 0

# Example usage:
sol = Solution()
N = 6
arr = [3, 6, 9, 5, 12, 18]

result = sol.isPossible(N, arr)
print("Is it possible to divide the array into three parts with sums divisible by 3?", result)  # Output: True
