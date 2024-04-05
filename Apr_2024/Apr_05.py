# Strictly Increasing Array

class Solution:
    def min_operations(self, nums):
        n = len(nums)
        LIS = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j] and (i - j) <= (nums[i] - nums[j]):
                    LIS[i] = max(LIS[i], LIS[j] + 1)
        return n - max(LIS)

# Example usage
solution = Solution()
nums = [1, 3, 5, 4, 2]
result = solution.min_operations(nums)
print("Minimum operations required:", result)  # Output: 2
