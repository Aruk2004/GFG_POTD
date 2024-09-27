# K Sized Subarray Maximum

from collections import deque

class Solution:
    
    # Function to find maximum of each subarray of size k.
    def max_of_subarrays(self, k, arr):
        n = len(arr)
        if n == 0 or k <= 0:
            return []

        max_elements = []
        dq = deque()  # This will store indices of the array elements

        for i in range(n):
            # Remove indices that are out of the current window
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # Remove elements that are smaller than the current element
            while dq and arr[dq[-1]] < arr[i]:
                dq.pop()

            # Add the current element index
            dq.append(i)

            # If we have processed at least k elements, record the maximum
            if i >= k - 1:
                max_elements.append(arr[dq[0]])

        return max_elements

# Example usage:
sol = Solution()
k1 = 3
arr1 = [1, 2, 3, 1, 4, 5, 2, 3, 6]
print(sol.max_of_subarrays(k1, arr1))  # Output: [3, 3, 4, 5, 5, 5, 6]

k2 = 4
arr2 = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
print(sol.max_of_subarrays(k2, arr2))  # Output: [10, 10, 10, 15, 15, 90, 90]
