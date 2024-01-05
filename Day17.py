import numpy as np
import heapq

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

    return distances[dest], path

# Your grid
grid = [
    [2, 4, 7, 8, 2, 9, 3, 3],
    [6, 4, 7, 5, 8, 3, 9, 2],
    [8, 4, 9, 3, 8, 4, 5, 9],
    [2, 8, 4, 9, 3, 5, 8, 3]
]

# Find the shortest path and its cost
shortest_path_cost, shortest_path = dijkstra(grid)
print("Shortest path cost:", shortest_path_cost)
print("Shortest path:", shortest_path)

