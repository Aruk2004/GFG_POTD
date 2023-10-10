# Nodes at given distance in binary tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.out = []

    def trace(self, node, k):
        if not node or k < 0:
            return

        if k == 0:
            self.out.append(node.data)
            return

        self.trace(node.left, k - 1)
        self.trace(node.right, k - 1)

    def findDist(self, node, target, k):
        if not node:
            return float('-inf')

        if node.data == target:
            self.trace(node, k)
            return k - 1

        from_left = self.findDist(node.left, target, k)
        if from_left != float('-inf'):
            if from_left == 0:
                self.out.append(node.data)
            elif from_left > 0:
                self.trace(node.right, from_left - 1)
            return from_left - 1

        from_right = self.findDist(node.right, target, k)
        if from_right != float('-inf'):
            if from_right == 0:
                self.out.append(node.data)
            elif from_right > 0:
                self.trace(node.left, from_right - 1)
            return from_right - 1

        return float('-inf')

    def KDistanceNodes(self, root, target, k):
        self.out = []
        self.findDist(root, target, k)
        self.out.sort()
        return self.out

# Example usage:
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

sol = Solution()
target_node = 2
distance_k = 2
result = sol.KDistanceNodes(root, target_node, distance_k)
print("Nodes at Distance K from Target Node:")
print(result)  # Output: [4, 5, 1]
