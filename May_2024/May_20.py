# Modular Exponentiation for large numbers

class Solution:
    def PowMod(self, x: int, n: int, m: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return x % m
        
        ans = self.PowMod(x, n // 2, m)
        ans = (ans * ans) % m
        
        if n % 2 != 0:
            ans = (ans * x) % m
        
        return ans

# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    x = 2
    n = 10
    m = 1000
    print(solution.PowMod(x, n, m))  # Output: 24
    
    # Test case 2
    x = 3
    n = 13
    m = 100
    print(solution.PowMod(x, n, m))  # Output: 87
    
    # Test case 3
    x = 5
    n = 5
    m = 100
    print(solution.PowMod(x, n, m))  # Output: 25
