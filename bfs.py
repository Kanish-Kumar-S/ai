g={"a":["b","d"],"b":["f","c"],"c":["g","e"],"d":["e"],"e":["b","f"],"f":["a"],"g":["e"]}
root="a"
q=[root]
a=[]
while(not(q==[])):
    curr=q[0]
    del q[0]
    if(curr not in a):
        a.append(curr)
    for x in g[curr]:
        if(x not in q and x not in a):
            q.append(x)
print("bfs:")
print(a)