# Largest Number formed from an Array

from functools import cmp_to_key

class Solution:
    def printLargest(self, n, arr):
        def compare(a, b):
            return int(b + a) - int(a + b)  # Custom comparison function
        
        arr.sort(key=cmp_to_key(compare))
        return ''.join(arr)

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    arr = ["54", "546", "548", "60"]
    result = sol.printLargest(len(arr), arr)
    print(result)  # Output: "6054854654"
