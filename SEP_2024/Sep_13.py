# Mirror Tree

class Solution:
    def mirror(self, node):
        if node is None:
            return

        self.mirror(node.left)
        self.mirror(node.right)

        node.left, node.right = node.right, node.left
