#Given a Directed Graph, Find a Mother Vertex in the Graph

class Solution:
    def dfs(self, i, adj, vis, topo):
        vis[i] = 1
        for edge in adj[i]:
            if not vis[edge]:
                self.dfs(edge, adj, vis, topo)
        topo.append(i)
    
    def findMotherVertex(self, V, adj):
        vis = [0] * V
        topo = []
        for i in range(V):
            if not vis[i]:
                self.dfs(i, adj, vis, topo)
        
        if len(topo) == V:
            mother_vertex = topo[-1]
            vis = [0] * V
            topo = []
            self.dfs(mother_vertex, adj, vis, topo)
            if len(topo) == V:
                return mother_vertex
        
        return -1

# Example usage:
if __name__ == "__main__":
    V = 7
    adj = [[] for _ in range(V)]

    adj[0].append(1)
    adj[0].append(2)
    adj[1].append(3)
    adj[4].append(1)
    adj[6].append(4)
    adj[5].append(6)
    adj[5].append(2)
    adj[6].append(0)

    solver = Solution()
    mother_vertex = solver.findMotherVertex(V, adj)

    if mother_vertex != -1:
        print(f"The mother vertex is {mother_vertex}")
    else:
        print("There is no mother vertex in the graph")
