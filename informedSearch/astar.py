import heapq

def astar(graph, start, goal, heuristic):
    pq = [(0, start)]
    parent = {start: None}
    g_cost = {start: 0}

    while pq:
        _, node = heapq.heappop(pq)

        if node == goal:
            path = []
            while node:
                path.append(node)
                node = parent[node]
            return path[::-1], g_cost[goal]

        for neigh, w in graph[node]:
            new_cost = g_cost[node] + w

            if neigh not in g_cost or new_cost < g_cost[neigh]:
                g_cost[neigh] = new_cost
                f_cost = new_cost + heuristic[neigh]
                parent[neigh] = node
                heapq.heappush(pq, (f_cost, neigh))


# Example graph
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}

heuristic = {
    'A': 5, 'B': 3, 'C': 4,
    'D': 2, 'E': 1, 'F': 0
}

path, cost = astar(graph, 'A', 'F', heuristic)
print("A* Path:", path)
print("Cost:", cost)