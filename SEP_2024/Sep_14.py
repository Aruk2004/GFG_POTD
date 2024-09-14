# Alternate positive and negative numbers

class Solution:
    def rearrange(self,arr):
        pos = []
        neg = []

        for i in range(len(arr)):
            if arr[i] >= 0:
                pos.append(arr[i])
            else:
                neg.append(arr[i])

        i = 0
        j = 0
        index = 0

        while i < len(pos) or j < len(neg):
            if i < len(pos):
                arr[index] = pos[i]
                i += 1
                index += 1
            if j < len(neg):
                arr[index] = neg[j]
                j += 1
                index += 1
