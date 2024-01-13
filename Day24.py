with open("day24example.txt") as f:
    hail =  [[list(map(int,part.split(","))) for part in line.strip().split("@")] for line in f.readlines()]

x=5
''' y-y1=m1(x-x1) -> y=m1*x-m1*x1+y1
    m1*x-m1*x1+y1 = m2*x-m2*x2+y2
    (m1-m2)*x = m1*x1-m1*x2+y2-y1)
    x = (m1*x1-m1*x2+y2-y1)/(m1-m2)
    y = m1*(m1*x1-m1*x2+y2-y1)/(m1-m2)-m1*x1+y1'''
def intersection(point1,slope1, point2,slope2):
    x = (slope1*point1[0]-slope1*point2[0]+point2[1]-point1[1])/(slope1-slope2)
    y = slope1*(slope1*point1[0]-slope1*point2[0]+point2[1]-point1[1])/(slope1-slope2)-slope1*point1[0]+point1[1]
    return (x,y)
count = 0
for i, stone1 in enumerate(hail[:-1]):
    for j, stone2 in enumerate(hail[i+1:]):
        point1 = stone1[0][:2]
        slope1 = stone1[1][1]/stone1[1][0]
        point2 = stone2[0][:2]
        slope2 = stone2[1][1]/stone2[1][0]
        if slope1 == slope2:
            continue
        x,y = intersection(point1,slope1, point2,slope2)
        if 7<x<27 and 7<y<27:
            count += 1
            #hmm
            
print(count)
        

    

