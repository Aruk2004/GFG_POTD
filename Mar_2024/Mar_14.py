# Largest subsquare surrounded by X

# Define the class
class Solution:
    def largestSubsquare(self, n, a):
        col = [[0]*n for _ in range(n)]
        row = [[0]*n for _ in range(n)]
        
        for i in range(n):
            sum_col = 0
            for j in range(n-1, -1, -1):
                sum_col = 0 if a[i][j] == 'O' else sum_col + 1
                col[i][j] = sum_col
        
        for j in range(n):
            sum_row = 0
            for i in range(n-1, -1, -1):
                sum_row = 0 if a[i][j] == 'O' else sum_row + 1
                row[i][j] = sum_row
        
        out = 0
        for i in range(n):
            for j in range(n):
                sq = min(col[i][j], row[i][j])
                while sq > out:
                    if col[i + sq - 1][j] >= sq and row[i][j + sq - 1] >= sq:
                        out = sq
                    sq -= 1
        return out

# Example usage
if __name__ == "__main__":
    solution = Solution()
    n = 4
    a = [['O', 'O', 'O', 'O'],
         ['X', 'X', 'O', 'O'],
         ['X', 'X', 'O', 'O'],
         ['X', 'X', 'O', 'O']]
    result = solution.largestSubsquare(n, a)
    print("Size of the largest subsquare:", result)
