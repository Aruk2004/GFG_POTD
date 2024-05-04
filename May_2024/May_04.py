# Construct Binary Tree from Inorder and Postorder

class Solution:
    def buildTree(self, In, post, n):
        if not In or not post:
            return 
        index = In.index(post[-1])
        root = Node(post[-1])
        root.left = self.buildTree(In[0:index],post[0:index],n)
        root.right = self.buildTree(In[index+1:],post[index:-1],n)
        return root

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Example usage
if __name__ == "__main__":
    # Inorder and postorder traversal sequences
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    
    # Instantiate the Solution class
    solution = Solution()
    
    # Build the binary tree
    root = solution.buildTree(inorder, postorder, len(inorder))
    
    # Function to print inorder traversal of the tree
    def inorderTraversal(root):
        if root:
            inorderTraversal(root.left)
            print(root.data, end=" ")
            inorderTraversal(root.right)
    
    # Print the inorder traversal of the constructed tree
    print("Inorder Traversal of the constructed tree:")
    inorderTraversal(root)
