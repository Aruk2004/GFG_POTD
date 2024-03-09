# Find the N-th character

# Define the class
class Solution:
    def nthCharacter(self, s, r, n):
        length = len(s)
        for i in range(r):
            temp = s
            for j in range(length):
                if temp[j // 2] == '0':
                    s = s[:j] + str(0 + (j % 2)) + s[j + 1:]
                else:
                    s = s[:j] + str(1 - (j % 2)) + s[j + 1:]
        return s[n]

# Example usage
if __name__ == "__main__":
    solution = Solution()
    input_string = "101010"
    repetitions = 3
    index_to_extract = 4
    result = solution.nthCharacter(input_string, repetitions, index_to_extract)
    print("Resulting string:", result)

