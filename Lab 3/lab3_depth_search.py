# Lab 3 Task 3 - UCS on the weighted graph

import heapq
from collections import deque
 
graph={
       "A":[("B",1),("C",5)],
       "B":[("D",2),("E",1)],
       "C":[("F",2),("G",7)],
       "D":[],
       "E":[("G",1)],
       "F":[],
       "G":[],
       }
 
def ucs(start, goal, g=graph):
    pq=[(0,start,[start])]; seen=set(); order=[]
    while pq:
        cost,node,path=heapq.heappop(pq)   
        if node in seen: continue
        seen.add(node)
        order.append((node,cost))
        if node==goal: return path,cost,order
        for n,w in g[node]:
            if n not in seen:
                heapq.heappush(pq,(cost+w,n,path+[n]))
    return None,None,order
 
def bfs(start, goal, g=graph):
    q=deque([(start,[start])]); seen={start}; order=[]
    while q:
        node,path=q.popleft()
        order.append(node)
        if node==goal: return path,order
        for n,w in g[node]:
            if n not in seen:
                seen.add(n); q.append((n,path+[n]))
    return None,order
 
def path_cost(path, g=graph):
    total=0
    for i in range(len(path)-1):
        for n,w in g[path[i]]:
            if n==path[i+1]: total+=w
    return total
 
if __name__=="__main__":
    print("----------Edge weights---------")
    for a in graph:
        for b,w in graph[a]:
            print(f"  {a}->{b} = {w}")
 
    p,c,order=ucs("A","G")
    print("\nUCS path:",'->'.join(p)," ---- return cost:",c)
    print("UCS process order:",order)
    print("UCS edge:",path_cost(p)," -----  hops:",len(p)-1)
    print("Manual sum:", " + ".join(str(dict(graph[a])[b]) for a,b in zip(p,p[1:])), "=", path_cost(p))
    print("Retur cost sum:", c==path_cost(p))
 
    bp,bo=bfs("A","G")
    print("\nBFS path:",'->'.join(bp),"| hops:",len(bp)-1,"| cost:",path_cost(bp))
    print("BFS visit order:",bo)
 
    print("\n-------- Edge cases ---------")
    print("start == goal :",ucs("A","A"))
    print("unreachable Z :",ucs("A","Z",{**graph,"Z":[]})[:2])
    cyc={"A":[("B",1)],"B":[("C",1)],"C":[("A",1),("D",4)],"D":[]}
    print("cycle graph   :",ucs("A","D",cyc))
