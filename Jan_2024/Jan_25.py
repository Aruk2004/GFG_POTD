# Shortest Prime Path

from typing import List
from collections import deque

class Solution:
    def __init__(self):
        self.isPrime = []

    def sieve(self):
        n = len(self.isPrime)
        self.isPrime[0] = self.isPrime[1] = False

        for i in range(2, int(n**0.5) + 1):
            if self.isPrime[i]:
                for j in range(i*i, n, i):
                    self.isPrime[j] = False

    def solve(self, Num1, Num2):
        self.isPrime = [True] * 10000
        self.sieve()

        tar = str(Num2)

        vis = set()
        q = deque()
        q.append(str(Num1))
        vis.add(str(Num1))
        lvl = 0

        while q:
            sz = len(q)
            while sz > 0:
                curr = q.popleft()

                if curr == tar:
                    return lvl

                for i in range(4):
                    for c in '0123456789':
                        perm = list(curr)
                        if i == 0 and c == '0':
                            continue

                        perm[i] = c
                        new_perm = ''.join(perm)
                        if self.isPrime[int(new_perm)] and new_perm not in vis:
                            vis.add(new_perm)
                            q.append(new_perm)

                sz -= 1
            lvl += 1

        return -1

# Example usage:
solution = Solution()
Num1 = 1033
Num2 = 8179
result = solution.solve(Num1, Num2)

# Print the result
print(result)
