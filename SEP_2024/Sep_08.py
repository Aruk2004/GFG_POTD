# Minimum Jumps

class Solution:
	def minJumps(self, arr):
        curr_reach, max_reach, jump_count = 0, 0, 0
        for i in range(len(arr) - 1):
            max_reach = max(max_reach, i + arr[i])
            if curr_reach == i:
                if max_reach == i:
                    return -1
                jump_count += 1
                curr_reach = max_reach
        return jump_count
