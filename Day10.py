with open("day10input.txt", "r") as file:
    lines = file.readlines()
grid={}

gridSize=(len(lines),len(lines[0]))
for i in range(len(lines)):
    for j in range(len(lines[i])):
        grid[(i,j)]=lines[i][j]
        if lines[i][j]=="S":
            start=(i,j)

symbols=["S"]

position=[start]
k=0


if (start[0]-1, start[1]) in grid and grid[(start[0]-1, start[1])] in ("|", "F", "7"):
    start = (start[0]-1, start[1])
    lastMove = (-1, 0)
elif (start[0]+1, start[1]) in grid and grid[(start[0]+1, start[1])] in ("|", "L", "J"):
    start = (start[0]+1, start[1])
    lastMove = (1, 0)
elif (start[0], start[1]+1) in grid and grid[(start[0], start[1]+1)] in ("-", "7", "J"):
    start = (start[0], start[1]+1)
    lastMove = (0, 1)
elif (start[0], start[1]-1) in grid and grid[(start[0], start[1]-1)] in ("-", "L", "F"):
    start = (start[0], start[1]-1)
    lastMove = (0, -1)

position.append(start)
symbols.append(grid[start])
k=1

while grid[start]!="S":
    #(1,0)
    if grid[start]=="|":
        if lastMove==(1,0):
            start=(start[0]+1,start[1])
        elif lastMove==(-1,0):
            start=(start[0]-1,start[1])
    elif grid[start]=="-":
        if lastMove==(0,1):
            start=(start[0],start[1]+1)
        elif lastMove==(0,-1):
            start=(start[0],start[1]-1)
    elif grid[start]=="L":
        if lastMove==(0,-1):
            start=(start[0]-1,start[1])
            lastMove=(-1,0)
        elif lastMove==(1,0):
            start=(start[0],start[1]+1)
            lastMove=(0,1)
    elif grid[start]=="7":
        if lastMove==(0,1):
            start=(start[0]+1,start[1])
            lastMove=(1,0)
        elif lastMove==(-1,0):
            start=(start[0],start[1]-1)
            lastMove=(0,-1)
    elif grid[start]=="F":
        if lastMove==(0,-1):
            start=(start[0]+1,start[1])
            lastMove=(1,0)
        elif lastMove==(-1,0):
            start=(start[0],start[1]+1)
            lastMove=(0,1)
    elif grid[start]=="J":
        if lastMove==(0,1):
            start=(start[0]-1,start[1])
            lastMove=(-1,0)
        elif lastMove==(1,0):
            start=(start[0],start[1]-1)
            lastMove=(0,-1)
    k+=1
    
    symbols.append(grid[start])
    position.append(start)
print(symbols)
print(position)
print(k//2+k%2)
symbols=symbols[:-1]
symbols[0]="F"
position=position[:-1]
corners=["J","L","F","7"]
vertices =[position[i] for i in range(len(position)) if symbols[i] in corners]
vertices=[(vertex[1],vertex[0]) for vertex in vertices]
#shoelace formula for area of a polytope
#       A=1/2*Sum(vi v vi+1)
shoelace=0
n = len(vertices)
for i in range(len(vertices)):
    det=vertices[i][0]*vertices[(i+1)%n][1]-vertices[(i+1)%n][0]*vertices[i][1]
    shoelace += det
A=1/2*shoelace
A= -A if A<0 else A
print(A)
#picks formula for area A= i+b/2-1 where i are interior pints and b are boundary points
boundary = len(symbols)
interior=A+1-boundary/2
print(interior)
    




