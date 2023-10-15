# Normal BST to Balanced BST

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.arr = []

    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        self.arr.append(node.data)
        self.inorder(node.right)

    def createBST(self, low, high):
        if low > high:
            return None

        mid = (low + high) // 2
        root = Node(self.arr[mid])

        root.left = self.createBST(low, mid - 1)
        root.right = self.createBST(mid + 1, high)

        return root

    def buildBalancedTree(self, root):
        self.inorder(root)
        return self.createBST(0, len(self.arr) - 1)

# Example usage:
root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right = Node(5)

sol = Solution()
balanced_root = sol.buildBalancedTree(root)

def printInorder(node):
    if not node:
        return
    printInorder(node.left)
    print(node.data, end=" ")
    printInorder(node.right)

print("In-order traversal of the Balanced Binary Search Tree:")
printInorder(balanced_root)  # Output: 1 2 3 4 5
