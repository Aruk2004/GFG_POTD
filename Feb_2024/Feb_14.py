# Find all Critical Connections in the Graph

# Define the Solution class
class Solution:
    def __init__(self):
        self.timer = 0
        self.ans = []
        self.vis = []
        self.dis = []
        self.low = []

    def dfs(self, node, parent, adj):
        self.timer += 1
        self.vis[node] = 1
        self.dis[node] = self.low[node] = self.timer
        for it in adj[node]:
            if it == parent:
                continue
            elif not self.vis[it]:
                self.dfs(it, node, adj)

            self.low[node] = min(self.low[node], self.low[it])
            if self.low[it] > self.dis[node]:
                self.ans.append([min(it, node), max(it, node)])

    def criticalConnections(self, v, adj):
        self.vis = [0] * v
        self.dis = [-1] * v
        self.low = [-1] * v
        for i in range(v):
            if self.vis[i] == 0:
                self.dfs(i, -1, adj)
        self.ans.sort()
        return self.ans

# Example usage
if __name__ == "__main__":
    # Create an instance of the Solution class
    sol = Solution()

    # Define the number of vertices and adjacency list
    v = 5
    adj = [[1], [0, 2], [1, 3, 4], [2], [2]]

    # Find critical connections in the network
    critical_connections = sol.criticalConnections(v, adj)

    # Print the critical connections
    print("Critical Connections:")
    for connection in critical_connections:
        print(connection)
