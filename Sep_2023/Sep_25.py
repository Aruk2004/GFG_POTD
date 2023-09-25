# Maximum Sum Combination

import heapq

class Solution:
    def maxCombinations(self, N, K, A, B):
        # Sort the arrays in ascending order
        A.sort()
        B.sort()

        # Create a heap (min-heap) to store combinations
        heap = [(-A[N - 1] - B[N - 1], N - 1, N - 1)]  # Use negative values for max-heap behavior

        out = []
        while K > 0:
            value, a, b = heapq.heappop(heap)
            out.append(-value)  # Convert back to positive value
            K -= 1

            if a > 0:
                heapq.heappush(heap, (-(A[a - 1] + B[b]), a - 1, b))
            if b > 0:
                heapq.heappush(heap, (-(A[a] + B[b - 1]), a, b - 1))

        return out

# Example usage:
N = 3
K = 2
A = [1, 2, 3]
B = [4, 5, 6]
sol = Solution()
result = sol.maxCombinations(N, K, A, B)
print(result)  # Output: [9, 8]
