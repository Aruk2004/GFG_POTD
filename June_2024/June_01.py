# Odd Even Problem

class Solution:
    def oddEven(self, s: str) -> str:
        # Initialize an array to store frequencies of each character
        freq = [0] * 26
        
        # Calculate frequencies of each character in the string
        for char in s:
            freq[ord(char) - ord('a')] += 1

        x = 0
        y = 0

        # Check each character frequency
        for i in range(26):
            if freq[i] > 0:
                # Character position in the alphabet (1-based index)
                position = i + 1
                if position % 2 == 0:  # Even position in the alphabet
                    if freq[i] % 2 == 0:  # Even frequency
                        x += 1
                else:  # Odd position in the alphabet
                    if freq[i] % 2 == 1:  # Odd frequency
                        y += 1

        # Determine if the sum of x and y is even or odd
        if (x + y) % 2 == 0:
            return "EVEN"
        else:
            return "ODD"

# Example usage
solution = Solution()
s1 = "abbbcc"
print(solution.oddEven(s1))  # Output: "ODD"

s2 = "nobitaa"
print(solution.oddEven(s2))  # Output: "EVEN"
