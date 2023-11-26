# Print Pattern

class Solution:
    def pattern(self, N):
        result = []
    
        def generate_sequence(n):
            if n <= 0:
                result.append(n)
                return
            result.append(n)
            generate_sequence(n - 5)
            result.append(n)
    
        generate_sequence(N)
    
        return result

# Example usage:
solution = Solution()
result1 = solution.pattern(16)
print(result1)  # Output: [16, 11, 6, 1, -4, 1, 6, 11, 16]

result2 = solution.pattern(10)
print(result2)  # Output: [10, 5, 0, 5, 10]
