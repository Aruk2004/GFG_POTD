# Root to leaf path sum


class Solution:

    def hasPathSum(self, root, target):

        def f(root,s):

            if not root:
                return

            s += root.data

            if s == target and not root.left and not root.right:
                return True

            if s != target and (not root.left and not root.right):
                return False

            l = f(root.left,s)
            r = f(root.right,s)

            return l or r

        return f(root,0)
