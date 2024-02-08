# Check if all leaves are at same level

from collections import deque

class Solution:
    def check(self, root):
        if not root:
            return True

        q = deque([(root, 0)])
        first_leaf = -1

        while q:
            node, lvl = q.popleft()

            if not node.left and not node.right:
                if first_leaf == -1:
                    first_leaf = lvl
                elif first_leaf != lvl:
                    return False
            
            lvl += 1
            if node.left:
                q.append((node.left, lvl))
            if node.right:
                q.append((node.right, lvl))
        
        return True


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

# Check if all leaf nodes are at the same level
result = sol.check(root)
print("All leaf nodes are at the same level:", result)
