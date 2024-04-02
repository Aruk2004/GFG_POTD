# Minimum Absolute Difference In BST

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def absolute_diff(self, root):
        res = []
        def fun(root):
            nonlocal res
            if root:
                res.append(root.data)
            if root.left:
                fun(root.left)
            if root.right:
                fun(root.right)

        fun(root)
        res.sort()
        ans = float('inf')
        for i in range(1, len(res)):
            ans = min(ans, res[i] - res[i - 1])
        return ans

# Example usage
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

solution = Solution()
min_diff = solution.absolute_diff(root)
print("Minimum absolute difference between any two nodes in the tree:", min_diff)  # Output: 1
