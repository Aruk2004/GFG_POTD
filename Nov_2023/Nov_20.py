# K Sum Paths

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def __init__(self):
        self.count = 0

    def sumK(self, root, k):
        def dfs(node, current_sum, prefix_sum):
            nonlocal count

            if not node:
                return

            current_sum += node.data
            count += prefix_sum.get(current_sum - k, 0)

            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

            dfs(node.left, current_sum, prefix_sum)
            dfs(node.right, current_sum, prefix_sum)

            prefix_sum[current_sum] -= 1

        count = 0
        prefix_sum = {0: 1}
        dfs(root, 0, prefix_sum)

        return count

# Example usage:
# Constructing a sample binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)

# Creating an instance of Solution
solution = Solution()

# Finding the number of paths with sum equal to K (K = 3 in this example)
result = solution.sumK(root, 3)
print(result)
