# Two Repeated Elements

class Solution:
    def twoRepeated(self, arr, n):
        seen = {}
        result = []
        for num in arr:
            if num in seen:
                if seen[num] == 1:
                    result.append(num)
                seen[num] += 1
            else:
                seen[num] = 1
        return result

s = Solution()
arr = [1, 2, 3, 2, 3, 4]
n = len(arr)
result = s.twoRepeated(arr, n)
print(result)  # Output: [2, 3]
