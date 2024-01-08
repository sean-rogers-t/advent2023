from collections import deque

def printGrid(grid):
    for row in grid:
        print("".join(row))
    print()



# Read the grid from file
with open('day21input.txt') as f:
    grid = [list(line.strip()) for line in f]

# Find starting point 'S'
start = next((r, c) for r, row in enumerate(grid) for c, val in enumerate(row) if val == 'S')
path_length = 64
queue = deque([(start, path_length)])
seen  = set()
seen.add(start)
end_points=set()
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
rows, cols = len(grid), len(grid[0])
while queue:
    (row, col), length = queue.popleft()
    if length % 2==0:
        end_points.add((row,col))

    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < rows and 0 <= c < cols and grid[r][c] != '#' and (r,c) not in seen and length>0: #  and (r, c) not in visited
            seen.add((r, c))
            queue.append(((r, c), length - 1))

#print("End points of all paths of length 6 starting at 'S':", end_points)
print("Number of paths of length 6 starting at 'S':", len(end_points))