# Closest Neighbour in BST

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class Solution:
    def findMaxForN(self, root, n):
        find = -1
        while root:
            if root.key > n:
                root = root.left
            else:
                if root.key <= n:
                    find = root.key
                    root = root.right
        return find

# Example usage
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)

solution = Solution()
max_val = solution.findMaxForN(root, 8)
print("Maximum value <= 8 in the BST:", max_val)  # Output: 7
