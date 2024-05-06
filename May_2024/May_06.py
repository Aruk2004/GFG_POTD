# Print all nodes that don't have sibling

def noSibling(root):
    list = []
    def sibling(root,list):
        if root == None:
            return
        if (root.left == None and root.right != None):
            list.append(root.right.data)
        elif (root.left != None and root.right == None):
            list.append(root.left.data)
        sibling(root.left,list)
        sibling(root.right,list)
        return list
    sibling(root,list)
    if len(list) == 0:
        list.append(-1)
    return sorted(list)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Example usage
if __name__ == "__main__":
    # Creating a binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.left.left = Node(6)

    # Find nodes without siblings
    result = noSibling(root)

    # Display the result
    print("Nodes without siblings:", result)
