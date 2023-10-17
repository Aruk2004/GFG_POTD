# Transitive closure of a Graph

class Solution:
    def transitiveClosure(self, N, graph):
        transitive = [[0 for _ in range(N)] for _ in range(N)]

        for i in range(N):
            for j in range(N):
                transitive[i][j] = graph[i][j]
                if i == j:
                    transitive[i][j] = 1

        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if transitive[i][k] and transitive[k][j]:
                        transitive[i][j] = 1

        return transitive

# Example usage:
solution = Solution()
N = 4
graph = [[1, 1, 0, 1],
         [0, 1, 1, 0],
         [0, 0, 1, 1],
         [0, 0, 0, 1]]
result = solution.transitiveClosure(N, graph)
for row in result:
    print(row)
