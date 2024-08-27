# Maximum Difference

class Solution:
    def findMaxDiff(self, arr):
        n = len(arr)
        
        # Arrays to store nearest smaller elements
        left_smaller = [0] * n
        right_smaller = [0] * n
        
        # Stack to find nearest left smaller elements
        stack = []
        
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                left_smaller[i] = arr[stack[-1]]
            else:
                left_smaller[i] = 0
            stack.append(i)
        
        # Clear the stack for the next pass
        stack.clear()
        
        # Stack to find nearest right smaller elements
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                right_smaller[i] = arr[stack[-1]]
            else:
                right_smaller[i] = 0
            stack.append(i)
        
        # Calculate the maximum absolute difference
        max_diff = 0
        for i in range(n):
            max_diff = max(max_diff, abs(left_smaller[i] - right_smaller[i]))
        
        return max_diff
