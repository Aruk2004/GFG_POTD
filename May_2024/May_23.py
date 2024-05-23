# K-Palindrome

class Solution:
    def kPalindrome(self, st: str, n: int, k: int) -> int:
        prev = [0] * len(st)
        for i in range(len(st) - 1, -1, -1):
            curr = [0] * len(st)
            curr[i] = 1
            for j in range(i + 1, len(st)):
                curr[j] = max(prev[j], curr[j - 1])
                if st[i] == st[j]:
                    curr[j] = max(curr[j], 2 + prev[j - 1])
            prev = curr[:]
        
        lps_length = curr[len(st) - 1]
        return 1 if len(st) - lps_length <= k else 0

# Example usage:
solution = Solution()
st = "abcdecba"
n = len(st)
k = 2
print(solution.kPalindrome(st, n, k))  # Output should be 1 if it can be turned into a palindrome by removing <= k characters, otherwise 0
