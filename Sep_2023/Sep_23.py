# Equilibriam Point

class Solution:
    def equilibriumPoint(self, a, n):
        total_sum = sum(a)
        pre_sum = 0
        
        for i in range(n):
            total_sum -= a[i]
            if total_sum == pre_sum:
                return i + 1
            pre_sum += a[i]
        
        return -1

# Example usage:
arr = [1, 3, 5, 2, 2]
n = len(arr)
sol = Solution()
result = sol.equilibriumPoint(arr, n)
print(result)  # Output: 3
