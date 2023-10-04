# Roman Number to Integer

class Solution:
    def romanToDecimal(self, s):
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        n = len(s)
        result = 0

        for i in range(n):
            if i + 1 < n and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                result -= roman_to_int[s[i]]
            else:
                result += roman_to_int[s[i]]

        return result

# Example usage:
roman_numeral = "MCMXCIV"
sol = Solution()
result = sol.romanToDecimal(roman_numeral)
print(result)  # Output: 1994
