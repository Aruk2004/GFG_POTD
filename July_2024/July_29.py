# Row with max 1s

class Solution:
	def rowWithMax1s(self,arr):
	    m = 0
	    r = -1
	    for ind, row in enumerate(arr):
	        t = sum(row)
	        if t > m:
	            m = t
	            r = ind
	        if t == len(row):
	            return r
	    return r
