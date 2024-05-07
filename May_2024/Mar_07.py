# Reverse Level Order Traversa

from collections import deque

# Define the Node class for the binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def reverseLevelOrder(root):
    # Base case: if the tree is empty, return an empty list
    if not root:
        return []

    # Initialize an empty deque to perform level-order traversal
    queue = deque()
    # Initialize a list to store the reverse level order traversal
    reverse_traversal = []

    # Add the root node to the queue
    queue.append(root)

    # Perform level-order traversal
    while queue:
        # Get the size of the current level
        level_size = len(queue)
        # Initialize a list to store nodes at the current level
        level_nodes = []

        # Traverse all nodes at the current level
        for _ in range(level_size):
            # Pop the front node from the queue
            node = queue.popleft()
            # Append the data of the node to the level_nodes list
            level_nodes.append(node.data)

            # Enqueue the left and right children of the current node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Prepend the level_nodes list to the reverse_traversal list
        reverse_traversal = level_nodes + reverse_traversal

    # Return the reverse level order traversal
    return reverse_traversal

# Example usage
if __name__ == "__main__":
    # Create the binary tree
    root = Node(1)
    root.left = Node(3)
    root.right = Node(2)
    root.left.left = Node(5)
    root.left.right = Node(4)

    # Get the reverse level order traversal of the binary tree
    result = reverseLevelOrder(root)

    # Print the reverse level order traversal
    print("Reverse Level Order Traversal:", result)
