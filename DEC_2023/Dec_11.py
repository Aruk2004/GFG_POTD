# Max Sum Subarray of size K

class Solution:
    def maximumSumSubarray(self, K, Arr, N):
        out = 0
        _sum = 0

        for i in range(N):
            _sum += Arr[i]
            
            if i >= K:
                _sum -= Arr[i - K]

            out = max(out, _sum)

        return out

# Example usage:
solution = Solution()
K = 3
Arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
N = len(Arr)
result = solution.maximumSumSubarray(K, Arr, N)
print(result)
