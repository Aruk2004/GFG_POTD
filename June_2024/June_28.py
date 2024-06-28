# The Palindrome Pattern

class Solution:
    def pattern (self, arr):
        n = len(arr)
        m = len(arr[0]) if n > 0 else 0

        for i in range(n):
            if arr[i] == arr[i][::-1]:
                return str(i) + ' ' + "R"
        for j in range(m):
            col = [arr[i][j] for i in range(n)]
            if col == col[::-1]:
                return str(j)+ ' ' +"C"
        return -1
