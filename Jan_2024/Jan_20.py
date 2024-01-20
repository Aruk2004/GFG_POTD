# Distribute candies in a binary tree

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def solve(self, root, moves):
        if not root:
            return 0

        left = self.solve(root.left, moves)
        right = self.solve(root.right, moves)
        moves[0] += abs(left) + abs(right)

        return root.data - 1 + left + right

    def distributeCandy(self, root):
        moves = [0]
        self.solve(root, moves)
        return moves[0]

# Example usage:
# Assuming you have a binary tree, create the tree and then use the Solution class
# to calculate the total number of moves required to distribute candies.

# Example tree creation:
#        1
#       / \
#      2   3
#     / \
#    4   5

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

sol = Solution()
total_moves = sol.distributeCandy(root)
print("Total moves required to distribute candies:", total_moves)
