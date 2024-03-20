# ZigZag Tree Traversal

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    # Function to store the zigzag order traversal of the tree in a list.
    def zigZagTraversal(self, root):
        if not root:
            return []

        result = []
        current_level = []
        next_level = []
        left_to_right = True
        current_level.append(root)

        while current_level:
            node = current_level.pop()
            result.append(node.data)

            if left_to_right:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            else:
                if node.right:
                    next_level.append(node.right)
                if node.left:
                    next_level.append(node.left)

            if not current_level:
                current_level, next_level = next_level, current_level
                left_to_right = not left_to_right

        return result

# Example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

solution = Solution()
result = solution.zigZagTraversal(root)
print("Zigzag level order traversal:", result)
