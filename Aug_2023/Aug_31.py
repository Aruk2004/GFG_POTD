#AVL Tree node deletion

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

def height(node):
    if node is None:
        return 0
    return node.height

def get_balance_factor(node):
    if node is None:
        return 0
    return height(node.left) - height(node.right)

def left_rotate(root):
    new_mid = root.right
    temp = new_mid.left

    new_mid.left = root
    root.right = temp

    root.height = max(height(root.left), height(root.right)) + 1
    new_mid.height = max(height(new_mid.left), height(new_mid.right)) + 1

    return new_mid

def right_rotate(root):
    new_mid = root.left
    temp = new_mid.right

    new_mid.right = root
    root.left = temp

    root.height = max(height(root.left), height(root.right)) + 1
    new_mid.height = max(height(new_mid.left), height(new_mid.right)) + 1

    return new_mid

def successor_inorder(root):
    curr = root
    while curr and curr.left is not None:
        curr = curr.left
    return curr

def delete_node(root, data):
    if root is None:
        return root

    if data < root.data:
        root.left = delete_node(root.left, data)
    elif data > root.data:
        root.right = delete_node(root.right, data)
    else:
        if root.left is None and root.right is None:
            return None
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        successor = successor_inorder(root.right)
        root.data = successor.data
        root.right = delete_node(root.right, successor.data)

    if root is None:
        return root

    root.height = max(height(root.left), height(root.right)) + 1
    balance = get_balance_factor(root)

    if balance <= 1 and balance >= -1:
        return root

    if balance > 1 and get_balance_factor(root.left) >= 0:
        return right_rotate(root)

    if balance > 1 and get_balance_factor(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    if balance < -1 and get_balance_factor(root.right) <= 0:
        return left_rotate(root)

    if balance < -1 and get_balance_factor(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)

def insert(root, data):
    if root is None:
        return Node(data)
    
    # Perform regular BST insertion
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    else:
        # Duplicate values are not allowed, so return the current root
        return root

    # Update the height of the current node
    root.height = max(height(root.left), height(root.right)) + 1

    # Check and balance the node after insertion
    balance = get_balance_factor(root)

    # Left Heavy
    if balance > 1:
        if data < root.left.data:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    # Right Heavy
    if balance < -1:
        if data > root.right.data:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root


def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.data))
        print_tree(root.left, level + 1, "L--- ")
        print_tree(root.right, level + 1, "R--- ")

if __name__ == "__main__":
    # Create an AVL tree
    root = None

    # Insert nodes
    values = [10, 20, 30, 40, 50, 25]
    for value in values:
        root = insert(root, value)

    print("Original AVL tree:")
    print_tree(root)

    # Delete a node
    delete_value = 30
    root = delete_node(root, delete_value)
    print(f"AVL tree after deleting {delete_value}:")
    print_tree(root)
