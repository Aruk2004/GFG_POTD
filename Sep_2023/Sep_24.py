class Solution:
    def duplicates(self, arr, n):
        cnt = [0] * n
        
        for i in range(n):
            cnt[arr[i]] += 1

        out = []
        for i in range(n):
            if cnt[i] > 1:
                out.append(i)

        if out:
            return out

        return [-1]

# Example usage:
arr = [1, 3, 3, 2, 2, 5, 5]
n = len(arr)
sol = Solution()
result = sol.duplicates(arr)
print(result)  # Output: [2, 3, 5]
