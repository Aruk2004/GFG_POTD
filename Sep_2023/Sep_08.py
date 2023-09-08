# Binary tree to BST

class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Solution:
    def inorder(self, root, nodes):
        if not root:
            return
        
        self.inorder(root.left, nodes)
        nodes.append(root)
        self.inorder(root.right, nodes)

    def binaryTreeToBST(self, root):
        nodes = []
        self.inorder(root, nodes)
        values = [node.data for node in nodes]
        
        values.sort()

        for i in range(len(nodes)):
            nodes[i].data = values[i]

        return root

# Helper function to print the tree in an inorder traversal (for verification)
def print_tree_inorder(node):
    if node:
        print_tree_inorder(node.left)
        print(node.data, end=' ')
        print_tree_inorder(node.right)

# Create a sample binary tree
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(5)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.right.left = TreeNode(4)
root.right.right = TreeNode(6)

# Initialize the Solution class
solution = Solution()

# Convert the binary tree to a BST
bst_root = solution.binaryTreeToBST(root)

# Print the resulting BST in inorder traversal (for verification)
print_tree_inorder(bst_root)
