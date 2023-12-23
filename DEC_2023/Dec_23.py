# Count More than n/k Occurences

from collections import defaultdict

class Solution:
    def countOccurence(self, arr, n, k):
        mp = defaultdict(int)
        minCnt = n // k
        
        for i in range(n):
            mp[arr[i]] += 1

        out = 0
        for count in mp.values():
            if count > minCnt:
                out += 1

        return out

# Example usage:
solution_instance = Solution()
arr = [3, 1, 2, 2, 1, 2, 3, 3]
n = len(arr)
k = 4
result = solution_instance.countOccurence(arr, n, k)
print(result)
