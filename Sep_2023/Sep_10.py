# Insert Node into BST

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class Solution:
    def insert(self, node, key):
        if not node:
            return Node(key)

        if key > node.key:
            if not node.right:
                node.right = Node(key)
            else:
                self.insert(node.right, key)
        elif key < node.key:
            if not node.left:
                node.left = Node(key)
            else:
                self.insert(node.left, key)

        return node

 #Function to Print tree 
    def print_tree(self, node, level=0, prefix="Root: "):
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.key))
            if node.left is not None or node.right is not None:
                self.print_tree(node.left, level + 1, "L--- ")
                self.print_tree(node.right, level + 1, "R--- ")

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    root = None
    keys = [5, 3, 7, 2, 4, 6, 8]

    for key in keys:
        root = solution.insert(root, key)

    solution.print_tree(root)
