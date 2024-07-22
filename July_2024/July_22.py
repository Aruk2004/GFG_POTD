# Largest BST

class Solution:
    def largestBst(self, root):
        # Your code here
        def largestBSTHelper(node):
            if not node:
                # Base case: Empty tree, return (isBST, size, min_value, max_value)
                return True, 0, float('inf'), float('-inf')

            # Recursively find BST properties for left and right subtrees
            left_isBST, left_size, left_min, left_max = largestBSTHelper(node.left)
            right_isBST, right_size, right_min, right_max = largestBSTHelper(node.right)

            # Check if current subtree rooted at 'node' is BST
            if (left_isBST and right_isBST and 
                left_max < node.data < right_min):
                # Calculate size of current BST
                current_size = 1 + left_size + right_size
                return True, current_size, min(left_min, node.data), max(right_max, node.data)
            else:
                # If current subtree is not BST, return the maximum of left and right subtree sizes
                return False, max(left_size, right_size), float('-inf'), float('inf')

        # Call the helper function to get the result
        isBST, size, _, _ = largestBSTHelper(root)
        return size
