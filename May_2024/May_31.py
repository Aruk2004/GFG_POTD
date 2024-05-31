# Swap two nibbles in a byte

class Solution:
    def swapNibbles (self, n):
        return (n & 15) << 4 | n >> 4
