# Check for BST

class Solution:

    #Function to check whether a Binary Tree is BST or not.
    def is_bst(self, node, min_val, max_val):
        if node is None:
            return True
        if not (min_val < node.data < max_val):
            return False
        return self.is_bst(node.left, min_val, node.data) and self.is_bst(node.right, node.data, max_val)

    def isBST(self, root):
        return self.is_bst(root, float('-inf'), float('inf'))
