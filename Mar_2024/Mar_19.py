# Possible Paths in a Tree

class Solution:
    def maximumWeight(self, n, edges, q, queries):

        par = [i for i in range(n)]
        rank = [1 for _ in range(n)]

        def find(n1):
            while (par[n1] != n1):
                par[n1] = par[par[n1]]
                n1 = par[n1]
            return par[n1]
        
        edges.sort(key=lambda x: x[2], reverse=True)
        queries = sorted(enumerate(queries), key=lambda x: x[1])

        res = [0]*q
        cur = 0
        for idx, x in queries:
            while edges and edges[-1][2] <= x:
                u, v, wt = edges.pop()
                u, v = find(u-1), find(v-1)
                if u != v:
                    par[v] = u 
                    cur += rank[u] * rank[v]
                    rank[u] += rank[v]
            res[idx] = cur

        return res

# Example usage
n = 7
edges = [[1, 2, 3], [2, 3, 1], [2, 4, 9], [3, 6, 7], [3, 5, 8], [5, 7, 4]]
q = 3
queries = [1, 3, 5]

solution = Solution()
result = solution.maximumWeight(n, edges, q, queries)
print("Maximum weights:", result)
