# Level order traversal

from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        q = deque([root])
        out = []

        while q:
            front = q.popleft()
            out.append(front.data)

            if front.left:
                q.append(front.left)
            if front.right:
                q.append(front.right)

        return out

# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

solution = Solution()
result = solution.levelOrder(root)
print("Level order traversal:", result)
