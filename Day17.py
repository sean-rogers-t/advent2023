
import numpy as np
import heapq


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
            
# Your grid

with open('day17input.txt') as f:
    grid = [[int(x) for x in line.strip()] for line in f]
# Find the shortest path and its cost
shortest_path_cost= dijkstra(grid,3)
print("Shortest path cost:", shortest_path_cost)


