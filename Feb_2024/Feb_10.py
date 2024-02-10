# Number of paths in a matrix with k coins

class Solution:
    def numberOfPath(self, n, k, arr):
        # Helper function to recursively find the number of paths
        def help(rowIdx, colIdx, n, k, arr, cnt, pathSum):
            # Base case: if rowIdx or colIdx exceeds the matrix dimensions, return the current count
            if rowIdx >= n or colIdx >= n:
                return cnt
            # Update the path sum with the value of the current cell
            pathSum += arr[rowIdx][colIdx]
            # If the current path sum exceeds k, return the current count
            if pathSum > k:
                return cnt
            # If the current path sum equals k and we reach the bottom-right cell, increment the count
            if pathSum == k and rowIdx == n - 1 and colIdx == n - 1:
                return cnt + 1
            # Recursively explore paths moving down (increment rowIdx)
            r = help(rowIdx + 1, colIdx, n, k, arr, cnt, pathSum)
            # Recursively explore paths moving right (increment colIdx)
            c = help(rowIdx, colIdx + 1, n, k, arr, cnt, pathSum)
            # Return the sum of paths found moving down and right
            return r + c

        # Start the recursion from the top-left corner (rowIdx = 0, colIdx = 0) with initial count 0 and path sum 0
        return help(0, 0, n, k, arr, 0, 0)

# Example usage:
sol = Solution()
k = 12
n = 3
arr = [
    [1, 2, 3],
    [4, 6, 5],
    [3, 2, 1]
]
print(sol.numberOfPath(n, k, arr))  # Output: 2
