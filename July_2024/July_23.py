# Merge two BST 's

class Solution:
    def merge(self, root1, root2):
        def inorder(root,ans):
            if root==None:
                return 
            inorder(root.left,ans)
            ans.append(root.data)
            inorder(root.right,ans)
        ans=[]
        inorder(root1,ans)
        inorder(root2,ans)
        ans.sort()
        return ans
