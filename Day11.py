#determine how may expansions have happened  up to this coordinate of the given galaxy
def PartitionNumber(num,partition):
    for i in range(len(partition) - 1):
        if partition[i] <= num < partition[i + 1]:
            return i+1
    if num<partition[0]:
        return 0
    if num>=partition[-1]:
        return len(partition)

#read in galactic grid and store as list of lists
with open("day11input.txt", "r") as file:
    lines = file.readlines()
lines=[line.strip() for line in lines]

grid=[]
for line in lines:
    grid.append(list(line))



#find which rows and columns to expand (those without #)
colsToExpand=[]
for col in range(len(grid[0])):
    if "#" not in [row[col] for row in grid]:
        colsToExpand.append(col)

rowsToExpand=[]
for i,row in enumerate(grid):
    if "#" not in row:
        rowsToExpand.append(i)

# Get pre-expansion coordinates for all galaxies
coordinates=[]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]=="#":
            coordinates.append((i,j))
#Hubble Rate
H=999999

# expand coordinates according to the expansion constant

expandedCoordinates=[]

for coordinate in coordinates:
    xPartition= PartitionNumber(coordinate[0],rowsToExpand)
    yPartition= PartitionNumber(coordinate[1],colsToExpand)
    newX = coordinate[0] + H * xPartition
    newY = coordinate[1] + H * yPartition
    expandedCoordinates.append((newX,newY))

# get all pairs of coordinates and the taxicab distance betweern them
pairs=[]
for i in range(len(coordinates)):
    for j in range(i+1,len(coordinates)):
        pairs.append((expandedCoordinates[i], expandedCoordinates[j]))

distances=[]
for pair in pairs:
    distances.append(abs(pair[0][0]-pair[1][0])+abs(pair[0][1]-pair[1][1]))

#sum up distances
totalDistanceSum=sum(distances)
print(totalDistanceSum)





