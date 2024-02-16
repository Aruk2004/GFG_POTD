# Flatten BST to sorted list

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Define the Solution class with the provided method
class Solution:
    def flattenBST(self, root):
        prev, head = None, root

        def dfs(node):
            nonlocal prev, head

            if not node:
                return

            if node.data != -1:  # Skip nodes with -1 value
                dfs(node.left)

                if not prev:
                    head = node
                else:    
                    node.left = None
                    prev.right = node

                prev = node
                dfs(node.right)

        dfs(root)
        return head

# Create a binary search tree
root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(8)

# Instantiate the Solution class
solution = Solution()

# Flatten the binary search tree
flattened_head = solution.flattenBST(root)

# Print the flattened linked list
current = flattened_head
while current:
    print(current.data, end=" ")
    current = current.right
