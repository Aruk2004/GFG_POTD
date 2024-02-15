# Count all Possible Path

class Solution:
    def isPossible(self, paths):
        for path in paths:
            if sum(path) % 2 != 0:
                return 0
        return 1

# Example usage
if __name__ == "__main__":
    # Create an instance of the Solution class
    sol = Solution()

    # Define the paths
    paths1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Sum of each path is even
    paths2 = [[1, 2, 3], [4, 5, 6], [7, 8, 10]]  # Sum of last path is odd

    # Check if it's possible to form a closed loop for each set of paths
    result1 = sol.isPossible(paths1)
    result2 = sol.isPossible(paths2)

    # Print the results
    print("Is it possible to form a closed loop from paths1?", "Yes" if result1 == 1 else "No")
    print("Is it possible to form a closed loop from paths2?", "Yes" if result2 == 1 else "No")
