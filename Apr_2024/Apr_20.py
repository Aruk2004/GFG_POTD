# Union of Two Sorted Arrays

class Solution:
    def findUnion(self,arr1,arr2,n,m):
        return sorted(list(set(arr1 + arr2)))

s = Solution()
arr1 = [1, 3, 5, 7]
arr2 = [3, 7, 9]
n = len(arr1)
m = len(arr2)
union_arr = s.findUnion(arr1, arr2, n, m)
print(union_arr)  # Output: [1, 3, 5, 7, 9]
