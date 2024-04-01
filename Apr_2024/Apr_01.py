# Pairs violating the BST property

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def pairsViolatingBST(self, n, root):
        s = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            s.append(node.data)
            inorder(node.right)
        inorder(root)

        ans = 0
        def mergesort(arr):
            nonlocal ans
            if len(arr) <= 1:
                return arr

            mi = len(arr) // 2
            a = mergesort(arr[:mi])
            b = mergesort(arr[mi:])
            i, j, ret = 0, 0, []
            while i < len(a) and j < len(b):
                if a[i] <= b[j]:
                    ret.append(a[i])
                    i += 1
                else:
                    ans += len(a) - i
                    ret.append(b[j])
                    j += 1
            if i < len(a):
                ret.extend(a[i:])
            if j < len(b):
                ret.extend(b[j:])
            return ret
        mergesort(s)
        return ans

# Example usage
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(10)

solution = Solution()
pairs_count = solution.pairsViolatingBST(7, root)
print("Number of pairs violating BST property:", pairs_count)  # Output: 1
