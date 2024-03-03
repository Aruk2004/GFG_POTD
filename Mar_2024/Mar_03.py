# First element to occur k times

from collections import defaultdict

class Solution:
    def firstElementKTime(self, n, k, a):
        freq_map = defaultdict(int)
        for num in a:
            freq_map[num] += 1
            if freq_map[num] == k:
                return num
        return -1

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    n = 7
    k = 2
    a = [1, 7, 4, 3, 4, 8, 7]
    result = sol.firstElementKTime(n, k, a)
    print(result)  # Output: 7
