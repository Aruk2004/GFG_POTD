# Inorder Traversal and BST

class Solution:
    def isRepresentingBST(self, arr, n):
        for i in range(n - 1):
            if arr[i] < arr[i + 1]:
                continue
            else:
                return 0
        return 1

# Example usage:
solution = Solution()
arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 3, 5, 1]

result1 = solution.isRepresentingBST(arr1, len(arr1))
result2 = solution.isRepresentingBST(arr2, len(arr2))

print(result1)  # Output: 1 (arr1 represents a BST)
print(result2)  # Output: 0 (arr2 does not represent a BST)
