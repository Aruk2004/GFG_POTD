# Array Pair Sum Divisibility Problem

from collections import Counter

class Solution:
    def canPair(self, nums, k):
        if len(nums) % 2 != 0:
            return False
            
        cnt = [0] * k
        
        for i in nums:
            cnt[i % k] += 1
        
        l, r = 1, k - 1
        
        while l < r:
            if cnt[l] != cnt[r]:
                return False
            l += 1
            r -= 1
        
        if (l == r and cnt[l] % 2 != 0) or cnt[0] % 2 != 0:
            return False
        
        return True

# Example usage:
nums = [9, 7, 5, 3]
k = 6
sol = Solution()
result = sol.canPair(nums, k)
print(result)
