# Remove K Digits

class Solution:
    def removeKdigits(self, S, K):
        stack = []

        for digit in S:
            while K > 0 and stack and stack[-1] > digit:
                stack.pop()
                K -= 1
            stack.append(digit)

        # Remove remaining K digits from the end
        stack = stack[:-K] if K > 0 else stack

        # Join the digits in the stack to form the result
        result = ''.join(stack).lstrip('0')

        # If the result is empty, return '0'
        return result if result else '0'

# Example usage:
sol = Solution()

S1, K1 = "149811", 3
S2, K2 = "1002991", 3

result1 = sol.removeKdigits(S1, K1)
result2 = sol.removeKdigits(S2, K2)

print(result1)  # Output: "111"
print(result2)  # Output: "21"
