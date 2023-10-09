# Height of Binary Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def height(self, node):
        if not node:
            return 0

        return max(self.height(node.left), self.height(node.right)) + 1

# Example usage:
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

sol = Solution()
tree_height = sol.height(root)
print(f"Height of the Binary Tree: {tree_height}")
