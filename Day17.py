import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFont
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
    

    # Priority queue
    queue = [(0, (0, 0,-1,0))]
    passed=set()
    while queue:
        dist, (row, col,direction,step_count) = heapq.heappop(queue)

        # Stop if we reach the destination
        if (row, col) == dest:
            print(dist)
            break
        if (row, col,direction,step_count) in passed:
            continue
        passed.add((row, col,direction,step_count))
        for i,(dr, dc) in enumerate(directions):
            if i == (direction + 2) % 4:  # Avoid backtracking
                continue
            r, c = row + dr, col + dc
            if 0 <= r < rows and 0 <= c < cols:
                new_step_count = step_count + 1 if i == direction else 1
                if new_step_count<=max_steps:
                    new_dist = dist + grid[r][c]
                    new_node = (r, c,i,new_step_count)
                    heapq.heappush(queue, (new_dist, new_node))
   
    return dist
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
def create_annotated_path_image(grid, path):
    nrows, ncols = len(grid), len(grid[0])
    cell_size = 50  # Adjust cell size as needed
    img = Image.new('RGB', (ncols * cell_size, nrows * cell_size), color='white')
    draw = ImageDraw.Draw(img)

    # Use a default font, or replace with a specific font if available
    font = ImageFont.load_default()

    for i in range(nrows):
        for j in range(ncols):
            x, y = j * cell_size, i * cell_size
            text = grid[i][j]
            w, h = draw.textsize(text, font=font)

            # Check if the current position is part of the path
            if path[i][j] not in {'*', ' '}:
                draw.rectangle([x, y, x + cell_size, y + cell_size], fill='lightblue')

            # Draw the text in the center of the cell
            text_x = x + (cell_size - w) / 2
            text_y = y + (cell_size - h) / 2
            draw.text((text_x, text_y), text, fill='black', font=font)

    # Display the image
    plt.imshow(img)
    plt.axis('off')
    plt.show()
            
# Your grid

with open('day17input.txt') as f:
    grid = [[int(x) for x in line.strip()] for line in f]
# Find the shortest path and its cost
shortest_path_cost= dijkstra(grid,3)
print("Shortest path cost:", shortest_path_cost)


