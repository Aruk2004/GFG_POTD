# Modified Game of Nim 

class Solution:
    def findWinner(self, n, A):
        XOR = 0

        # Calculate the XOR of all elements in the array
        for i in range(n):
            XOR ^= A[i]

        # If the XOR is zero, return player 1 as the winner
        if XOR == 0:
            return 1

        # If the XOR is non-zero and the number of elements is even, return player 1
        # Otherwise, return player 2
        return 1 if n % 2 == 0 else 2

# Example usage:
solution_instance = Solution()
n = 5
A = [4, 2, 7, 9, 3]
result = solution_instance.findWinner(n, A)
print(result)
