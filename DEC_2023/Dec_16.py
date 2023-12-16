# String's Count

class Solution:
    @staticmethod
    def countStr(n):
        return 1 + 2 * n + (n * (n - 1)) + ((n * (n - 1)) // 2) + (n * (n - 1) * (n - 2)) // 2

# Example usage:
solution_instance = Solution()
result = solution_instance.countStr(5)  # Replace 5 with the desired value of n
print(result)
