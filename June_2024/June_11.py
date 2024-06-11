# Maximum Tip Calculator

from typing import List

class Solution:
    def maxTip(self, n : int, x : int, y : int, arr : List[int], brr : List[int]) -> int:
        tp = zip(arr, brr)
        sorted_tips = sorted(tp, key=lambda t: abs(t[0] - t[1]), reverse=True)
        cntA, cntB, total = 0, 0, 0
        for a, b in sorted_tips:
            if (a >= b and cntA < x) or cntB == y:
                total += a
                cntA += 1
            else:
                total += b
                cntB += 1
        return total
