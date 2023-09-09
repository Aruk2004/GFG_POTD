# Kth largest element in BST

class Solution:
    def __init__(self):
        self.ans = None

    def modified_inorder(self, root, k):
        if not root:
            return k

        k = self.modified_inorder(root.right, k)
        
        k -= 1
        if k == 0:
            self.ans = root.data
            return 0  # Stop further traversal
        
        k = self.modified_inorder(root.left, k)
        
        return k

    def kthLargest(self, root, k):
        self.modified_inorder(root, k)
        return self.ans

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Create a sample BST
root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

solution = Solution()
k = 3  # Find the 3rd largest element
result = solution.kthLargest(root, k)
print(f"The {k}th largest element is: {result}")
