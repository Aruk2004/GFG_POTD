# Check wheather a string is palindrome or not

class Solution:
    def isPalindrome(self, S: str):
        i, j = 0, len(S) - 1
        while i < j:
            if S[i] != S[j]:
                return "Not a palindrome"
            i += 1
            j -= 1
        return "Palindrome"

if __name__ == "__main__":
    solution = Solution()

    user_input = input("Enter a string: ")
    result = solution.isPalindrome(user_input)

    print(result)
