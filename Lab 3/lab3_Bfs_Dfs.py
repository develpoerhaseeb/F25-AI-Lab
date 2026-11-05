# Lab 3 Task 1 - BFS and DFS

from collections import deque
graph ={
    "A":["B","C"],
    "B":["D","E"],
    "C":["F"],
    "D":[],
    "E":["G"],
    "F":[],
    "G":[]
}
def bfs(start,gaol):
    q= deque([(start,[start])]); seen= {start}
    while q:
        node,path = q.popleft()
        if node==gaol: return path
        for n in graph[node]:
            if n not in seen:
                seen.add(n); q.append((n,path+[n]))
def dfs(start, goal):
    stack = [(start,[start])]; seen = set()
    while stack:
        node, path= stack.pop()
        if node ==goal: return path
        if node in seen: continue
        seen.add(node)
        for n in reversed(graph[node]): stack.append((n,path+[n]))
def bfs_trace(start,goal):
    q = deque([(start,[start])]); seen = {start}
    order = []; step = 0
    print("------------------BFS trace-----------------")
    while q:
        node, path= q.popleft()
        step+= 1
        order.append(node)
        print("Step",step,": processed",node,"path =","->".join(path))
        if node==goal:
            print("goal reached, queue left:",[x[0] for x in q])
            return path, order
        for n in graph[node]:
            if n not in seen:
                seen.add(n); q.append((n,path+[n]))
        print("queue now:",[x[0] for x in q])
def dfs_trace(start,goal):
    stack = [(start,[start])]; seen = set()
    order = []; step =0
    print("----------DFS trace------------")
    while stack:
        node,path = stack.pop()
        step+=1
        if node==goal:
            order.append(node)
            print("Step",step,": processed",node,"path =","->".join(path))
            print("goal reached, stack left:",[x[0] for x in stack])
            return path, order
        if node in seen:
            print("step",step,":",node,"already processed, skipped")
            continue
        seen.add(node)
        order.append(node)
        print("Step",step,": processed", node,"path =","->".join(path))
        for n in reversed(graph [node] ):stack.append ((n, path+[n]))
        print("stack now:" ,[x [0] for x in stack])
if __name__  == "__main__" :
    print("--------Code output---------")
    print(bfs("A","G"))
    print(dfs("A","G"))
    print()
    bp,bo = bfs_trace("A","G")
    print("BFS final path:",bp)
    print("BFS visit path:",bo)
    print()
    dp,do=dfs_trace("A","G")
    print("DFS final path:",dp)
    print("DFS visit path:",do)
    print()
    print("BFS trace:",bp==bfs("A","G"))
    print("DFS trace:",dp==dfs("A","G"))
    print("BFS order:",bo==["A","B","C","D","E","F","G"])
    print("DFS order:",bo==["A","B","D","E","G"])
