# Nth Natural Number

class Solution:
    def findNth(self, n):
        ans = ""
        while n:
            ans = str(n % 9) + ans
            n //= 9
        return int(ans)
