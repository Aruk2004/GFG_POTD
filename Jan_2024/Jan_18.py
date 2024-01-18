# Water the plants

class Solution:
    def min_sprinklers(self, gallery, n):
        
        range_ = [-1] * n

        for i in range(n):
            l = max(0, i - gallery[i])
            r = min(n - 1, i + gallery[i])
            for j in range(l, r + 1):
                range_[j] = max(range_[j], r)

        count = 0
        last = -1

        for i in range(n):
            if range_[i] == -1:
                return -1

            if i > last:
                count += 1
                last = range_[i]

        return count

# Example usage:

sol = Solution()
gallery_array = [3, 1, 2, 0, 4, 2, 1, 0, 1]
n = len(gallery_array)
result = sol.min_sprinklers(gallery_array, n)

print(result)
