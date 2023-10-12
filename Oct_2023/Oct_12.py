# Duplicate subtree in Binary Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def same(x, y):
    if (x is None) ^ (y is None):
        return False
    if (x is None) and (y is None):
        return True
    if x.data != y.data:
        return False

    return same(x.left, y.left) and same(x.right, y.right)

class Solution:
    def dupSub(self, root):
        nodes = []

        queue = [root]

        while queue:
            cur = queue.pop(0)

            leaf = True

            if cur.left is not None:
                queue.append(cur.left)
                leaf = False
            if cur.right is not None:
                queue.append(cur.right)
                leaf = False

            if not leaf:
                nodes.append(cur)

        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                if same(nodes[i], nodes[j]):
                    return 1

        return 0

# Example usage:
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(2)
root.right.left.left = Node(4)
root.right.right = Node(5)
solution = Solution()
result = solution.dupSub(root)
print(result)
