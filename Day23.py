# seems similiar to Day17
import numpy as np
import heapq

def dijkstra(start,finish,grid):
    rows, cols = len(grid), len(grid[0])
    dest = (rows - 1, cols - 1)

    # Directions: up, down, left, right
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    arrows =[">","v","<","^"]
    # Initialize distances and predecessors
    distances = {(row, col): 0 for row in range(rows) for col in range(cols)}
    
    predecessors = {}
    #queue = [(distance, node,necessary_next_move = (0,0))]
    # Priority queue
    queue = [(0, start,())]

    while queue:
        dist, (row, col),nextMove = heapq.heappop(queue)

        # Stop if we reach the destination
        if (row, col) == dest:
            break
        if nextMove:
            r,c=row + nextMove[0], col + nextMove[1]
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] != '#':
                new_dist = dist + 1
                if new_dist < distances[(r, c)]:
                    distances[(r, c)] = new_dist
                    predecessors[(r, c)] = (row, col)
                    heapq.heappush(queue, (new_dist, (r, c),()))
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] != '#':
                new_dist = dist + 1
                if new_dist > distances[(r, c)]:
                    distances[(r, c)] = new_dist
                    predecessors[(r, c)] = (row, col)
                    if grid[r][c] == '.':
                        heapq.heappush(queue, (new_dist, (r, c),()))
                    else:
                        arrowIndex = arrows.index(grid[r][c])
                        heapq.heappush(queue, (new_dist, (r, c),directions[arrowIndex]))
            
# Your grid
directions = {'>': (0, 1), 'v': (1, 0), '<': (0, -1), '^': (-1, 0)}

def dfs(grid, x, y, visited, path_length, max_length, destination):
    if (x, y) == destination:
        max_length[0] = max(max_length[0], path_length)
        return

    visited.add((x, y))

    # If current cell has an arrow, you must follow it
    if grid[x][y] in directions:
        dx, dy = directions[grid[x][y]]
        nx, ny = x + dx, y + dy
        if is_valid_move(grid, nx, ny, visited):
            dfs(grid, nx, ny, visited, path_length + 1, max_length, destination)
    else:
        for dx, dy in directions.values():
            nx, ny = x + dx, y + dy
            if is_valid_move(grid, nx, ny, visited):
                dfs(grid, nx, ny, visited, path_length + 1, max_length, destination)

    visited.remove((x, y))

def is_valid_move(grid, nx, ny, visited):
    rows, cols = len(grid), len(grid[0])
    return 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] != "#"



with open("day23input.txt") as f:
    lines =  [line.strip() for line in f.readlines()]
start = (0,lines[0].index('.'))
finish = (len(lines)-1,lines[-1].index('.'))

visited = set()
max_length = [0]
longest_path = [[]]
dfs(lines, start[0], start[1], visited, 0, max_length, finish)

print("Longest path length:", max_length[0])