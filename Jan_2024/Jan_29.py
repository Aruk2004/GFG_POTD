# Count digit groupings of a number

class Solution:
    def TotalCount(self, s):
        n = len(s)
        suffix = [0] * (n + 1)
        MAX = 0

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + int(s[i])
            MAX += int(s[i])

        dp = [[0] * (MAX + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(suffix[0] - suffix[i + 1], MAX + 1):
                dp[i][j] = 1

        for end in range(n):
            for summation in range(MAX + 1):
                low, high = -1, end + 1

                while low < high - 1:
                    mid = (low + high) // 2

                    cur_sum = suffix[mid] - suffix[end + 1]

                    if cur_sum <= summation:
                        high = mid
                    else:
                        low = mid

                for br in range(high, end + 1):
                    cur_sum = suffix[br] - suffix[end + 1]

                    if cur_sum <= summation:
                        dp[end][summation] += dp[br - 1][cur_sum] if br > 0 else 0

        return dp[n - 1][MAX]

# Create an instance of the Solution class
solution = Solution()

# Example input string
input_str = "12321"

# Call the TotalCount method with the input string
result = solution.TotalCount(input_str)

# Print the result
print("Total count of subarrays with maximum sum of digits:", result)
