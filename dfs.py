#DFS
g={"a":["b","d"],"b":["f","c"],"c":["g","e"],"d":["e"],"e":["b","f"],"f":["a"],"g":["e"]}
root="a"
q=[root]
a=[]
k=g.keys()
while(not(q==[])):
    curr=q.pop()
    if(curr not in a):
            a.append(curr)
    if curr in k:
        for x in g[curr]:
            if(x not in q and x not in a):
                q.append(x)
print("")
print(g)
print("dfs:",end='')
print(a)