# Sum of leaf nodes in BST

# Define the TreeNode class to represent a node in the binary tree
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Define the Solution class
class Solution:
    def sumOfLeafNodes(self, root):
        if root is None:
            return 0

        # Initialize the sum
        leaf_sum = 0

        # Helper function to perform DFS
        def dfs(node):
            nonlocal leaf_sum
            if node is None:
                return

            # If node is a leaf node, add its value to the sum
            if node.left is None and node.right is None:
                leaf_sum += node.data

            # Recursively traverse left and right subtrees
            dfs(node.left)
            dfs(node.right)

        # Start DFS from the root
        dfs(root)

        return leaf_sum

# Example usage
if __name__ == "__main__":
    # Construct a binary tree
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(20)

    # Instantiate the Solution class
    sol = Solution()

    # Calculate the sum of leaf nodes
    leaf_sum = sol.sumOfLeafNodes(root)

    # Print the result
    print("Sum of leaf nodes:", leaf_sum)

