# Kth Smallest

class Solution:

    def kthSmallest(self, arr, k):

        arr = sorted(arr)
        return arr[k - 1]
