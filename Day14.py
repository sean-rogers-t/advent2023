def EvaluateLoad(grid):
    sum=0
    for i,row in enumerate(grid):
        for cell in row:
            if cell=="O":
                sum+=len(grid)-i
    return sum
def TransposeGrid(grid):
    transposedGrid = ["".join([row[i] for row in grid]) for i in range(len(grid[0]))]
    return transposedGrid
def ReflectGrid(grid):
    return [row[::-1] for row in grid]
def FlipGrid(grid):
    return grid[::-1]
def TiltGridWest(grid):
    for i,row in enumerate(grid):
        buckets = row.split("#")
        for j,bucket in enumerate(buckets):
            countStone = bucket.count("O")
            buckets[j] = "O"*countStone + "."*(len(bucket)-countStone)
        grid[i] = "#".join(buckets)
    return grid


with open("day14input.txt") as file:
    grid = file.read().splitlines()
grids=[grid]
#north,west,south,east
print(EvaluateLoad(grid))
for i in range(1000000000):
    #north
    grid=TransposeGrid(grid)
    grid=TiltGridWest(grid)
    grid=TransposeGrid(grid)
    #west
    grid=TiltGridWest(grid)
    #south
    grid=FlipGrid(TransposeGrid(TiltGridWest(TransposeGrid(FlipGrid(grid)))))
    #east
    grid=ReflectGrid(TiltGridWest(ReflectGrid(grid)))
    if grid not in grids:
        grids.append(grid)
        
        print(EvaluateLoad(grid))
        if i%100000==0:
            print(i)
        x=5
    else:
        print(EvaluateLoad(grid))
        print(i)
        print(grids.index(grid))
        print(i-grids.index(grid))
        start=grids.index(grid)
        numGrids=i-grids.index(grid)+1
        finalGrids=grids[:-1*numGrids]
        
        break


    
print(EvaluateLoad(grids[(1000000000-start)%numGrids+start]))


