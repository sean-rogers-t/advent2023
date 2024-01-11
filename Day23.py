# seems similiar to Day17
import numpy as np
import heapq

def dfs(junctions,beginning,grid, graph, start,finish,direction = None):
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
            if [node,distance] in graph[currentNode]["outgoing"] or [currentNode,distance] in graph[node]["incoming"]:
                continue
            graph[node]["incoming"].append([currentNode,distance])
            graph[currentNode]["outgoing"].append([node,distance])
            if node == finish:
                return dfs(junctions,node,grid,graph,start,finish)
            
            stack=[]
            visited=set()
            distance=0
            for dr,dc in directions:
                r,c = node[0]+dr,node[1]+dc
                if 0<r<len(grid) and  0<c<len(grid[0]) and grid[r][c] in arrows and badDirection[grid[r][c]] !=(dr,dc):  
                    dfs(junctions,node,grid,graph,start,finish,(dr,dc))
        else:
            for dr,dc in directions:
                r,c = node[0]+dr,node[1]+dc
                if (r,c) not in visited and grid[r][c] != "#" and (grid[r][c] == "." or badDirection[grid[r][c]] !=(dr,dc)):  
                    visited.add((r,c))
                    stack.append((r,c))
                    distance+=1

# find shortest path
def topologicalSort(graph):
    # List to store the topological order
    top_order = []

    # Dictionary to keep track of the number of incoming edges for each node
    incoming_edges_count = {node: len(graph[node]["incoming"]) for node in graph}

    # Initialize a queue with nodes having no incoming edges
    queue = [node for node, count in incoming_edges_count.items() if count == 0]
    queue = [[node,0] for node in queue]
    while queue:
        # Take one node with no incoming edges
        node = queue.pop(0)
        
        top_order.append(node[0])

        # Decrease the count of incoming edges for all neighbors
        for neighbor in graph[node[0]]["outgoing"]:
            incoming_edges_count[neighbor[0]] -= 1
            # If a neighbor has no more incoming edges, add it to the queue
            if incoming_edges_count[neighbor[0]] == 0:
                queue.append(neighbor)

    # Check for a cycle (if there are nodes with incoming edges left)
    if len(top_order) != len(graph):
        raise Exception("Graph has at least one cycle")

    return top_order
def longestPathDAG(graph, source, sink):
    top_order = topologicalSort(graph)
    distance = {node: -float("inf") for node in graph}

    distance[source] = 0

    for vertex in top_order:
        for neighbor in graph[vertex]["outgoing"]:
            edge_weight = neighbor[1]
            if distance[neighbor[0]] < distance[vertex] + edge_weight:
                distance[neighbor[0]] = distance[vertex] + edge_weight

    return distance[sink]

with open("day23input.txt") as f:
    grid =  [line.strip() for line in f.readlines()]
start = (0,grid[0].index('.'))
finish = (len(grid)-1,grid[-1].index('.'))

visited = set()
max_length = [0]
longest_path = [[]]
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

graph = {node:{"incoming":[],"outgoing":[]} for node in junctions}


dfs(junctions,start,grid,graph, start, finish)


dist = longestPathDAG(graph,start,finish)
print(dist)


    
                
  
