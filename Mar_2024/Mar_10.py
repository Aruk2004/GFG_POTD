# Remove all duplicates from a given string

# Define the class
class Solution:
    def removeDuplicates(self, s):
        seen = set()
        result = ""
        for char in s:
            if char not in seen:
                result += char
                seen.add(char)
        return result

# Example usage
if __name__ == "__main__":
    solution = Solution()
    input_string = "abracadabra"
    result = solution.removeDuplicates(input_string)
    print("String with duplicates removed:", result)
