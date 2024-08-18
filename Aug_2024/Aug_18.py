# Split an array into two equal Sum subarrays

class Solution:
    def canSplit(self, nums):
        left, right = 0, len(nums) - 1
        current_sum = 0

        # Traverse the array from both ends towards the middle
        while left <= right:
            # If current_sum is non-positive, add the left element and move left pointer
            if current_sum <= 0:
                current_sum += nums[left]
                left += 1
            # If current_sum is positive, subtract the right element and move right pointer
            else:
                current_sum -= nums[right]
                right -= 1

        # Check if current_sum is zero, indicating a possible split
        return current_sum == 0
