#Minimum operations to make matrix Beautiful

class Solution:
    def findMinOperation(self, a, n):
        maxRow, maxCol, total = 0, 0, 0
        
        for i in range(n):
            sumRow, sumCol = 0, 0
            
            for j in range(n):
                sumRow += a[i][j]
                sumCol += a[j][i]
                total += a[i][j]
                
            maxRow = max(maxRow, sumRow)
            maxCol = max(maxCol, sumCol)
        
        return max(maxRow * n, maxCol * n) - total

if __name__ == "__main__":
    solution = Solution()
    
    # Example matrix and size
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    size = 3
    
    result = solution.findMinOperation(matrix, size)
    print("Minimum operations:", result)
