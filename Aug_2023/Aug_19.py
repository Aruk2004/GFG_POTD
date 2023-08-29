#Function to find a continuous sub-array which adds up to a given number.

class Solution:
    def subarraySum(self, arr, n, s):
        out = []
        i = 0
        sum = 0
        
        for j in range(n):
            sum += arr[j]
            while sum > s and i < j:
                sum -= arr[i]
                i += 1
            if sum == s:
                out.append(i + 1)
                out.append(j + 1)
                return out
        
        out.append(-1)
        return out
  
# Example usage
solution = Solution()
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)
s = 15
result = solution.subarraySum(arr, n, s)
print(result)  # Output: [1, 5]
