from graphviz import Graph
def visualize_graph_with_graphviz_nodes(adjacency_matrix, index_to_node):
    # Initialize an undirected graph
    g = Graph('G', filename='graph.gv', engine='dot')

    # Add nodes with labels from index_to_node mapping
    for i in range(len(adjacency_matrix)):
        node_label = f"{i} ({index_to_node[i]})"
        if not isEmpty(adjacency_matrix, i):
            g.node(node_label)

    # Add weighted edges based on the adjacency matrix
    for i in range(len(adjacency_matrix)):
        for j in range(i+1, len(adjacency_matrix)):
            if adjacency_matrix[i][j] > 0:  # Check for an edge
                edge_label = str(adjacency_matrix[i][j])
                g.edge(f"{i} ({index_to_node[i]})", f"{j} ({index_to_node[j]})", label=edge_label)

    # Render and view the graph
    g.view()
def visualize_graph_with_graphviz(adjacency_matrix,components):
    # Initialize an undirected graph
    g = Graph('G', filename='graph.gv', engine='dot')
    nodes = []
    # Add nodes with labels from index_to_node mapping
    for i in range(len(components)):
        if len(components[i]) == 0:
            continue
        node_label = ", ".join([str(i) for i in components[i]])
        min_node = components[i][0]
        if not isEmpty(adjacency_matrix, min_node):
            g.node(node_label)
            nodes.append(node_label)

    # Add weighted edges based on the adjacency matrix
    for i in range(len(components)):
        for j in range(i+1, len(components)):
            if len(components[i]) == 0 or len(components[j]) == 0:
                continue
            node_i = components[i][0]
            node_j = components[j][0]
            if adjacency_matrix[node_i][node_j] > 0:  # Check for an edge
                node_label_i = ", ".join([str(i) for i in components[i]])
                node_label_j = ", ".join([str(i) for i in components[j]])
                edge_label = str(adjacency_matrix[node_i][node_j])
                g.edge(node_label_i, node_label_j, label=edge_label)

    # Render and view the graph
    g.view()

def create_graph(vertex_pairs):
    graph = {}
    for pair in vertex_pairs:
        # Unpack the pair into two vertices
        a, b = pair
        # Add each vertex to the graph dictionary if not already present
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        # Add each vertex to the other's adjacency list
        graph[a].append(b)
        graph[b].append(a)
    return graph

def bfs_connected_component_size(graph, start_node):
    # Initialize a set to keep track of visited nodes
    visited = set()
    # Initialize a queue for BFS
    queue = [start_node]
    
    while queue:
        # Dequeue a vertex from the queue
        vertex = queue.pop(0)
        # If not visited, visit the node
        if vertex not in visited:
            visited.add(vertex)
            # Add all unvisited neighbors to the queue
            queue.extend([node for node in graph[vertex] if node not in visited])
    
    # The size of the connected component is the number of visited nodes
    return len(visited)

def isEmpty(adjacency, node):
    """
    Check if a node is isolated in the graph.
    """
    n = len(adjacency)
    for i in range(n):
        if adjacency[node][i] > 0:
            return False
        if adjacency[i][node] > 0:
            return False
    return True

def merge_nodes(adjacency, a, b):
    """
    Merge node b into node a and remove node b from the adjacency matrix.
    """
    n = len(adjacency)
    # Update connections for merging nodes
    for i in range(n):
        adjacency[a][i] += adjacency[b][i]
        adjacency[i][a] += adjacency[i][b]
        adjacency[b][i] = 0  # Remove connections to b
        adjacency[i][b] = 0
    adjacency[a][a] = 0  # Remove potential self-loop

    # Remove node b from the adjacency matrix
    # adjacency.pop(b)
    # for row in adjacency:
    #     row.pop(b)

def MAS(sequence, complement, adjacency):
    n = len(sequence)
    max_node = -1
    max_adj = 0
    for node in complement:
        adj_num =0 
        for other in sequence:
            if adjacency[node][other]>0:
                adj_num += adjacency[node][other]
        if adj_num > max_adj:
            max_adj = adj_num
            max_node = node
    return max_node

def min_cut_phase(adjacency,start,components):
    sequence = start
    complement = [components[i][0] for i in range(len(components)) if len(components[i])>0]
    complement.remove(start[0])
    while len(complement)>0:
        node = MAS(sequence, complement, adjacency)
        sequence.append(node)
        
        complement.remove(node)
    s , t  = sequence[-2], sequence[-1]
    cut_value = sum(adjacency[t][i] for i in range(len(adjacency)) if i != t)
    x=0
    return sequence, cut_value

def stoer_wagner(adjacency,components):
    n = len(adjacency)
    min_cut = float('inf') 
    cuts =[]
    stPairs =[]
    start=1
    component_num = len(list(filter(lambda comp: len(comp) > 0, components)))
    while component_num > 1:
        sequence, cut_value = min_cut_phase(adjacency,[start],components)
        cuts.append(cut_value)
        min_cut = min(min_cut, cut_value)
        s, t = sequence[-2], sequence[-1]
        stPairs.append((s,t))
        start = s
        # Update components before contracting graph
        components[s].extend(components[t])
        
        components[t] =[]  # Reflect contraction in components list

        merge_nodes(adjacency, s, t)
        #visualize_graph_with_graphviz(adjacency,components)
        component_num = len(list(filter(lambda comp: len(comp) > 0, components)))

    # Output the sizes of the two final components
    sizes = [len(component) for component in components if len(component) > 0]
    return min_cut, cuts, stPairs

def find_size(min_cut,cuts,stPairs,n):
    min_cut_idx = cuts.index(min_cut)
    graph  = create_graph(stPairs[:min_cut_idx])
    start = stPairs[min_cut_idx][1]
    size = bfs_connected_component_size(graph,start)
    return size, n-size, size*(n-size)
example  = [[0,2,0,0,3,0,0,0],[2,0,3,0,2,2,0,0],[0,3,0,4,0,0,2,0],[0,0,4,0,0,0,2,2],[3,2,0,0,0,3,0,0],
            [0,2,0,0,3,0,1,0],[0,0,2,2,0,1,0,3],[0,0,0,2,0,0,3,0]]
#components = [[i] for i in range(8)]
#visualize_graph_with_graphviz(adjacency,index_to_node)
# visualize_graph_with_graphviz(example,components)
# mincut,cuts,stPairs = stoer_wagner(example,components)
# print(find_size(mincut,cuts,stPairs))

with open("day25input.txt") as f:
    lines = [line.strip() for line in f.readlines()]


nodes = []
adjacency = []
for line in lines:
    node = line.split(":")[0]
    neighbors = line.split(":")[1].strip().split(" ")
    if node not in nodes:
        nodes.append(node)
    for neighbor in neighbors:
        if neighbor and neighbor not in nodes:
            nodes.append(neighbor)
node_to_index = {node:i for i,node in enumerate(nodes)}
index_to_node = {i:node for node,i in node_to_index.items()}

n=len(nodes)
adjacency = [[0]*n for i in range(n)]

for line in lines:
    parts = line.split(":")
    node = parts[0]
    neighbors = parts[1].split(" ")
    node_idx = node_to_index[node]
    for neighbor in neighbors:
        if neighbor:  # Check to prevent errors from empty strings
            neighbor_idx = node_to_index[neighbor]
            adjacency[node_idx][neighbor_idx] = 1
            adjacency[neighbor_idx][node_idx] = 1

components = [[i] for i in range(n)]
visualize_graph_with_graphviz(adjacency,components)
mincut,cuts,stPairs = stoer_wagner(adjacency,components)
print(find_size(mincut,cuts,stPairs,n))



