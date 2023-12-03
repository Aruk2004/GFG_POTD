# Brothers From Different Roots

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def inorder(self, root, v):
        if not root:
            return

        self.inorder(root.left, v)
        v.append(root.data)
        self.inorder(root.right, v)

    def countPairs(self, root1, root2, x):
        t1, t2 = [], []

        self.inorder(root1, t1)
        self.inorder(root2, t2)

        i, j = 0, len(t2) - 1
        out = 0

        while i < len(t1) and j >= 0:
            current_sum = t1[i] + t2[j]
            if current_sum > x:
                j -= 1
            elif current_sum < x:
                i += 1
            else:
                out += 1
                i += 1
                j -= 1

        return out

# Constructing the first BST
root1 = Node(5)
root1.left = Node(3)
root1.right = Node(7)
root1.left.left = Node(2)
root1.left.right = Node(4)

# Constructing the second BST
root2 = Node(10)
root2.left = Node(6)
root2.right = Node(15)
root2.left.left = Node(4)
root2.left.right = Node(8)

# Creating an instance of the Solution class
solution = Solution()

# Counting pairs with sum equal to 10
result = solution.countPairs(root1, root2, 10)

# Printing the result
print(result)
