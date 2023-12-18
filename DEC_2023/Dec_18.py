# Game of XOR

class Solution:
    def gameOfXor(self, N, A):
        if N % 2 == 0:
            return 0

        XOR = 0
        for i in range(0, N, 2):
            XOR ^= A[i]

        return XOR

# Example usage:
solution_instance = Solution()
N = 5
A = [4, 2, 7, 9, 3]
result = solution_instance.gameOfXor(N, A)
print(result)
