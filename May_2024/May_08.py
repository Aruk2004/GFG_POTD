# Root to Leaf Paths

class Solution:
    def Paths(self, root : Optional['Node']) -> List[List[int]]:
        temp = []
        ans = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node == -1:
                temp.pop()
                continue
            temp.append(node.data)
            stack.append(-1)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            if not (node.left or node.right):
                ans.append(temp[:])
        return ans

  class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Example usage
if __name__ == "__main__":
    # Create a binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    # Instantiate the Solution class
    solution = Solution()

    # Get the root-to-leaf paths
    paths = solution.Paths(root)

    # Print the root-to-leaf paths
    print("Root-to-leaf Paths:")
    for path in paths:
        print(path)
