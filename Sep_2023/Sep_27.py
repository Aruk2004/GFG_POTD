# Find the closest pair from two arrays

class Solution:
    def printClosest(self, arr, brr, n, m, x):
        # Initialize variables to keep track of the closest pair and their difference from x
        closest_pair = None
        closest_diff = float('inf')

        # Initialize pointers for the two arrays
        i = 0  # Pointer for arr (starting from the beginning)
        j = m - 1  # Pointer for brr (starting from the end)

        # Loop through the arrays while pointers are valid
        while i < n and j >= 0:
            # Calculate the current pair sum
            current_sum = arr[i] + brr[j]

            # Calculate the absolute difference between the current sum and x
            current_diff = abs(current_sum - x)

            # Update the closest pair if the current difference is smaller
            if current_diff < closest_diff:
                closest_pair = (arr[i], brr[j])
                closest_diff = current_diff

            # If the current sum is greater than x, decrement the pointer for brr
            if current_sum > x:
                j -= 1
            # If the current sum is less than or equal to x, increment the pointer for arr
            else:
                i += 1

        # Return the closest pair
        return closest_pair

# Example usage:
arr = [1, 4, 5, 7]
brr = [10, 20, 30, 40]
n = len(arr)
m = len(brr)
x = 32
solution = Solution()
closest_pair = solution.printClosest(arr, brr, n, m, x)
print("Closest pair:", closest_pair)


class Solution:
    def printClosest(self, arr, brr, n, m, x):
        # Initialize variables to keep track of the closest pair and their difference from x
        closest_pair = None
        closest_diff = float('inf')

        # Initialize pointers for the two arrays
        i = 0  # Pointer for arr (starting from the beginning)
        j = m - 1  # Pointer for brr (starting from the end)

        # Loop through the arrays while pointers are valid
        while i < n and j >= 0:
            # Calculate the current pair sum
            current_sum = arr[i] + brr[j]

            # Calculate the absolute difference between the current sum and x
            current_diff = abs(current_sum - x)

            # Update the closest pair if the current difference is smaller
            if current_diff < closest_diff:
                closest_pair = (arr[i], brr[j])
                closest_diff = current_diff

            # If the current sum is greater than x, decrement the pointer for brr
            if current_sum > x:
                j -= 1
            # If the current sum is less than or equal to x, increment the pointer for arr
            else:
                i += 1

        # Return the closest pair
        return closest_pair

# Example usage:
arr = [1, 4, 5, 7]
brr = [10, 20, 30, 40]
n = len(arr)
m = len(brr)
x = 32
solution = Solution()
closest_pair = solution.printClosest(arr, brr, n, m, x)
print("Closest pair:", closest_pair)
