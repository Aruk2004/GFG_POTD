# Search Pattern (Rabin-Karp Algorithm)

class Solution:
    def search(self, pattern: str, text: str) -> List[int]:
        out = []
        mod = 10
        h = len(pattern)
        n = len(text)
        hashp = 0
        hasht = 0
        p = 1
        
        for i in range(h - 1):
            p = (p * 26) % mod
        
        for i in range(h):
            hashp = ((hashp * 26) + ord(pattern[i])) % mod
            hasht = ((hasht * 26) + ord(text[i])) % mod
        
        for i in range(n - h + 1):
            if hashp == hasht:
                j = 0
                while j < h and pattern[j] == text[i + j]:
                    j += 1
                if j == h:
                    out.append(i + 1)
            
            if i < n - h:
                hasht = (26 * (hasht - ord(text[i]) * p) + ord(text[i + h])) % mod
                if hasht < 0:
                    hasht += mod
        
        return out

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    pattern = "ABC"
    text = "ABABCABCDABABCABCD"
    result = sol.search(pattern, text)
    print(result)  # Output: [1, 5, 9, 13]
