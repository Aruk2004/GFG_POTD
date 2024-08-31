# Sorted subsequence of size 3

class Solution:
    def find3Numbers(self, arr):
        smallest = 10**9
        for i in range(0,len(arr)):
            if arr[i] < smallest:
                smallest = arr[i]
                for j in range(i+1,len(arr)):
                    if arr[i] < arr[j]:
                        for k in range(j+1,len(arr)):
                            if arr[j] < arr[k]:
                                return [arr[i],arr[j],arr[k]]
        return []
