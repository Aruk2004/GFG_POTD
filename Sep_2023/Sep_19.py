# Find first set bit

class Solution:
    def getFirstSetBit(self, n: int) -> int:
        cnt = 0
        while n:
            cnt += 1
            if n & 1:
                break
            n >>= 1
        return cnt

# Example usage
if __name__ == "__main__":
    solution = Solution()
    n = 18  # Binary representation: 10010
    firstSetBitPosition = solution.getFirstSetBit(n)
    print("Position of the first set bit:", firstSetBitPosition)
