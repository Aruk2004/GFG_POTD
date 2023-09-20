#Rotate Bits

class Solution:
    def rotate(self, n: int, d: int):
        mask_16 = (1 << 16) - 1
        d = d % 16

        out = [0, 0]
        out[0] = (n << d | n >> (16 - d)) & mask_16
        out[1] = (n >> d | n << (16 - d)) & mask_16

        return out

# Example usage
if __name__ == "__main__":
    solution = Solution()
    n = 12345
    d = 3
    result = solution.rotate(n, d)
    print("Rotated values:", result)
