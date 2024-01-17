# All Unique Permutations of an array

from itertools import permutations

class Solution:
    def uniquePerms(self, arr, n):
        arr.sort()
        unique_permutations = sorted(set(permutations(arr)))
        return [list(perm) for perm in unique_permutations]

# Example usage:
sol = Solution()
input_arr = [1, 2, 1]
result = sol.uniquePerms(input_arr, len(input_arr))
print(result)
