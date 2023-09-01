#Corner nodes of a Binary Tree

from collections import deque

class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class Solution:
    def printCorner(self, root):
        if not root:
            return

        queue = deque()
        queue.append(root)

        while queue:
            sz = len(queue)
            first = queue[0]
            last = None

            for _ in range(sz):
                last = queue.popleft()
                if last.left:
                    queue.append(last.left)
                if last.right:
                    queue.append(last.right)

            if first != last:
                print(first.data, last.data, end=" ")
            else:
                print(first.data, end=" ")

# Example usage:
# Create a binary tree and call the printCorner method
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

solution = Solution()
solution.printCorner(root)
