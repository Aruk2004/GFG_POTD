# Binary representation of next number

class Solution:
    def binaryNextNumber(self, s):
        result = int(s, 2)
        return bin(result + 1)[2:]
