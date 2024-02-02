# Implement Atoi

class Solution:
    # Function to convert string to integer.
    def atoi(self, s):
        # Check if the string is empty
        if not s:
            return -1

        # Initialize variables to track the sign and result
        sign = 1
        result = 0
        i = 0

        # Skip leading whitespaces
        while i < len(s) and s[i] == ' ':
            i += 1

        # Check for the sign character
        if i < len(s) and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Process digits in the string
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            # Check for overflow
            if result > (2**31 - 1 - digit) // 10:
                return -1
            result = result * 10 + digit
            i += 1

        # Check for any non-numeric characters after valid numeric part
        while i < len(s) and s[i] != ' ':
            return -1

        # Apply the sign to the result
        return sign * result

# Example usage:
solution = Solution()

s1 = "-123"
s2 = "21a"

output1 = solution.atoi(s1)
output2 = solution.atoi(s2)

print(output1)  # Output: -123
print(output2)  # Output: -1

