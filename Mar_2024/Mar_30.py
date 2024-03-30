# Minimum element in BST

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def minValue(self, root):
        if root is None:
            return None
        if root.left is None:
            return root.data
        return self.minValue(root.left)

# Example usage
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)

solution = Solution()
min_val = solution.minValue(root)
print("Minimum value in the BST:", min_val)  # Output: 3
