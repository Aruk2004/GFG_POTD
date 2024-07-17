# Construct Binary Tree from Parent Array

class Solution:
    def createTree(self,parent):
        n = len(parent)
        created = [None]*n

        root = None

        for i in range(n):
            if created[i] is None:
                created[i] = Node(i)
            if parent[i] == -1:
                root = created[i]
            else:
                if created[parent[i]] is None:
                    created[parent[i]] = Node(parent[i])

                p = created[parent[i]]
                if p.left is None:
                    p.left = created[i]
                else:
                    p.right = created[i]
        return root
