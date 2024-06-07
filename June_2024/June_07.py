# Maximum occured integer

class Solution:
    def maxOccured(self,n, l, r, maxx):
        diff = [0] * (maxx + 2)
        for i in range(n):
            diff[l[i]] += 1
            diff[r[i] + 1] -= 1
        max_freq = 0
        result = 0
        curr_freq = 0
        for i in range(maxx + 1):
            curr_freq += diff[i]
            if curr_freq > max_freq:
                max_freq = curr_freq
                result = i

        return result
