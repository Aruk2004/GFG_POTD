# Perfect Number

import math

class Solution:
    def isPerfectNumber(self, n):
        if n == 1:
            return 0
        total = 1
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                total += i
                if n // i != i:
                    total += n // i
        return int(total == n)

# Create an instance of the Solution class
solution = Solution()

# Prompt the user to enter a number
user_input = input("Enter a positive integer: ")

# Convert the user input to an integer
n = int(user_input)

# Test the isPerfectNumber method with the user's input
result = solution.isPerfectNumber(n)

# Print the result (1 for perfect number, 0 for non-perfect number)
if result == 1:
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")
