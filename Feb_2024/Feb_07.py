# Min distance between two given nodes of a Binary Tree

class Solution:
    def __init__(self):
        self.ans = 0

    def solve(self, root, a, b):
        if root is None or self.ans > 0:
            return 0

        l = self.solve(root.left, a, b)
        r = self.solve(root.right, a, b)

        if root.data == a or root.data == b:
            if l != 0:
                self.ans = l
            elif r != 0:
                self.ans = r
            else:
                return 1

        if l != 0 and r != 0:
            self.ans = l + r
        elif l != 0:
            return l + 1
        elif r != 0:
            return r + 1

        return 0

    def findDist(self, root, a, b):
        if a == b:
            return 0

        self.solve(root, a, b)
        return self.ans


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Create a binary tree
#        1
#       / \
#      2   3
#     / \ 
#    4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Create an instance of Solution
sol = Solution()

# Calculate the distance between nodes 4 and 5
a = 4
b = 5
distance = sol.findDist(root, a, b)
print("Distance between nodes", a, "and", b, "is:", distance)
