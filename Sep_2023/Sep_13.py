# Find largest no possible with given digits and Sum

class Solution:
    def findLargest(self, N, S):
        if (S == 0 and N > 1) or (N * 9 < S):
            return "-1"
        
        out = ""
        for i in range(N):
            if S >= 9:
                out += '9'
                S -= 9
            else:
                if S:
                    out += str(S)
                    S = 0
                else:
                    out += '0'
        
        return out

# Create an instance of the Solution class
solution = Solution()

# Prompt the user to enter values for N and S
N = int(input("Enter N (number of digits): "))
S = int(input("Enter S (sum of digits): "))

# Call the findLargest method with user-provided values
result = solution.findLargest(N, S)

# Print the result
print("Largest Number:", result)
