# Check for Balanced Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.height = {}

    def isBalanced(self, root):
        if not root:
            return True

        is_left_balanced = self.isBalanced(root.left)
        is_right_balanced = self.isBalanced(root.right)

        left_height = self.height.get(root.left, 0)
        right_height = self.height.get(root.right, 0)

        is_balanced = is_left_balanced and is_right_balanced and abs(left_height - right_height) <= 1

        self.height[root] = max(left_height, right_height) + 1

        return is_balanced

# Example usage:
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

sol = Solution()
result = sol.isBalanced(root)
print("Is the Binary Tree balanced:", result)  # Output: True
