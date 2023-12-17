# Max Sum without Adjacents

class Solution:
    def findMaxSum(self, arr, n):
        lastPrev = 0
        prev = arr[0]
        curr = 0

        for i in range(1, n):
            curr = max(prev, arr[i] + lastPrev)
            lastPrev = prev
            prev = curr

        return max(lastPrev, prev)

# Example usage:
solution_instance = Solution()
arr = [3, 2, 7, 10]
result = solution_instance.findMaxSum(arr, len(arr))
print(result)
