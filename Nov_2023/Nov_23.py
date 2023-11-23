# AVL Tree Insertion

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
        self.height = 1


class Solution:
    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def insertToAVL(self, root, key):
        if not root:
            return Node(key)

        if key < root.data:
            root.left = self.insertToAVL(root.left, key)
        else:
            root.right = self.insertToAVL(root.right, key)

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance = self.balance_factor(root)

        # Left Heavy
        if balance > 1:
            # Left Right Case
            if key > root.left.data:
                root.left = self.left_rotate(root.left)
            # Left Left Case
            return self.right_rotate(root)

        # Right Heavy
        if balance < -1:
            # Right Left Case
            if key < root.right.data:
                root.right = self.right_rotate(root.right)
            # Right Right Case
            return self.left_rotate(root)

        return root


def inorder_traversal(root):
    result = []

    if root:
        result += inorder_traversal(root.left)
        result.append(root.data)
        result += inorder_traversal(root.right)

    return result


# Example usage:
# N = 7
# Values to be inserted = {21, 26, 30, 9, 4, 14, 28}
# Output:
# 4 9 14 21 26 28 30

# Creating an instance of the Solution class
sol = Solution()

# Initializing the root node
root = None

# Values to be inserted
keys = [21, 26, 30, 9, 4, 14, 28]

# Inserting values into the AVL tree and printing the inorder traversal after each insertion
for key in keys:
    root = sol.insertToAVL(root, key)
    inorder_result = inorder_traversal(root)
    print(" ".join(map(str, inorder_result)))
