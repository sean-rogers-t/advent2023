# seems similiar to Day17
import numpy as np
import heapq
import graphviz

def dfsMakeDAG(junctions,beginning,grid, DAG, start,finish,direction = None):
    visited = set()
    if beginning == finish:
        return
    currentNode = beginning
    if direction:
        (dr,dc) =  direction
        stack = [(beginning[0]+2*dr,beginning[1]+2*dc)]
        visited.add((beginning[0]+2*dr,beginning[1]+2*dc))
        distance=2
    else:
        stack = [start]
        visited.add(start)
        distance=0
    
    while stack:
        node = stack.pop()
        if node in junctions and  node != beginning:
            if [node,distance] in DAG[currentNode]["outgoing"] or [currentNode,distance] in DAG[node]["incoming"]:
                continue
            DAG[node]["incoming"].append([currentNode,distance])
            DAG[currentNode]["outgoing"].append([node,distance])
            if node == finish:
                return dfsMakeDAG(junctions,node,grid,DAG,start,finish)
            
            stack=[]
            visited=set()
            distance=0
            for dr,dc in directions:
                r,c = node[0]+dr,node[1]+dc
                if 0<r<len(grid) and  0<c<len(grid[0]) and grid[r][c] in arrows and badDirection[grid[r][c]] !=(dr,dc):  
                    dfsMakeDAG(junctions,node,grid,DAG,start,finish,(dr,dc))
        else:
            for dr,dc in directions:
                r,c = node[0]+dr,node[1]+dc
                if (r,c) not in visited and grid[r][c] != "#" and (grid[r][c] == "." or badDirection[grid[r][c]] !=(dr,dc)):  
                    visited.add((r,c))
                    stack.append((r,c))
                    distance+=1

def dfsLongestPath(graph,start,finish):
    maxLength=0
    numPaths=0
    visited = set()
    stack =[((start,0),0,set([start]))]

    while stack:
        node, length, path = stack.pop()
        if node[0]==finish:
            maxLength = max(maxLength,length)
            numPaths+=1
            continue
        for neighbor in graph[node[0]]:
            if neighbor[0] not in path:
                new_visited = path.copy()
                new_visited.add(neighbor[0])
                stack.append((neighbor,length+neighbor[1],new_visited))

    
    return maxLength, numPaths

    

# find longest path
def topologicalSort(DAG):
    # List to store the topological order
    top_order = []

    # Dictionary to keep track of the number of incoming edges for each node
    incoming_edges_count = {node: len(DAG[node]["incoming"]) for node in DAG}

    # Initialize a queue with nodes having no incoming edges
    queue = [node for node, count in incoming_edges_count.items() if count == 0]
    queue = [[node,0] for node in queue]
    while queue:
        # Take one node with no incoming edges
        node = queue.pop(0)
        
        top_order.append(node[0])

        # Decrease the count of incoming edges for all neighbors
        for neighbor in DAG[node[0]]["outgoing"]:
            incoming_edges_count[neighbor[0]] -= 1
            # If a neighbor has no more incoming edges, add it to the queue
            if incoming_edges_count[neighbor[0]] == 0:
                queue.append(neighbor)

    # Check for a cycle (if there are nodes with incoming edges left)
    if len(top_order) != len(DAG):
        raise Exception("DAG has at least one cycle")

    return top_order
def longestPathDAG(DAG, source, sink):
    top_order = topologicalSort(DAG)
    distance = {node: -float("inf") for node in DAG}

    distance[source] = 0

    for vertex in top_order:
        for neighbor in DAG[vertex]["outgoing"]:
            edge_weight = neighbor[1]
            new_dist=distance[vertex] + edge_weight
            if distance[neighbor[0]] < new_dist:
                distance[neighbor[0]] = new_dist

    return distance[sink]

with open("day23input.txt") as f:
    grid =  [line.strip() for line in f.readlines()]
start = (0,grid[0].index('.'))
finish = (len(grid)-1,grid[-1].index('.'))


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
arrows =[">","v","<","^"]
badDirection = {"^":(1,0),">":(0,-1),"v":(-1,0),"<":(0,1)}
junctions=[start]
numrows = len(grid)
numCols = len(grid[0])
for line in range(1,numrows-1):
    for spot in range(1,numCols-1):
        if grid[line][spot] ==".":
            count = len([grid[r][c] for r in range(line-1,line+2) for c in range(spot-1,spot+2) if grid[r][c] in arrows])
            if count>2:
                junctions.append((line,spot))

junctions.append(finish)

DAG = {node:{"incoming":[],"outgoing":[]} for node in junctions}

dfsMakeDAG(junctions,start,grid,DAG, start, finish)



dist = longestPathDAG(DAG,start,finish)
top_order = topologicalSort(DAG)

dot = graphviz.Digraph(comment='Garden')
dot  #doctest: +ELLIPSIS
for i, junction in enumerate(top_order):
    dot.node(str(i),str(junction)) # doctest: +NO_EXE
for node in DAG:
    for neighbor in DAG[node]["outgoing"]:
        dot.edge(str(top_order.index(node)),str(top_order.index(neighbor[0])),label=str(neighbor[1]))
print(dot.source) # doctest: +NORMALIZE_WHITESPACE +NO_EXE
#doctest_mark_exe()
dot.render('doctest-output/round-table.gv', view=True)  # doctest: +SKIP
print(dist)

graph = {node:[] for node in DAG}
for node in DAG:
    for neighbor in DAG[node]["outgoing"]:
        graph[node].append(neighbor)
    for neighbor in DAG[node]["incoming"]:
        graph[node].append(neighbor)

dot = graphviz.Graph(comment='Garden')
dot  #doctest: +ELLIPSIS
for i, junction in enumerate(top_order):
    dot.node(str(i),str(junction)) # doctest: +NO_EXE
for node in DAG:
    for neighbor in DAG[node]["outgoing"]:
        dot.edge(str(top_order.index(node)),str(top_order.index(neighbor[0])),label=str(neighbor[1]))
print(dot.source) # doctest: +NORMALIZE_WHITESPACE +NO_EXE
#doctest_mark_exe()
dot.render('doctest-output/round-table.gv', view=True)

visited = set()
max_length = [0]
longest_path = [[start]]
path_length = 0
dfsLongestPath(graph,start,finish)






    
                
  
