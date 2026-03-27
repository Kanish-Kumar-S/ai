import heapq

def greedy_bfs(graph, start, goal, heuristic):
    pq = [(heuristic[start], start)]
    visited = set()
    parent = {start: None}

    while pq:
        _, node = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            path = []
            while node:
                path.append(node)
                node = parent[node]
            return path[::-1]

        for neigh in graph[node]:
            if neigh not in visited:
                parent[neigh] = node
                heapq.heappush(pq, (heuristic[neigh], neigh))


# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

heuristic = {
    'A': 5, 'B': 3, 'C': 4,
    'D': 6, 'E': 2, 'F': 0
}

print("Greedy BFS Path:", greedy_bfs(graph, 'A', 'F', heuristic))