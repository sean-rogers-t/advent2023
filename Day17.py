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



def dijkstra(grid,max_steps):
    rows, cols = len(grid), len(grid[0])
    dest = (rows - 1, cols - 1)

    # Directions: up, down, left, right
    # Directions: right (0), down (1), left (2), up (3)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Initialize distances and predecessors
    distances = {(row, col,d,s): float('inf') for row in range(rows) for col in range(cols) for d in range(4) for s in range(max_steps+1)}
    distances[(0, 0,-1,0)] = 0
    predecessors = {}

    # Priority queue
    queue = [(0, (0, 0,-1,0))]

    while queue:
        dist, (row, col,direction,step_count) = heapq.heappop(queue)

        # Stop if we reach the destination
        if (row, col) == dest:
            break

        for i,(dr, dc) in enumerate(directions):
            if i == (direction + 2) % 4:  # Avoid backtracking
                continue
            r, c = row + dr, col + dc
            if 0 <= r < rows and 0 <= c < cols:
                new_step_count = step_count + 1 if i == direction else 1
                if new_step_count<=max_steps:
                    new_dist = dist + grid[r][c]
                    new_node = (r, c,i,new_step_count)
                    if new_dist < distances[(r, c,i,new_step_count)]:
                        distances[new_node] = new_dist
                        predecessors[new_node] = (row, col,direction,step_count)
                        heapq.heappush(queue, (new_dist, new_node))
        
    possiblePaths =[(key,value) for key,value in distances.items() if key[0]==12 and key[1]==12 and value!=float('inf')]
    possiblePaths.sort(key=lambda x:x[1])
    start=possiblePaths[0][0]
    path = generate_key_sequence(predecessors, start)
    print_grid(path,grid)
    return possiblePaths[0][1]
    # Reconstruct the shortest path
    # Initialize the path
    """ path = []

    # Start from the destination
    current = (dest[0], dest[1], -1, -1)

    # Find the predecessor with the smallest distance that leads to the current node
    # We ignore the direction and step count when looking for the predecessor
    current_distance = min((distances[(current[0], current[1], d, s)], (d, s)) 
                        for d in range(4) for s in range(1, max_steps+1))[1]
    current = (current[0], current[1], current_distance[0], current_distance[1])

    while current[0:2] != (0, 0) or (current[2] != -1 and current[3] != 0):
        path.append(current[0:2])
        current = predecessors[current]

    # Add the start node and reverse the path
    path.append((0, 0))
    path.reverse()

    return distances[(dest[0], dest[1], current[2], current[3])], path """
def print_grid(path, grid):
    directionDict = {0: '>', 1: 'v', 2: '<', 3: '^',-1: 'S'}
    rows, cols = len(grid), len(grid[0])
    gridpath= [['*'] * cols for _ in range(rows)]
    for stop in path:
        gridpath[stop[0]][stop[1]] = directionDict[stop[2]]
    for row in gridpath:
        print(''.join(row))
    
            
# Your grid
grid = [
    [2, 4, 7, 8, 2, 9, 3, 3],
    [6, 4, 7, 5, 8, 3, 9, 2],
    [8, 4, 9, 3, 8, 4, 5, 9],
    [2, 8, 4, 9, 3, 5, 8, 3]
]
with open('day17input.txt') as f:
    grid = [[int(x) for x in line.strip()] for line in f]
# Find the shortest path and its cost
shortest_path_cost= dijkstra(grid,3)
print("Shortest path cost:", shortest_path_cost)


