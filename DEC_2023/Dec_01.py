# Check whether BST contains Dead End

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.arr = [0]  # Initialize with a 0 value to handle the edge case of root being 1.
        self.leaf = []

    def inorder(self, node):
        if not node:
            return
        
        self.inorder(node.left)
        self.arr.append(node.data)
        if not node.left and not node.right:
            self.leaf.append(node.data)
        self.inorder(node.right)

    def isDeadEnd(self, root):
        self.arr = [0]
        self.leaf = []
        self.inorder(root)
        
        j = 0
        for i in range(1, len(self.arr) - 1):
            if self.arr[i] == self.leaf[j]:
                if self.arr[i - 1] == self.leaf[j] - 1 and self.arr[i + 1] == self.leaf[j] + 1:
                    return True
                j += 1
        
        return False

    def isDeadEndForMultipleTrees(self, trees):
        results = []
        for tree in trees:
            result = self.isDeadEnd(tree)
            results.append(result)
        return results

# Example usage with multiple test cases:
tree1 = Node(8)
tree1.left = Node(5)
tree1.right = Node(9)
tree1.left.left = Node(2)
tree1.left.right = Node(7)

tree2 = Node(10)
tree2.left = Node(5)
tree2.right = Node(15)
tree2.left.left = Node(2)
tree2.left.right = Node(7)
tree2.right.right = Node(20)

# Use the Solution class for multiple test cases.
solution = Solution()
results = solution.isDeadEndForMultipleTrees([tree1, tree2])
print(results)
