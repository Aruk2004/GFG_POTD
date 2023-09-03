#check if Trees are isomorphic

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isIsomorphic(root1, root2):
    # Base case: If both roots are None, they are isomorphic
    if not root1 and not root2:
        return True

    # If one of the roots is None or their data is different, they are not isomorphic
    if not root1 or not root2 or root1.data != root2.data:
        return False

    # Check isomorphism in a flipped manner and in the same manner
    is_flip = isIsomorphic(root1.left, root2.right) and isIsomorphic(root1.right, root2.left)
    not_flip = isIsomorphic(root1.left, root2.left) and isIsomorphic(root1.right, root2.right)

    # Return True if either is_flip or not_flip is True
    return is_flip or not_flip

# Helper function to build a sample binary tree
def build_sample_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    return root

# Helper function to build another sample binary tree
def build_another_sample_tree():
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(6)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(4)
    return root

if __name__ == "__main__":
    root1 = build_sample_tree()
    root2 = build_another_sample_tree()

    if isIsomorphic(root1, root2):
        print("The trees are isomorphic.")
    else:
        print("The trees are not isomorphic.")
