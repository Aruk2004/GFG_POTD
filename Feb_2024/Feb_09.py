# Check for Children Sum Property in a Binary Tree

class Solution:
    def isSumProperty(self, root):
        if root is None:
            return 1
        if root.left is None and root.right is None:
            return 1

        leftSum = 0
        rightSum = 0
        if root.left is not None:
            leftSum = root.left.data
        if root.right is not None:
            rightSum = root.right.data

        if root.data == leftSum + rightSum and self.isSumProperty(root.left) and self.isSumProperty(root.right):
            return 1
        return 0


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Create a binary tree
#         10
#        /  \
#       8    2
#      / \ 
#     3   5
root = TreeNode(10)
root.left = TreeNode(8)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(5)

# Create an instance of Solution
sol = Solution()

# Check if the tree satisfies the children sum property
result = sol.isSumProperty(root)
print("The binary tree satisfies the children sum property:", result)
