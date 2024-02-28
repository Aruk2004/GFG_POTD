# Check if a number is divisible by 8

class Solution:
    def DivisibleByEight(self, s: str) -> int:
        n = len(s)
        l = int(s[max(n - 3, 0):])
        return 1 if l % 8 == 0 else -1

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    s = "123456"
    result = sol.DivisibleByEight(s)
    print(result)  # Output: 1
