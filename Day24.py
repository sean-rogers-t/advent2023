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
        if 7<x<27 and 7<y<27 and t1>0 and t2>0:
            count += 1
            #hmm
            
print(count)
        

    

