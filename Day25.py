from graphviz import Graph
def visualize_graph_with_graphviz(adjacency_matrix):
    # Initialize an undirected graph
    g = Graph('G', filename='graph.gv')

    # Add nodes
    for i in range(len(adjacency_matrix)):
        g.node(str(i))

    # Add edges based on the adjacency matrix
    for i in range(len(adjacency_matrix)):
        for j in range(i+1, len(adjacency_matrix)):
            if adjacency_matrix[i][j] > 0:
                g.edge(str(i), str(j))

    # Render and view the graph
    g.view()


def merge_nodes(adjacency, a, b):
    """
    Merge node b into node a and remove node b from the adjacency matrix.
    """
    n = len(adjacency)
    # Update connections for merging nodes
    for i in range(n):
        adjacency[a][i] += adjacency[b][i]
        adjacency[i][a] += adjacency[i][b]
    adjacency[a][a] = 0  # Remove potential self-loop

    # Remove node b from the adjacency matrix
    # Remove b's row
    adjacency.pop(b)
    # Remove b's column
    for i in range(len(adjacency)):
        adjacency[i].pop(b)


def MAS(sequence, complement, adjacency):
    n = len(sequence)
    max_node = -1
    max_adj = 0
    for node in complement:
        adj_num =0 
        for other in sequence:
            if adjacency[node][other]>0:
                adj_num += 1
        if adj_num > max_adj:
            max_adj = adj_num
            max_node = node
    return max_node

def min_cut_phase(adjacency,start=0):
    sequence = [0]
    complement = list(range(1,len(adjacency)))
    while len(complement)>0:
        node = MAS(sequence, complement, adjacency)
        sequence.append(node)
        if node in complement:
            complement.remove(node)
    s , t  = sequence[-2], sequence[-1]
    return sequence, t

def stoer_wagner(adjacency):
    n = len(adjacency)
    components = [[i] for i in range(n)]
    a=0
    while len(adjacency) > 2:
        sequence, _ = min_cut_phase(adjacency,a)
        a, b = sequence[-2], sequence[-1]

        # Update components before contracting graph
        components[a].extend(components[b])
        components.pop(b)  # Reflect contraction in components list

        merge_nodes(adjacency, a, b)
        visualize_graph_with_graphviz(adjacency,index_to_node)  # This now also reduces the adjacency matrix size
        x=0

    # Output the sizes of the two final components
    sizes = [len(component) for component in components]
    return sizes
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

def visualize_graph_with_graphviz(adjacency_matrix,index_to_node):
    # Initialize an undirected graph
    g = Graph('G', filename='graph.gv')

    # Add nodes
    for i in range(len(adjacency_matrix)):
        g.node(str(i) + ", " + index_to_node[i])

    # Add edges based on the adjacency matrix
    for i in range(len(adjacency_matrix)):
        for j in range(i+1, len(adjacency_matrix)):
            if adjacency_matrix[i][j] > 0:
                g.edge(str(i) + ", " + index_to_node[i], str(j) + ", " + index_to_node[j])

    # Render and view the graph
    g.view()

visualize_graph_with_graphviz(adjacency,index_to_node)
print(stoer_wagner(adjacency))




