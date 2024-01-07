# Split Array Largest Sum

class Solution:
    def solve(self, arr, N, K, mid):
        _sum = 0
        for i in range(N):
            if arr[i] > mid:
                return False
            _sum += arr[i]
            if _sum > mid:
                K -= 1
                _sum = arr[i]
        
        return K >= 1

    def splitArray(self, arr, N, K):
        _sum = sum(arr)
        low, high = 0, _sum
        ans = _sum

        while low <= high:
            mid = (low + high) // 2
            if self.solve(arr, N, K, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

# Example usage:
sol = Solution()
result = sol.splitArray([1, 2, 3, 4, 5], 5, 2)  
print(result)
