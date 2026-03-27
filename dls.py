#DLS
g = {"a": ["b", "c"], "b": ["c"], "c": ["d"]}
root = "a"
limit = 2   

stack = [(root, 0)]   
visited = []
k = g.keys()

while stack:
    curr, depth = stack.pop()

    if curr not in visited:
        visited.append(curr)

    if depth < limit and curr in k:
        for x in reversed(g[curr]): 
            if x not in visited:
                stack.append((x, depth + 1))

print("graph:", g)
print("depth limited dfs:", visited)
