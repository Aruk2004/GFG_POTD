# K distance from root

class Solution:
    def KDistance(self,root,k):
        queue=[]
        ans=[]

        count=0
        queue.append(root)
        while queue and count<=k+1:
            level=[]
            for i in range(len(queue)):
                node=queue.pop(0)
                if node:
                    level.append(node.data)
                    queue.append(node.left)
                    queue.append(node.right)

            if level:
                ans.append(level)
                count+=1

        return ans[k] if len(ans)>k else []

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Example usage
if __name__ == "__main__":
    # Create a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    # Instantiate the Solution class
    solution = Solution()
    
    # Find nodes at distance K from the root
    k_distance_nodes = solution.KDistance(root, 2)
    
    # Display the nodes at distance K from the root
    print("Nodes at distance 2 from the root:", k_distance_nodes)
