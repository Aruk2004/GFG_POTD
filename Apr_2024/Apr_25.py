# Maximum sum of hour glass

class Solution:
    def hg(self,i,j,mat):
        return (mat[i][j]+mat[i][j+1]+mat[i][j+2]
                +mat[i+1][j+1]
                +mat[i+2][j]+mat[i+2][j+1]+mat[i+2][j+2])

    def findMaxSum(self,n,m,mat):
        if n<3:
            return -1
        ans=-float("inf")
        for i in range(n-2):
            for j in range(m-2):
                curr=self.hg(i,j,mat)
                ans=max(ans,curr)
        return ans

sol = Solution()
mat = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]
n = 4
m = 5
print(sol.findMaxSum(n, m, mat))  # Output: 76 (Maximum sum of hourglass in the matrix)
