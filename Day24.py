import sympy
with open("day24input.txt") as f:
    hail =  [[list(map(int,part.split(","))) for part in line.strip().split("@")] for line in f.readlines()]



def intersection(point1,derivative1, point2,derivative2):
    x1,y1 = point1
    x2,y2 = point2
    slope1 = derivative1[1]/derivative1[0]
    slope2 = derivative2[1]/derivative2[0]
    x = (slope1*x1-slope2*x2+y2-y1)/(slope1-slope2)
    y=slope1*x-slope1*x1+y1
    t1 = (x-x1)/derivative1[0]
    t2 = (x-x2)/derivative2[0]
    return (x,y,t1,t2)
count = 0
min = 200000000000000
max = 400000000000000
# pt1
for i, stone1 in enumerate(hail[:-1]):
    for j, stone2 in enumerate(hail[i+1:]):
    
        point1 = stone1[0][:2]
        derivative1 =  stone1[1][0:2]
        point2 = stone2[0][:2]
        derivative2 = stone2[1][0:2]
        if point1 == point2:
            continue
        if derivative1[1]/derivative1[0] == derivative2[1]/derivative2[0]:
            continue
        x,y,t1,t2 = intersection(point1,derivative1, point2,derivative2)
        if min<x<max and min<y<max and t1>0 and t2>0:
            count += 1
            #hmm
            
print(count)
        
#pt2
xr,yr,zr,vxr,vyr,vzr = sympy.symbols("xr yr zr vxr vyr vzr")
kinetic_equations = []
i=0
for stone in hail:
    x,y,z = stone[0]
    vx,vy,vz = stone[1]
    kinetic_equations.append((vyr-vy)*(x-xr)-(vxr-vx)*(y-yr))
    kinetic_equations.append((vzr-vz)*(x-xr)-(vxr-vx)*(z-zr))
    i=i+1
    if i>6:
        break
godRock = sympy.solve(kinetic_equations)
print(godRock)
print(godRock[0][xr]+godRock[0][yr]+godRock[0][zr])

    

