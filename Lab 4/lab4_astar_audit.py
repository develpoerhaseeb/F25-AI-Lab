#lab 4 lab task
import math
graph ={
    "S":[("A", 1),("B", 4)] ,
    "A":[("C", 2)] ,
    "B":[("G", 5)] ,
    "C":[("G", 3)] ,
    "G":[]
}
heuristic={"S":5, "A":4, "B":4, "C":2, "G":0}
START,GOAL="S","G"
#------------------QUEUE---------------
def push (queue, entry):
    queue.append (entry)
def pop_samllest (queue):
    entry=min (queue)
    queue.remove (entry)
    return entry
#-------------A* / UCS ------------
def search(start, goal, h):
    queue=[(h[start], 0, start, [start])]
    best={start: 0}
    trace=[]
    steps=[]
    expanded=[]
    stale= 0

    while queue:
        f, g, node, path=pop_samllest(queue)
        if g !=best [node]:
            stale = stale+1
            continue
        trace.append (node)
        steps.append( (node, g, h [node], f))
        if node== goal:
            return path, g, trace, steps, expanded, stale
        expanded.append (node)
        for next_node, edge_cost in graph [node]:
            new_g= g+edge_cost
            if new_g <best.get (next_node, math.inf):
                best[next_node]= new_g
                push(queue, (new_g+h[next_node], new_g, next_node, path+[next_node]))
    return [], math.inf, trace, steps, expanded, stale
def sum_path (path):
    total=0  
    for i in range ( len(path)- 1):
        total +=next (c for n, c in graph [path [i] ] if n == path [i+1])
    return total
def show_result(title, h):
    path, cost, trace, steps, expanded, stale=search(START, GOAL, h)
    print("\n" + title)
    print("Path:"+"------".join (path))
    print("Cost:", cost)
    print("Independent sum cost:", sum_path (path))
    print("Process node:", trace)
    for node, g, hn, f in steps:
        print(f" {node}:g= {g}h= {hn}g= {f}")
    print("Expanded nodes:", expanded)
    print("Expansion Count:", len(expanded))
    print("Stale entries skip:", stale)
    return path, cost, expanded

#-----------Remaining Cost-----------
zero_h={node: 0 for node in graph}
true_remaining={}
for node in graph:
    _,c,_,_,_,_= search(node, GOAL, zero_h)
    true_remaining [node]= c

#----------Task 1 check ---------------
def show_frontier (queue):
    items= sorted (queue)
    return " ".join(f"{n} ({g}, {heuristic [n]}, {f})" for f, g, n,_ in items) or "empty"
def task1_check():
    print("-----------Task 1 check------------")
    print("Tie Break: Low f then low g then node name")
    queue=[(heuristic[START], 0, START, [START])]
    best={START: 0}
    for step in range(1,4):
        print(f"\nExpansion {step}")
        print("Frontier before:", show_frontier(queue))
        f,g,node,path=pop_samllest(queue)
        print(f" Selected {node}:g= {g}, h={heuristic[node]}, f={g}+{heuristic[node]} ={f}")
        print("Remaining after remove:", show_frontier(queue))

        for next_node,cost in graph[node]:
            new_g=g+cost
            new_f=new_g+heuristic[next_node]
            print(f" Successor{next_node}:g={g} +{cost} ={new_g}, f={new_g} +{heuristic [next_node] }={new_f}")
            if new_g < best.get(next_node, math.inf):
                best[next_node]= new_g
                push(queue, (new_f, new_g, next_node, path + [next_node]))
        print("Frontier:", show_frontier(queue))
        ordered=sorted(queue)
        if len(ordered) >  1:
            print(f" Next Node: {ordered [0] [2]} (f= {ordered[0] [0]}) bcz it is lower than {ordered [1] [2]} (f={ordered[1 ] [0]})")
        elif ordered:
            print(f" Next node: {ordered[0][2]}")

#---------------------Task 2: A* / UCS ------------------
def task2():
    print("\n-----------Task 2: A* / UCS -----------")
    show_result("A* with supply heuristic",heuristic)
    show_result("UCS cntrol (all h=0)",zero_h)
    print("\nNote:Gaol process but never count")

#-------------Task 3: Overestimate test level -----------------
def task3():
    print("------------Task 3: Overestimate level task ------------")
    node,new_value="C", 10
    modified= heuristic.copy()
    modified [node]= new_value
    changed = [n for n in heuristic if heuristic [n] != modified [n]]
    print("Value Change:",changed,"(only one)")
    print(f" h({node}) ={heuristic[node]}, modified h({node})= {modified[node]}")
    print(f" Remainging cost{node} ={true_remaining [node]}")
    print(f" Overestimate by {modified} [node]-{true_remaining [node]}")

    p0,c0,e0=show_result( "A* with h(C)=2", heuristic)
    p1,c1,e1=show_result( "A* with modified", modified)
    
    print("\nComparison modify")
    print("Path change", p0 !=p1, f"({p0} -- {p1})")
    print("Cost change", c0 !=c1, f"({c0} -- {c1})")
    print("Count Change", len(e0)!= len(e1), f"( {len(e0)} -----  {len (e1)}, node: {e0} ------- {e1} )")
    mild=heuristic.copy()
    mild["C"]= 4
    p2, c2, e2 = show_result("Extra  test: Mild overestimate = 4",mild)
    print ("\nh(c)=4 change answer?", p2 !=p0, "----- one run does not heuristic is safe")

#------------- Run ---------------
RUN="all"

if RUN in ("all","task1"):
    task1_check()
if RUN =="all":
    print()
if RUN in ("all","task2"):
    
    task2()
if RUN in ("all","task3"):
    if RUN == "all":
        print()
    task3()