# Swapping pairs make sum equal


class Solution:
    def findSwapValues(self, a, n, b, m):
        s1 = sum(a)
        s2 = sum(b)
        mid = (s1 + s2) // 2
        if (s2 > s1):
            if ((s1 + s2) % 2 == 0 and (s2 - mid + 1) in b and (mid - s1 - 1) in a):
                return 1
            else:
                return -1
        elif (s1 > s2):
            if ((s1 + s2) % 2 == 0 and (s1 - mid + 1) in a and (mid - s2 - 1) in b):
                return 1
            else:
                return -1
        else:
            return 1
