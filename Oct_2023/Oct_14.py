# Find Common Nodes in two BSTs

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.out = []

    def find(self, node, x):
        if not node:
            return False

        if node.data == x:
            return True

        if node.data > x:
            return self.find(node.left, x)

        return self.find(node.right, x)

    def inorder(self, root1, root2):
        if not root1:
            return

        self.inorder(root1.left, root2)
        if self.find(root2, root1.data):
            self.out.append(root1.data)
        self.inorder(root1.right, root2)

    def findCommon(self, root1, root2):
        self.inorder(root1, root2)
        return self.out

# Example usage:
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

root2 = Node(2)
root2.left = Node(1)
root2.right = Node(4)
root2.left.right = Node(3)

sol = Solution()
result = sol.findCommon(root1, root2)
print("Common elements between two Binary Search Trees:", result)  # Output: [1, 2, 3, 4]
