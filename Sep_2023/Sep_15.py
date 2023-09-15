# Partition Equal Subset Sum

class Solution:
    def canPart(self, N, i, arr, target, dp):
        if target == 0:
            return True

        if i >= N:
            return False

        if target >= arr[i]:
            take = self.canPart(N, i + 1, arr, target - arr[i], dp)
            if take:
                dp[i][target] = True
                return True

        notTake = self.canPart(N, i + 1, arr, target, dp)
        dp[i][target] = notTake
        return notTake

    def equalPartition(self, N, arr):
        sum_val = sum(arr)
        if sum_val % 2 != 0:
            return False  # If the sum is odd, it's impossible to partition into equal subsets.

        target = sum_val // 2
        dp = [[-1 for _ in range(target + 1)] for _ in range(N)]
        return self.canPart(N, 0, arr, target, dp)

# Example usage:
arr = [1, 5, 11, 5]
N = len(arr)
solution = Solution()
result = solution.equalPartition(N, arr)
print(result)
