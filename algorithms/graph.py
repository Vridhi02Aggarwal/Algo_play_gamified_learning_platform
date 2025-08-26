# graph_dfs.py
from collections import deque
import heapq

def dfs_build_steps(graph, start):
    visited = set()
    steps = []
    explanations = []

    def dfs(node):
        if node not in visited:
            visited.add(node)
            steps.append(node)
            explanations.append(f"Visited {node}")
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    explanations.append(f"From {node} → going to {neighbor}")
                    dfs(neighbor)

    dfs(start)
    return steps, explanations

# graph_bfs.py


def bfs_build_steps(graph, start):
    visited = set()
    queue = deque([start])
    steps = []
    explanations = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            steps.append(node)
            explanations.append(f"Visited {node}")

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    explanations.append(f"From {node} → enqueue {neighbor}")
                    queue.append(neighbor)

    return steps, explanations

# graph_dijkstra.py



def dijkstra_build_steps(graph, start):
    # graph format: { 'A': {'B': 4, 'C': 2}, ... }
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]  # (distance, node)
    
    steps = []
    explanations = []

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > distances[current_node]:
            continue

        steps.append(current_node)
        explanations.append(f"Visiting {current_node}, current distance = {current_dist}")

        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                explanations.append(
                    f"Updating distance of {neighbor}: {distances[neighbor]} → {distance} via {current_node}"
                )
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return steps, explanations, distances


# graph_kruskal.py

def kruskal_build_steps(edges, n):
    """
    Kruskal's Algorithm (Minimum Spanning Tree)
    edges: list of (weight, u, v)
    n: number of vertices
    """
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX, rootY = find(x), find(y)
        if rootX != rootY:
            if rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            elif rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
            return True
        return False

    steps = []
    explanations = []
    mst_edges = []

    edges.sort()  # sort by weight

    for w, u, v in edges:
        if union(u, v):
            mst_edges.append((u, v, w))
            steps.append(list(mst_edges))  # snapshot of current MST edges
            explanations.append(f"Added edge ({u}, {v}) with weight {w}")
        else:
            explanations.append(f"Skipped edge ({u}, {v}) with weight {w} (cycle detected)")

    return steps, explanations

