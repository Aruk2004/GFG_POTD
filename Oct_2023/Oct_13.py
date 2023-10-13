# Floor in BST

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def floor(self, root, x):
        floor_value = -1

        while root is not None:
            if root.data == x:
                return x
            elif root.data < x:
                floor_value = root.data
                root = root.right
            else:
                root = root.left

        return floor_value

# Example usage:
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.right = Node(20)

sol = Solution()
x = 8
result = sol.floor(root, x)
print(f"Floor of {x} in the Binary Search Tree: {result}")  # Output: 7
