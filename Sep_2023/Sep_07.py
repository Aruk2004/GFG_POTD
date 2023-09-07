#Minimum Multiplications to reach End

from collections import deque

class Solution:
    def __init__(self):
        self.MOD = 100000
    
    def minimumMultiplications(self, arr, start, end):
        if start == end:
            return 0

        n = len(arr)
        dp = [-1] * self.MOD

        dp[start] = 0

        q = deque()
        q.append(start)

        while q:
            current = q.popleft()

            for i in range(n):
                next_val = (current * arr[i]) % self.MOD

                if dp[next_val] == -1:
                    dp[next_val] = dp[current] + 1
                    q.append(next_val)

                    if next_val == end:
                        return dp[next_val]

        return -1
