# Paths from root with a specified sum

class Solution:
    def __init__(self):
        pass

    def dfs(self, root, sum, curr, temp, ans):
        if root is None:
            return
        
        curr += root.data
        temp.append(root.data)
        
        if curr == sum:
            ans.append(temp.copy())
        
        self.dfs(root.left, sum, curr, temp, ans)
        self.dfs(root.right, sum, curr, temp, ans)
        temp.pop()  # Backtrack

    def printPaths(self, root, sum):
        ans = []
        temp = []
        self.dfs(root, sum, 0, temp, ans)
        return ans

  class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Example usage of the Solution class
if __name__ == "__main__":
    # Create a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left = TreeNode(2)
    root.right.left.right = TreeNode(5)

    # Create an instance of the Solution class
    solution = Solution()

    # Find paths with a sum of 8 in the binary tree
    target_sum = 8
    result = solution.printPaths(root, target_sum)

    # Print the result
    print("Paths with sum", target_sum, ":", result)
