# Count ways to N'th Stair(Order does not matter)

class Solution:
    def nthStair(self, n):
        val = 0
        for i in range(0, n + 1, 2):
            val += 1
        return val
