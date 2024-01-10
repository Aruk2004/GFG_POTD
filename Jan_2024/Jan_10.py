# Longest subarray with sum divisible by K

class Solution:
    def longSubarrWthSumDivByK(self, arr, k):
        mp = {0: -1}
        out, _sum = 0, 0

        for i in range(len(arr)):
            _sum += arr[i]
            rem = _sum % k

            if rem < 0:
                rem += k

            if rem in mp:
                out = max(out, i - mp[rem])
            else:
                mp[rem] = i

        return out

# Example usage:
# Create an instance of the Solution class
sol = Solution()

# Call the longSubarrWthSumDivByK function with specific values of arr and k
arr = [4, 5, 0, -2, -3, 1]
k = 5
result = sol.longSubarrWthSumDivByK(arr, k)

# Print the result
print(result)
