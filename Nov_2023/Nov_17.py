# Binary Tree to CDLL

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.head = None
        self.tail = None

    def inorder(self, root):
        if not root:
            return

        self.inorder(root.left)

        curr = Node(root.data)
        if self.tail:
            self.tail.right = curr
            curr.left = self.tail
        else:
            self.head = curr
        self.tail = curr

        self.inorder(root.right)

    def bTreeToCList(self, root):
        self.tail = self.head = None

        self.inorder(root)

        self.head.left = self.tail
        self.tail.right = self.head

        return self.head

# Example usage:
# Creating a sample binary tree
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

# Creating an instance of Solution
solution = Solution()

# Converting the binary tree to a circular doubly linked list
circular_list_head = solution.bTreeToCList(root)

# Printing the circular doubly linked list
current = circular_list_head
while current:
    print(current.data, end=" ")
    current = current.right
    if current == circular_list_head:
        break
