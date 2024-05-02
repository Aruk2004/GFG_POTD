# Serialize and deserialize a binary tree

class Solution:
    #Function to serialize a tree and return a list containing nodes of tree.
    def serialize(self, root):
        inor = []
        def inorder(root):
            if root == None:
                return 
            inorder(root.left)
            inor.append(root)
            inorder(root.right)
        inorder(root)
        preor = []
        def preorder(root):
            if root == None:
                return 
            preor.append(root)
            preorder(root.left)
            preorder(root.right)
        preorder(root)

        return [inor, preor]


    #Function to deserialize a list and construct the tree.   
    def deSerialize(self, a):
        inorder_ = a[0]
        preorder = a[-1]
        def f(inor,preor):
            if len(inor):
                node = Node(preor[0].data)
                temp = inor.index(preor[0])
                preor.pop(0)
                node.left = f(inor[:temp],preor)
                node.right = f(inor[temp + 1:],preor)
                return node
            else:
                return None


        return f(inorder_,preorder)

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Example usage
if __name__ == "__main__":
    # Create a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    # Instantiate the Solution class
    solution = Solution()
    
    # Serialize the tree
    serialized_tree = solution.serialize(root)
    
    # Display the serialized tree
    print("Serialized tree:")
    print("Inorder:", [node.data for node in serialized_tree[0]])
    print("Preorder:", [node.data for node in serialized_tree[1]])
    
    # Deserialize the list to construct the tree
    deserialized_tree = solution.deSerialize(serialized_tree)
    
    # Display the deserialized tree
    print("\nDeserialized tree:")
    print("Inorder:", [node.data for node in serialized_tree[0]])
    print("Preorder:", [node.data for node in serialized_tree[1]])
