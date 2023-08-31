#AVL Tree Deletion

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

def deleteNode(root, data):
    if not root:
        return root

    if data < root.data:
        root.left = deleteNode(root.left, data)
        
    elif data > root.data:
        root.right = deleteNode(root.right, data)
        
    else:
        if root.left is None and root.right is None:
            return None
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        successor = successor_inorder(root.right)
        root.data = successor.data
        root.right = deleteNode(root.right, successor.data)

    if not root:
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

#Driver code
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1  # Initial height for a new node is 1

# Insert a node into the AVL tree
def insert(root, data):
    if root is None:
        return Node(data)
    
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    
    root.height = max(height(root.left), height(root.right)) + 1
    balance = get_balance_factor(root)
    
    # Perform rotations to restore AVL balance
    # ... (similar to the rotations in your code)

    return root

# Example usage
if __name__ == "__main__":
    root = None
    
    data = [10, 20, 30, 40, 50, 25]
    for value in data:
        root = insert(root, value)
    
    print("Inorder traversal of the AVL tree:")
    inorder_traversal(root)
