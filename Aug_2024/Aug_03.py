# The Celebrity Problem

class Solution:
    def celebrity(self, mat):
        for i in range(len(mat)):
            a=1
            for j in range(len(mat)):
                if mat[i][j]==1:
                    a=0
                    break
            if a==1:
                for j in range(len(mat)):
                    if i!=j and mat[j][i]==0:
                        a=0
                        break
            if a==1:
                return i
        return -1
