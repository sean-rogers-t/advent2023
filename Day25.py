from graphviz import Graph
def visualize_graph_with_graphviz(adjacency_matrix, index_to_node):
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

    # Add nodes with labels from index_to_node mapping
    for i in range(len(components)):
        node_label = components[i].join(",")
        if not isEmpty(adjacency_matrix, i):
            g.node(node_label)

    # Add weighted edges based on the adjacency matrix
    for i in range(len(adjacency_matrix)):
        for j in range(i+1, len(adjacency_matrix)):
            if adjacency_matrix[i][j] > 0:  # Check for an edge
                edge_label = str(adjacency_matrix[i][j])
                g.edge(f"{i}", f"{j}", label=edge_label)

    # Render and view the graph
    g.view()
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

def min_cut_phase(adjacency,start=[0]):
    sequence = start
    complement = list(range(0,len(adjacency)))
    complement.remove(start[0])
    while len(complement)>0:
        node = MAS(sequence, complement, adjacency)
        sequence.append(node)
        
        complement.remove(node)
    s , t  = sequence[-2], sequence[-1]
    cut_value = sum(adjacency[t][i] for i in range(len(adjacency)) if i != t)
    x=0

    return sequence, cut_value
def stoer_wagner(adjacency):
    n = len(adjacency)
    min_cut = float('inf') 
    components = [[i] for i in range(n)]
    a=1
    while len(adjacency) > 2:
        sequence, cut_value = min_cut_phase(adjacency,[a])
        min_cut = min(min_cut, cut_value)
        a, b = sequence[-2], sequence[-1]
        min_node = min(a, b)
        max_node = max(a, b)
        # Update components before contracting graph
        components[min_node].extend(components[max_node])
        components.pop(max_node)  # Reflect contraction in components list

        merge_nodes(adjacency, min_node, max_node)
        #visualize_graph_with_graphviz(adjacency)  
        x=0

    # Output the sizes of the two final components
    sizes = [len(component) for component in components]
    return min_cut, sizes
with open("day25example.txt") as f:
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

example  = [[0,2,0,0,3,0,0,0],[2,0,3,0,2,2,0,0],[0,3,0,4,0,0,2,0],[0,0,4,0,0,0,2,2],[3,2,0,0,0,3,0,0],
            [0,2,0,0,3,0,1,0],[0,0,2,2,0,1,0,3],[0,0,0,3,0,0,3,0]]
#visualize_graph_with_graphviz(adjacency,index_to_node)
visualize_graph_with_graphviz(example)
print(stoer_wagner(example))




