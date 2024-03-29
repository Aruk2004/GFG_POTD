# Euler Circuit in an Undirected Graph

class Solution:
	def isEularCircuitExist(self, v, adj):
		return all(len(v_adj) % 2 == 0 for v_adj in adj)

solution = Solution()

# Example 1: Graph with an Eulerian circuit
v1 = 4
adj1 = [
    [1, 2],
    [0, 2],
    [0, 1, 3],
    [2]
]
result1 = solution.isEularCircuitExist(v1, adj1)
print("Example 1 - Eulerian circuit exists:", result1)

# Example 2: Graph without an Eulerian circuit
v2 = 4
adj2 = [
    [1, 2],
    [0, 2],
    [0, 1],
    [3]
]
result2 = solution.isEularCircuitExist(v2, adj2)
print("Example 2 - Eulerian circuit exists:", result2)
