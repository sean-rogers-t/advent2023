def find_longest_path(graph, source, sink):
    # Stack will store tuples of (current node, cumulative weight, path)
    stack = [(source, 0, [source])]
    longest_path = (0, [])  # (length, path)

    while stack:
        current_node, current_weight, path = stack.pop()

        if current_node == sink:
            if current_weight > longest_path[0]:
                longest_path = (current_weight, path)
            continue

        for neighbor, weight in graph.get(current_node, []):
            if (current_node, neighbor) not in path:  # Avoid revisiting edges
                new_weight = current_weight + weight
                new_path = path + [(current_node, neighbor)]
                stack.append((neighbor, new_weight, new_path))

    return longest_path

# Example graph
graph = {
    'start': [('A', 5)],
    'A': [('B', 3), ('E', 4)],
    'B': [('C', 2)],
    'C': [('D', 1), ('G', 4)],
    'D': [('F', 1)],
    'E': [('F', 6)],
    'F': [('H', 7)],
    'G': [('J', 2)],
    'H': [('J', 4)],
    'J': [('Sink', 3)]
}

longest_path_length, longest_path = find_longest_path(graph, 'start', 'Sink')
print("Longest path length:", longest_path_length)
print("Longest path:", longest_path)
