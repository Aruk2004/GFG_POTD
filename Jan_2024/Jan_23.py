# Course Schedule

from collections import deque

class Solution:
    def findOrder(self, n, m, pre):
        graph = [[] for _ in range(n)]
        degree = [0] * n

        for i in pre:
            degree[i[0]] += 1
            graph[i[1]].append(i[0])

        q = deque()
        for i in range(n):
            if degree[i] == 0:
                q.append(i)

        ans = []
        while q:
            front = q.popleft()
            ans.append(front)
            for i in graph[front]:
                degree[i] -= 1
                if degree[i] == 0:
                    q.append(i)

        if any(i >= 1 for i in degree):
            return []

        return ans

# Example usage:
solution = Solution()
n = 4
m = 3
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
result = solution.findOrder(n, m, prerequisites)

# Print the result
print(result)
