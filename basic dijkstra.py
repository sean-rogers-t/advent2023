import numpy as np
import heapq
def generate_key_sequence(dictionary, start_key, max_length=1000):
    """
    Generates a sequence of keys by repeatedly applying the dictionary to its values.

    :param dictionary: The dictionary to use for generating the sequence.
    :param start_key: The initial key to start from.
    :param max_length: The maximum length of the sequence to prevent infinite loops.
    :return: A list containing the sequence of keys.
    """
    sequence = [start_key]
    current_key = start_key

    for _ in range(max_length):
        if current_key not in dictionary:
            break  # Stop if the current key is not in the dictionary

        current_key = dictionary[current_key]
        sequence.append(current_key)

        if current_key == start_key:
            break  # Stop if the sequence has looped back to the start

    return sequence
def dijkstra(grid):
    rows, cols = len(grid), len(grid[0])
    dest = (rows - 1, cols - 1)

    # Directions: up, down, left, right
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Initialize distances and predecessors
    distances = {(row, col): float('inf') for row in range(rows) for col in range(cols)}
    distances[(0, 0)] = 0
    predecessors = {}

    # Priority queue
    queue = [(0, (0, 0))]

    while queue:
        dist, (row, col) = heapq.heappop(queue)

        # Stop if we reach the destination
        if (row, col) == dest:
            break

        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < rows and 0 <= c < cols:
                new_dist = dist + grid[r][c]
                if new_dist < distances[(r, c)]:
                    distances[(r, c)] = new_dist
                    predecessors[(r, c)] = (row, col)
                    heapq.heappush(queue, (new_dist, (r, c)))

    # Reconstruct the shortest path
    path = []
    current = dest
    while current != (0, 0):
        path.append(current)
        current = predecessors[current]
    path.append((0, 0))
    path.reverse()
    print_grid(path,grid)
    return distances[dest], path
def print_grid(path, grid):
    directionDict = {0: '>', 1: 'v', 2: '<', 3: '^',-1: 'S'}
    rows, cols = len(grid), len(grid[0])
    gridpath= [['*'] * cols for _ in range(rows)]
    for stop in path:
        gridpath[stop[0]][stop[1]] = "-"
    for row in gridpath:
        print(''.join(row))
# Your grid
""" grid = [
    [2, 4, 7, 8, 2, 9, 3, 3],
    [6, 4, 7, 5, 8, 3, 9, 2],
    [8, 4, 9, 3, 8, 4, 5, 9],
    [2, 8, 4, 9, 3, 5, 8, 3]
] """
with open('day17input.txt') as f:
    grid = [[int(x) for x in line.strip()] for line in f]
# Find the shortest path and its cost
shortest_path_cost, shortest_path = dijkstra(grid)
print("Shortest path cost:", shortest_path_cost)
