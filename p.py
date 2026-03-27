import heapq
g={"a":[("b",1),("c",4)],"b":[("c",2),("d",1)]}
k=g.keys()
goal="d"
root="a"
pq=[(0,root,[])]
a=[]
while(not(pq==[])):
    cost,curr,path=heapq.heappop(pq)
    if curr==goal:
        print(path+[curr])
        print(cost)
        break
    if((cost,curr,path) not in a):
        a.append((cost,curr,path))
    if curr in g.keys():
        for x in g[curr]:
            n,c=x
            if((c+cost,n,path+[curr]) not in pq and (c+cost,n,path+[curr]) not in a):
                heapq.heappush(pq,(c+cost,n,path+[curr]))
