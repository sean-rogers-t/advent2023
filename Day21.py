from collections import deque

def printGrid(grid):
    for row in grid:
        print("".join(row))
    print()


def bfs(grid, start, path_length):
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
    return end_points


with open('day21input.txt') as f:
        input = [line.strip() for line in f]
assert len(input) == len(input[0])
print(f"The solution to part 1 is {len(bfs(input, (65, 65), 64))}")

# Part 2
# note that 26501365 = 202300 * 131 + 65
# solve the first few problems with pathlength i*131+65
# Use solution from Day 9 to find recurrence relation
# You'll find that a_n-3a_{n-1}+3s_{n-2}+a_{n-3}=0
# with initial conditions  a_0 =3738, a_1=33270, a_2=92194
# this recurrence can be solved a_n=14696*x^2+14836*x+3738
# then a_202300 = 601441063166538
dim=len(input)
S=dim//2
answers=[]

for i in range(4):
    path_length = S+dim*i
    expansion = 1+2*i
    
    grid = [list(line.strip()*expansion) for line in input]*expansion
    
    start = (path_length, path_length)
    
    end_points=bfs(grid, start, path_length)
    answers.append(len(end_points))
    
print(answers)

nextNumbers=[]
start=answers
lastNumber=[]
while any(start):
    lastNumber.append(start[-1])
    nextSequence=[]
    for i in range(len(start)-1):
        nextSequence.append(start[i+1]-start[i])
    start=nextSequence
nextNumbers.append(sum(lastNumber))
#firstNumber=firstNumber[::-1]
print(nextNumbers)

#print("End points of all paths of length 6 starting at 'S':", end_points)
