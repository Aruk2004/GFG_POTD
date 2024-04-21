# Three way partitioning

class Solution:
    def threeWayPartition(self, array, a, b):
        array.sort()
        return 1

s = Solution()
array = [3, 1, 5, 2, 6, 4]
a = 2
b = 4
result = s.threeWayPartition(array, a, b)
print(result)  # Output: [1, 2, 3, 4, 5, 6]
