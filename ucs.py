import heapq

def ucs(graph, start, goal):
    pq = [(0, start)]
    visited = set()
    parent = {start: None}
    cost_so_far = {start: 0}

    while pq:
        cost, node = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            # reconstruct path
            path = []
            curr = goal
            while curr is not None:
                path.append(curr)
                curr = parent[curr]
            path.reverse()
            return cost, path

        for neigh, w in graph.get(node, []):
            new_cost = cost + w

            if neigh not in cost_so_far or new_cost < cost_so_far[neigh]:
                cost_so_far[neigh] = new_cost
                parent[neigh] = node
                heapq.heappush(pq, (new_cost, neigh))

    return None
g = { "a": [("b", 1), ("c", 4)], "b": [("c", 2), ("d", 5)], "c": [("d", 1)], "d": [] }
ucs(g,"a","d")