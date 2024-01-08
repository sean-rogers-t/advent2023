from collections import deque

def printGrid(grid):
    for row in grid:
        print("".join(row))
    print()

def bfs_paths(grid, starts, current_length, path_length):
    if current_length == path_length:
        return (starts, len(starts))
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Up, right, down, left
    visited = set()
    queue = deque([(start, current_length) for start in starts])  # Queue of (position, current path length)
    paths_end_points = []

    while queue:
        (row, col), length = queue.popleft()
        if length == current_length + 1:
            if (row, col) not in paths_end_points:
                paths_end_points.append((row, col))
            continue

        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] != '#': #  and (r, c) not in visited
                visited.add((r, c))
                queue.append(((r, c), length + 1))

    return bfs_paths(grid, paths_end_points, current_length + 1, path_length)

# Read the grid from file
with open('day21input.txt') as f:
    grid = [list(line.strip()) for line in f]

# Find starting point 'S'
start = next((r, c) for r, row in enumerate(grid) for c, val in enumerate(row) if val == 'S')

# Find all end points of paths of length 6 starting at 'S'
end_points, solution= bfs_paths(grid, [start],0,64)
#print("End points of all paths of length 6 starting at 'S':", end_points)
print("Number of paths of length 6 starting at 'S':", solution)
