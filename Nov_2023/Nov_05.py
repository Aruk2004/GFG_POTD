# Top K Frequent Elements in Array

from collections import Counter

class Solution:
    def topK(self, nums, k):
        # Create a Counter dictionary to count the frequency of each element
        count = Counter(nums)
        
        # Sort the elements based on frequency and then by their value in descending order
        sorted_elements = sorted(count.keys(), key=lambda x: (-count[x], -x))
        
        # Return the top k elements
        return sorted_elements[:k]

# Example usage
input_nums = [1, 1, 2, 2, 3, 3, 3, 4]
k = 2
solver = Solution()
output = solver.topK(input_nums[1:], k)  # Skip the first element which represents the size of the array
print(output)  # Output: [3, 2]
