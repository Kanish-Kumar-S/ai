import heapq

def tsp_astar(graph, start):
    n = len(graph)
    pq = [(0, start, [start])]

    while pq:
        cost, node, path = heapq.heappop(pq)

        if len(path) == n:
            return cost + graph[node][start], path + [start]

        for neigh, w in graph[node]:
            if neigh not in path:
                heapq.heappush(pq, (cost + w, neigh, path + [neigh]))


# Example graph (complete graph)
graph = {
    'A': [('B', 10), ('C', 15), ('D', 20)],
    'B': [('A', 10), ('C', 35), ('D', 25)],
    'C': [('A', 15), ('B', 35), ('D', 30)],
    'D': [('A', 20), ('B', 25), ('C', 30)]
}

cost, path = tsp_astar(graph, 'A')
print("TSP Path:", path)
print("Cost:", cost)