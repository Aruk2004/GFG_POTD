# Column name from a given column number

class Solution:
    def colName(self, n):
        out = []
        code = ['Z'] + [chr(ord('A') + i - 1) for i in range(1, 26)]

        while n > 0:
            out.append(code[n % 26])
            if n % 26 == 0:
                n -= 1
            n //= 26

        out.reverse()
        return ''.join(out)

# Example usage:
n = 701
sol = Solution()
result = sol.colName(n)
print(result)  # Output: "ZY"
