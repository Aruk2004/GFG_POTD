#Leaf under Budget

from queue import Queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getCount(self, root, k):
        q = Queue()
        q.put((root, 1))
        cnt = 0

        while not q.empty() and k > 0:
            node, level = q.get()

            if not node.left and not node.right:
                if level > k:
                    return cnt

                cnt += 1
                k -= level
            else:
                if node.left:
                    q.put((node.left, level + 1))
                if node.right:
                    q.put((node.right, level + 1))

        return cnt

# Example usage:
if __name__ == "__main__":
    # Create a sample binary tree
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution()
    k = 2
    result = solution.getCount(root, k)
    print(f"Number of leaf nodes with depth greater than {k}: {result}")
