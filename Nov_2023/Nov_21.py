# Determine if Two Trees are Identical

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    # Function to check if two trees are identical.
    def isIdentical(self, root1, root2):
        # Base case: If both nodes are None, they are identical
        if not root1 and not root2:
            return True
        # If one of the nodes is None and the other is not, they are not identical
        elif not root1 or not root2:
            return False
        # Compare the values of the current nodes and recursively check the left and right subtrees
        else:
            return (
                root1.data == root2.data
                and self.isIdentical(root1.left, root2.left)
                and self.isIdentical(root1.right, root2.right)
            )

# Example usage:
# Constructing two sample binary trees
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)

# Creating an instance of Solution
solution = Solution()

# Checking if the trees are identical
result = solution.isIdentical(root1, root2)
print("Yes" if result else "No")
