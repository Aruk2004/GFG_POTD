# Pythagorean Triplet

class Solution:
    def checkTriplet(self, arr, n):
        # Create a set to store the squares of elements in the array
        squares = set()
        for num in arr:
            squares.add(num * num)

        # Iterate through all possible pairs of elements in the array
        for i in range(n):
            for j in range(n):
                if i != j:
                    # Check if the sum of squares of the two numbers is in the set
                    if (arr[i] * arr[i] + arr[j] * arr[j]) in squares:
                        return True

        # If no such triplet is found, return False
        return False

# Example usage:
solution = Solution()
arr = [3, 1, 4, 6, 5]
n = len(arr)
result = solution.checkTriplet(arr, n)
print(result)  # It will print True for the example array [3, 1, 4, 6, 5]
