# Count the nodes at distance K from leaf

class Solution:
    def __init__(self):
        self.cnt = 0
    
    def dfs(self, node, k, lvl, mp):
        if not node:
            return
        
        mp[lvl] = False
        
        if not node.left and not node.right:
            if lvl - k >= 0 and not mp[lvl - k]:
                mp[lvl - k] = True
                self.cnt += 1
        
        lvl += 1
        self.dfs(node.left, k, lvl, mp)
        self.dfs(node.right, k, lvl, mp)
    
    def printKDistantfromLeaf(self, root, k):
        self.cnt = 0
        mp = {}
        self.dfs(root, k, 0, mp)
        return self.cnt

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Create a binary tree
#        1
#       / \
#      2   3
#     / \ 
#    4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Create an instance of Solution
sol = Solution()

# Calculate the count of nodes at distance 2 from leaf nodes
k = 2
count = sol.printKDistantfromLeaf(root, k)
print("Count of nodes at distance", k, "from leaf nodes:", count)
