# Subarray with 0 sum

class Solution:
    # Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self, arr, n):
        prefix_sum_set = set()
        prefix_sum = 0

        for num in arr:
            prefix_sum += num

            # If the current prefix sum is already in the set, then a subarray with 0-sum exists.
            if prefix_sum == 0 or prefix_sum in prefix_sum_set:
                return True

            # Add the current prefix sum to the set.
            prefix_sum_set.add(prefix_sum)

        # If no subarray with 0-sum is found, return False.
        return False

# Example usage with multiple test cases:
solution = Solution()
test_cases = [
    [4, 2, -3, 1, 6],
    [4, 2, 0, 1, 6],
    [-3, 2, 3, 1, 6],
]

for arr in test_cases:
    result = solution.subArrayExists(arr, len(arr))
    print(result)
