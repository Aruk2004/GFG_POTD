#Shortest path from 1 to n


class Solution:
    def minimumStep(self, n: int) -> int:
        cnt = 0
        while n > 1:
            if n % 3 == 0:
                n //= 3
            else:
                n -= 1
            cnt += 1
        return cnt

# Example usage:
solution = Solution()
result = solution.minimumStep(10)
print(result)
