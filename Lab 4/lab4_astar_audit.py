#lab 4 aj sir naa Informed Search: Heuristics & A* kriwaa 
import math
 
# ---------- Graph for lab manual ----------
graph = {

    "S" :[("A", 1), ("B", 4)],
    "A":  [("C", 2)],
    "B" :[("G", 5)],
    "C":  [("G", 3)],
    "G" :[]
}
 
heuristic ={"S":  5, "A":4, "B":  4, "C":2, "G":  0 }
 
START      ,      GOAL        = "S", "G"
 
 
# ----------  Queue ka tarika la ga stack ka ni ----------

def push(queue, entry):
    queue.append(entry)
 
 
def pop_smallest(queue):
    entry = min(queue)
    queue.remove(entry)
    return entry
 
 
# ---------- Search: A* with the supplied h UCS when every h = 0 ----------

def search(start, goal, h):
    queue = [(h[start], 0, start, [start])]
    best = {start: 0}      
    trace = []             
    steps = []             
    expanded = []      
    stale = 0             
 
    while queue:
        f, g, node, path = pop_smallest(queue)
 
        if g != best[node]:  
            stale += 1
            continue
 
        trace.append(node)
        steps.append((node, g, h[node], f))
 
        if node == goal:
            return path, g, trace, steps, expanded, stale
 
        expanded.append(node)
 
        for next_node, edge_cost in graph[node]:
            new_g = g + edge_cost
            if new_g < best.get(next_node, math.inf):
                best[next_node] = new_g
                push(  queue,    (new_g +h[next_node],   new_g,next_node,   path +[next_node]))
 
    return [], math.inf, trace, steps, expanded, stale
 
 
def sum_path(path):

    total = 0
    for i in   range(len  (path) -1):
        total =total+ next(c for n, c in graph[path[i]] if n == path[i + 1])
    return total
 
 
def show_result(title, h):
    path, cost, trace, steps, expanded, stale = search(START, GOAL, h)
    print("\n"  +title)
    print ("Path:", " ->".join(path) )
    print("Returned cost:", cost)
    print("Independently summed cost:", sum_path(path))
    print("Processed-node trace:", trace)
    for node, g, hn, f in steps:
        print(f"   {node}: g={g}, h={hn}, f={f}")
    print("Expanded nodes:", expanded)
    print("Expansion count:", len(expanded))
    print("Stale entries skipped:", stale)
    return path, cost, expanded
 
 
# ---------- True remaining cost of every node (UCS from that node to G) ----------
zero_h = {node: 0 for node in graph}
true_remaining = {}
for node in graph:
    _, c, _, _, _, _ = search(node, GOAL, zero_h)
    true_remaining[node] = c
 
 
# ---------- Task 1 check: frontier table for the first three expansions ----------
def show_frontier(queue):
    items = sorted(queue)
    return ",  ".join(f"{n}({g},{heuristic[n]},{f})" for f, g, n, _ in items) or "empty"
 
 
def task1_check():
    print("=== Task 1 check: first three expansions (compare with the hand calculation) ===")
    print("Tie-break: lowest f then lowest g then node name")
    queue = [(heuristic[START], 0, START, [START])]
    best = {START: 0}
    for step in range (1,   4) :
        print( f" \n Expansion     {  step}")
        print("   Frontier before:", show_frontier(queue))
        f, g, node, path = pop_smallest(queue)
        print(f"   Selected {node}: g={g}, h={heuristic[node]}, f={g}+{heuristic[node]}={f}")
        print("   Remaining after removing it:", show_frontier(queue))
        for next_node, cost in graph[node]:
            new_g = g + cost
            new_f = new_g + heuristic[next_node]
            print (f"   Successor{next_node}:      g={g}+  {cost}={new_g},f= {new_g}+  {heuristic[next_node]}  ={new_f}")
            if new_g < best.get(next_node, math.inf):
                best[next_node] = new_g
                push(queue, (new_f, new_g, next_node, path + [next_node]))
        print("   Frontier now:", show_frontier(queue))
        ordered = sorted(queue)
        if  len(ordered )   >1  :
            print(f"Next node:     {ordered[0][2]}    (f={ordered[0][0]})   because it is lower than {ordered[1][2]} (f={ordered[1][0]})")
        else:
            print(f"       Next node: {ordered[0]     [2]}     ")
 
 
# ---------- Heuristic value----------
def audit():
    print("=== Heuristic audit ===")
    print("True remaining cost:", true_remaining)
    print("Admissible? h(n) <= true remaining cost")
    for n in heuristic:
        print(f"  {n}: {heuristic[n]      }        <= {true_remaining[n]} ->     {heuristic[n] <= true_remaining[n]}")
    print("Consistent?      h(u) <=cost(u,v)    + h(v)")
    for u in graph:
        for v, c in graph[u]:
            print(f"  {u}->{v}:   {heuristic[u]} <=   {c} +{heuristic[v]} ={c +   heuristic[v]} ->{heuristic[u]   <= c + heuristic[v]}")
  
 
# ----------   Task 2: is task maa A* aur UCS dekha gaa  ----------
def task2():
    print("  \n=== Task 2:   A* vs UCS    (same graph, same start and goal)   ===")
    show_result("A* with the supplied heuristic", heuristic)
    show_result("UCS control (all h = 0)", zero_h)
    print("\nNote:     the goal is processed but nevercounted as expanded in both runs.  ")
 
 
# ---------- Task 3: is task ma overestimate ----------
def task3():
    print("=== Task 3: Overestimate task ho gaa ===")
    node, new_value = "C", 10
    modified = heuristic.copy()
    modified[node] = new_value
 
    changed = [n for n in heuristic if heuristic[n] != modified[n]]
    print("Values changed:", changed, "(only one)")
    print (f"Original   h({node})            = {heuristic[node]}, modified h({node}) ={  modified[node]}")
    print(f"      True remaining cost of {node}=       {true_remaining     [node]     }"      )
    print (f"Overestimate by        {modified[node] -       true_remaining[node]} -> still admissible ?       {modified[node]<= true_remaining     [node]}")
 
    p0, c0, e0 = show_result("A* with original h(C) = 2", heuristic)
    p1, c1, e1 = show_result("A* with modified h(C) = 10", modified)
 
    print("\nComparison (original -> modified)")
    print("   path changed? ", p0 != p1, " ", p0, "->", p1)
    print("         cost changed?        ",c0      != c1,      " ",c0, "->",     c1)
    print("      count changed?     "    , len(e0) != len(e1)," ",      len(e0), "->", len(e1), "nodes:",      e0, "->", e1)
 
    
    mild = heuristic.copy()
    mild["C"] = 4
    p2, c2, e2 = show_result("Extra test: mild overestimate h(C) = 4 (true remaining = 3)", mild)
    print("\nh(C) = 4 changes the answer?", p2 != p0, "-> one unchanged run does not prove a heuristic is safe")
 
 
# ---------- Run ----------
RUN = "all"     

if RUN in ("all", "task1"):
    task1_check()
    if RUN == "all":
        print()
if RUN in ("all", "task2"):
    audit()
    task2()
if RUN in ("all", "task3"):
    if RUN == "all":
        print()
    task3()