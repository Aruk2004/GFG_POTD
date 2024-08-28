# Sorting Elements of an Array by Frequency

from collections import Counter 
class Solution:
    def sortByFreq(self,arr):
        freq = Counter(arr)
        s = sorted(arr, key = lambda x:(-freq[x], x))
        return s
