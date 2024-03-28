# City With the Smallest Number of Neighbors at a Threshold Distance

from typing import List

class Solution:
    def findCity(self, n : int, m : int, edges : List[List[int]], d : int) -> int:
        # code here
        from collections import defaultdict
        from heapq import heappush, heappop
        g = defaultdict(list)

        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))

        def dijkstr(n):
            costs = {n: 0}
            q = [(0, n)]
            while q:
                cost0, n0 = heappop(q)
                for nbr, c in g[n0]:
                    cost = cost0+c
                    if cost > d:
                        continue
                    if nbr not in costs or costs[nbr] > cost:
                        costs[nbr] = cost
                        heappush(q, (cost, nbr))
            return len(costs)

        ans = 0
        cnt = n
        for k in range(n):
            c = dijkstr(k)
            if c <= cnt:
                cnt = c
                ans = k
        return ans

solution = Solution()
n = 5  # Number of cities
m = 6  # Number of edges
edges = [
    [0, 1, 10],  # Edge from city 0 to city 1 with distance 10
    [1, 2, 15],  # Edge from city 1 to city 2 with distance 15
    [2, 3, 20],  # Edge from city 2 to city 3 with distance 20
    [3, 4, 25],  # Edge from city 3 to city 4 with distance 25
    [0, 2, 30],  # Edge from city 0 to city 2 with distance 30
    [2, 4, 35],  # Edge from city 2 to city 4 with distance 35
]
d = 50  # Distance threshold

result = solution.findCity(n, m, edges, d)
print("City with shortest distance from others:", result)
