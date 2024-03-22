# Diagonal sum in binary tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    #Complete the function below
    def diagonalSum(self, root):
        #:param root: root of the given tree.

        #code here
      if not root:
        return []
      dic={}
      def find(level,root):
        if not root: return
        if level not in dic:
            dic[level]=[root.data]
        else: dic[level].append(root.data)
        if root.left: find(level+1,root.left)
        if root.right: find(level,root.right)

      ans=[]
      find(0,root)
      # print(dic)
      for i in dic:
        ans.append(sum(dic[i]))
      return ans



# Example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

solution = Solution()
result = solution.diagonalSum(root)
print("Diagonal sums:", result)
