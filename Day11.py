with open("day11input.txt", "r") as file:
    lines = file.readlines()
lines=[line.strip() for line in lines]

grid=[]
for line in lines:
    grid.append(list(line))
#expand universe
colsToExpand=[]
for col in range(len(grid[0])):
    if "#" not in [row[col] for row in grid]:
        colsToExpand.append(col)

colsToExpand = sorted(colsToExpand)  # Sort colsToExpand
columns_added = 0  # Counter for the number of columns added

for col in colsToExpand:
    adjusted_col = col + columns_added
    for row in grid:
        row.insert(adjusted_col, ".")
    columns_added += 1  # Increment counte

rowsToExpand=[]
for i,row in enumerate(grid):
    if "#" not in row:
        rowsToExpand.append(i)
blankRow=["." for _ in range(len(grid[0]))]

for i,row in enumerate(rowsToExpand):
    grid.insert(row+i,blankRow)

coordinates=[]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]=="#":
            coordinates.append((i,j))
pairs=[]
for i in range(len(coordinates)):
    for j in range(i+1,len(coordinates)):
        pairs.append((coordinates[i],coordinates[j]))
print(len(pairs))
distances=[]
for pair in pairs:
    distances.append(abs(pair[0][0]-pair[1][0])+abs(pair[0][1]-pair[1][1]))

totalDistanceSum=sum(distances)
print(totalDistanceSum)




