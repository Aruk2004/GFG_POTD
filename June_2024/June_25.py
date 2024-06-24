# Left Rotate Matrix K times

class Solution:
    def rotateMatrix(self, k, mat):
        rows = len(mat)
        if rows == 0:
            return mat
        cols = len(mat[0])
        
        # Normalize k
        k = k % cols
        
        # Rotate each row to the left by k positions
        for i in range(rows):
            mat[i] = mat[i][k:] + mat[i][:k]
        
        return mat

# Example usage:
solution = Solution()
k = 2
mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotated_mat
