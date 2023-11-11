# Isomorphic Strings

class Solution:
    def areIsomorphic(self, str1, str2):
        if len(str1) != len(str2):
            return False

        mp1, mp2 = {}, {}
        for char1, char2 in zip(str1, str2):
            mp1[char1] = char2
            mp2[char2] = char1

        return all(mp1[char1] == char2 and mp2[char2] == char1 for char1, char2 in zip(str1, str2))

# Test the class and function
sol = Solution()
result = sol.areIsomorphic("egg", "add")
print(result)  # Output: True
