# Candy

class Solution:
    def minCandy(self, N, ratings):
        left = [1] * N
        right = [1] * N

        # Calculate left array
        for i in range(1, N):
            if ratings[i] > ratings[i - 1]:
                left[i] += left[i - 1]

        # Calculate right array
        for i in range(N - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] += right[i + 1]

        # Calculate the total sum
        total_sum = sum(max(left[i], right[i]) for i in range(N))

        return total_sum

# Example usage:
solution_instance = Solution()
N = 5
ratings = [1, 0, 2, 1, 3]
result = solution_instance.minCandy(N, ratings)
print(result)
