# Minimum Cost of ropes 

import heapq
from typing import List

class Solution:
   def minCost(self, arr: List[int]) -> int:

        if len(arr) < 2: return 0

        heapq.heapify(arr)

        totalCost = 0

        while len(arr) > 1:
            x, y = heapq.heappop(arr), heapq.heappop(arr)
            min_cost = x + y
            totalCost += min_cost
            heapq.heappush(arr, min_cost)

        return totalCost
