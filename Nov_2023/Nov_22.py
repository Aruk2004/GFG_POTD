# Symmetric Tree

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        def isMirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False

            return (
                left.data == right.data
                and isMirror(left.left, right.right)
                and isMirror(left.right, right.left)
            )

        if not root:
            return True

        return isMirror(root.left, root.right)

# Example usage:
# Constructing a sample symmetric binary tree
symmetric_root = Node(5)
symmetric_root.left = Node(1)
symmetric_root.right = Node(1)
symmetric_root.left.left = Node(2)
symmetric_root.right.right = Node(2)

# Constructing a sample non-symmetric binary tree
non_symmetric_root = Node(5)
non_symmetric_root.left = Node(10)
non_symmetric_root.right = Node(10)
non_symmetric_root.left.left = Node(20)
non_symmetric_root.left.right = Node(20)
non_symmetric_root.right.right = Node(30)

# Creating an instance of Solution
solution = Solution()

# Checking if the trees are symmetric
result_symmetric = solution.isSymmetric(symmetric_root)
result_non_symmetric = solution.isSymmetric(non_symmetric_root)

print("Symmetric:", result_s
