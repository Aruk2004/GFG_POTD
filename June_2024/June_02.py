# Construct list using given q XOR queries

from typing import List

class Solution:
    def constructList(self, q : int, queries : List[List[int]]) -> List[int]:
        mask, ans = 0, []
        for t, v in queries[::-1]:
            if t == 0:
                ans.append(v ^ mask)
            else:
                mask ^= v

        return sorted(ans + [0 ^ mask])
