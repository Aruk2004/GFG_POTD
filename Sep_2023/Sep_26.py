class Solution:
    def fourSum(self, arr, k):
        n = len(arr)
        out = []
        
        arr.sort()

        for q1 in range(n):
            if q1 > 0 and arr[q1] == arr[q1 - 1]:
                continue

            for q2 in range(q1 + 1, n):
                if q2 > q1 + 1 and arr[q2] == arr[q2 - 1]:
                    continue

                q3 = q2 + 1
                q4 = n - 1

                while q3 < q4:
                    _sum = arr[q1] + arr[q2] + arr[q3] + arr[q4]

                    if _sum == k:
                        out.append([arr[q1], arr[q2], arr[q3], arr[q4]])
                        q3 += 1
                        q4 -= 1

                        while q3 < q4 and arr[q3] == arr[q3 - 1]:
                            q3 += 1
                        while q3 < q4 and arr[q4] == arr[q4 + 1]:
                            q4 -= 1
                    elif _sum < k:
                        q3 += 1
                    else:
                        q4 -= 1

        return out

# Example usage:
arr = [1, 0, -1, 0, -2, 2]
k = 0
sol = Solution()
result = sol.fourSum(arr, k)
print(result)  # Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
