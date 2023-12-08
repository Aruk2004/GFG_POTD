# Transform to prime

class Solution:
    def is_prime(self, n):
        if n == 1:
            return False

        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False

        return True

    def minNumber(self, arr, N):
        total_sum = sum(arr)
        cnt = 0

        while not self.is_prime(total_sum):
            cnt += 1
            total_sum += 1

        return cnt

# Example usage:
solution = Solution()
arr = [3, 5, 7]
N = len(arr)
result = solution.minNumber(arr, N)
print(result)  # Output: 0
