# Adjacency List

class Solution:
    def printGraph(self, V, edges):
        adjList = [[] for _ in range(V)]
        
        for edge in edges:
            u, v = edge
            adjList[u].append(v)
            adjList[v].append(u)
        
        return adjList

# Example usage:
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()

    # Define the number of vertices and edges for your graph
    V = 5
    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (0, 4)]

    # Call the printGraph method to get the adjacency list
    adjacency_list = solution.printGraph(V, edges)

    # Print the adjacency list
    for i, neighbors in enumerate(adjacency_list):
        print(f"Vertex {i}: {neighbors}")
