# You and your books

class Solution:
    def max_Books(self, n: int, k: int, arr: List[int]) -> int:
        res, count = 0, 0
        for i in range(n):
            if arr[i] <= k:
                count += arr[i]
            else:
                count = 0
            res = max(res, count)
        return res

# Example usage
if __name__ == "__main__":
    solution = Solution()
    n = 5
    k = 3
    arr = [1, 2, 3, 4, 5]
    print(solution.max_Books(n, k, arr))  # Output should be 6 (1 + 2 + 3)
