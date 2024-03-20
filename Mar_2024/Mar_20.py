# Sum of nodes on the longest path from root to leaf node

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def longestPathUtil(self, root):
        if not root:
            return (0, 0)  # Return (length, sum) for an empty tree

        # Recursively find the longest path and sum for left and right subtrees
        left_length, left_sum = self.longestPathUtil(root.left)
        right_length, right_sum = self.longestPathUtil(root.right)

        # Compare the lengths of left and right subtrees
        if left_length > right_length:
            max_length = left_length + 1
            max_sum = left_sum + root.data
        elif right_length > left_length:
            max_length = right_length + 1
            max_sum = right_sum + root.data
        else:
            # If lengths are equal, choose the path with maximum sum
            max_length = left_length + 1
            max_sum = max(left_sum, right_sum) + root.data

        return (max_length, max_sum)

    def sumOfLongRootToLeafPath(self, root):
        # Call the utility function to find the longest path and sum
        _, max_sum = self.longestPathUtil(root)
        return max_sum

# Example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

solution = Solution()
result = solution.sumOfLongRootToLeafPath(root)
print("Sum of longest root-to-leaf path:", result)
