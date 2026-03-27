
g = {"a": ["b", "c"], "b": ["c"], "c": ["d"]}
root = "a"
max_depth = 3
k = g.keys()

def dls(limit):
    stack = [(root, 0)]
    visited = []

    while stack:
        curr, depth = stack.pop()

        if curr not in visited:
            visited.append(curr)

        if depth < limit and curr in k:
            for x in reversed(g[curr]):
                if x not in visited:
                    stack.append((x, depth + 1))

    return visited


# IDDFS
for depth in range(max_depth + 1):
    result = dls(depth)
    print(f"Depth {depth}:", result)
