# Index of an Extra Element

class Solution:
    def findExtra(self, n, a, b):
        for i in range(n - 1):
          if a[i] != b[i]:
              return i
        return n - 1
