# First element to occur k times

class Solution:
    def firstElementKTime(self, n: int, k: int, a: List[int]) -> int:
        freq_map = {}
        for num in a:
            freq_map[num] = freq_map.get(num, 0) + 1
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
