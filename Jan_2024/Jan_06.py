# Techfest and the Queue

from math import sqrt

class Solution:
    def primePowers(self, n):
        cnt = 0
        i = 2
        while i <= sqrt(n):
            while n % i == 0:
                cnt += 1
                n //= i
            i += 1
        
        if n > 1:
            cnt += 1
        
        return cnt

    def sumOfPowers(self, a, b):
        cnt = 0
        for i in range(a, b + 1):
            cnt += self.primePowers(i)
        
        return cnt

# Example usage:
sol = Solution()
result = sol.sumOfPowers(10, 20) 
print(result)
