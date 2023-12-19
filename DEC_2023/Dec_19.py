# Rightmost different bit

class Solution:
    
    # Function to find the first position with different bits.
    def posOfRightMostDiffBit(self, m, n):
        # Find the XOR of m and n
        xor_result = m ^ n
        
        # Find the position of the rightmost set bit
        if xor_result == 0:
            return -1  # m and n are the same
        
        position = 1
        while xor_result:
            if xor_result & 1:
                return position
            xor_result >>= 1
            position += 1

# Example usage:
sol = Solution()
M = 10   # Binary: 1010
N = 15   # Binary: 1111

result = sol.posOfRightMostDiffBit(M, N)
print("Position of rightmost different bit:", result)
