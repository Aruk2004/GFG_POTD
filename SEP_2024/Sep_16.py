# Longest valid Parentheses

class Solution:
    def maxLength(self, s: str) -> int:
        # Initialize a stack with -1 to handle edge cases
        stack = [-1]
        max_len = 0
        
        # Iterate through the string
        for i in range(len(s)):
            if s[i] == '(':
                # Push the index of '(' onto the stack
                stack.append(i)
            else:
                # Pop the topmost element
                stack.pop()
                
                # If the stack is not empty, calculate the valid length
                if stack:
                    max_len = max(max_len, i - stack[-1])
                else:
                    # Push the current index if the stack is empty (new boundary)
                    stack.append(i)
        
        return max_len
