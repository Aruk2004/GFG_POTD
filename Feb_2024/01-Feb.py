Panagram Checking

class Solution:
    
    # Function to check if a string is Pangram or not.
    def checkPangram(self, s):
        # Create a set to store unique characters in the string
        char_set = set()

        # Iterate through each character in the string
        for char in s:
            # Check if the character is an alphabet letter
            if char.isalpha():
                # Convert the letter to lowercase and add it to the set
                char_set.add(char.lower())

        # Check if the set contains all 26 letters of the English alphabet
        return len(char_set) == 26

# Example usage:
solution = Solution()

s1 = "Bawds jog, flick quartz, vex nymph"
s2 = "sdfs"

output1 = solution.checkPangram(s1)
output2 = solution.checkPangram(s2)

print(output1)  # Output: True
print(output2)  # Output: False
