# Count pairs Sum in matrices

# Define the class
class Solution:
    def countPairs(self, mat1, mat2, n, x):
        sz = n * n
        l, r = 0, sz - 1
        cnt = 0
        
        while l < sz and r >= 0:
            sum_val = mat1[l // n][l % n] + mat2[r // n][r % n]
            
            if sum_val == x:
                l += 1
                r -= 1
                cnt += 1
            elif sum_val > x:
                r -= 1
            else:
                l += 1
        
        return cnt

# Example usage
if __name__ == "__main__":
    solution = Solution()
    mat1 = [[1, 3, 5], [2, 4, 7], [6, 8, 9]]
    mat2 = [[2, 1, 6], [3, 5, 8], [4, 7, 9]]
    n = 3
    x = 10
    result = solution.countPairs(mat1, mat2, n, x)
    print("Number of pairs with sum equal to", x, ":", result)
