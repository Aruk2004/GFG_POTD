# Find the String

class Solution:
    def findString(self, n, k):
        vis = set()

        start = "0" * n
        ans = start

        def dfs(node):
            nonlocal ans
            vis.add(node)
            next_s = node[1:]

            for i in range(k - 1, -1, -1):
                child = next_s + str(i)

                if child not in vis:
                    ans += str(i)
                    dfs(child)

        dfs(start)

        return ans

# Example usage:
solution = Solution()
n_value = 3
k_value = 2
result_string = solution.findString(n_value, k_value)
print(result_string)
