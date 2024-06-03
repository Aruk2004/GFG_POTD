# Trail of one

class Solution:
    def numberOfConsecutiveOnes (ob, n):
        a, b = 1, 1

        for _ in range(n):
            a, b = b, (a+b) % 1000000007

        return (pow(2, n, 1000000007) - b) % 1000000007
