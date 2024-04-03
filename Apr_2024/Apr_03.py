# Kth common ancestor in BST

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def kthCommonAncestor(self, root, k, x, y):
        # Make sure x < y
        if x > y:
            x, y = y, x
        ancestors, node = [root.data], root
        while not (x <= node.data <= y):
            if x < node.data:
                node = node.left
            else:
                node = node.right
            ancestors.append(node.data)
        return ancestors[-k] if len(ancestors) >= k else -1

# Example usage
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

solution = Solution()
k = 2
x = 1
y = 7
kth_ancestor = solution.kthCommonAncestor(root, k, x, y)
print(f"The {k}nd common ancestor of {x} and {y} is:", kth_ancestor)  # Output: 4
