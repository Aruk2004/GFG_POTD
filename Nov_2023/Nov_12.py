# Check if string is rotated by two places

class Solution:
    def isRotated(self, s1, s2):
        if s1 == s2[2:] + s2[:2]:
            return True
        if s1 == s2[-2:] + s2[:-2]:
            return True

        return False

# Test the class and function
sol = Solution()
result = sol.isRotated("abcde", "deabc")
print(result)  # Output: True
