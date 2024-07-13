# Shortest Path in Weighted undirected graph

import heapq
from collections import defaultdict
import sys
from typing import List

class Solution:
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0, 1]  # Single node graph, path from node 1 to itself

        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        # Dijkstra's Algorithm
        distances = {i: sys.maxsize for i in range(1, n + 1)}
        distances[1] = 0
        priority_queue = [(0, 1)]  # (distance, node)
        parent = {1: None}

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    parent[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

        if distances[n] == sys.maxsize:
            return [-1]

        # Reconstruct path from 1 to n
        path = []
        current = n
        while current is not None:
            path.append(current)
            current = parent[current]
        path.reverse()

        return [distances[n]] + path
