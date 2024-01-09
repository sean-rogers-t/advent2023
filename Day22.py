import numpy as np
def intersection(brick1,brick2=None):
    if brick2 is None:
        return False
    (x1, y1,z1), (x2, y2,z2) = brick1
    (x3, y3,z3), (x4, y4,z4) = brick2

    # Check if the segments are entirely to one side of the other
    if x2 < x3 or x1 > x4:
        return False

    # Check if one segment is entirely above or below the other
    if y2 < y3 or y1 > y4:
        return False

    return True

with open('day22example.txt') as file:
    bricks=[[np.array(tuple(map(int, part.split(',')))) for part in line.split('~')] for line in file]
bricks.sort(key=lambda x: x[0][2])
totalRanges=[]
for i in range(3):
    low = min([min(brick[0][i],brick[1][i]) for brick in bricks])
    high = max([max(brick[0][i],brick[1][i]) for brick in bricks])
    totalRanges.append((low,high))
print(totalRanges)

diffs = [brick[1]-brick[0] for brick in bricks]
brickTypes = []
for brick in bricks:
    for  i in range(3):
        if brick[0][i] != brick[1][i]:
            brickTypes.append(i)
            break
bottoms = [min(brick[0][2],brick[1][2]) for brick in bricks]

Bricks=[]
for i,brick in enumerate(bricks): 
    new_brick={"name":chr(65+i),"start":brick[0],"end":brick[1],"type":brickTypes[i],"bottom":brick[0][2],"top":brick[1][2], "zHeight":diffs[i][2]+1,"supports":[],"supportedBy":[],"base":False}
    Bricks.append(new_brick)



Bricks.sort(key=lambda x: x["bottom"])
brickQueue=Bricks.copy()
landedBricks=[{"name":"base","start":(0,0,0),"end":(totalRanges[0][1],totalRanges[1][1],0),"type":brickTypes[0],"bottom":0,"top":0, "zHeight":0,"supports":[],"supportedBy":[],"base":True}]

while brickQueue:
    brick=brickQueue.pop(0)
    for landedBrick in landedBricks:
        x=brick["name"]
        y=landedBrick["name"]
        bottom = brick["bottom"]
        if landedBrick["top"] < bottom-1 and len(brick["supportedBy"])!=0:
            continue
        top = landedBrick["top"]
        if intersection((brick["start"],brick["end"]),(landedBrick["start"],landedBrick["end"])):
            brick["supportedBy"].append(landedBrick["name"]) if not landedBrick["base"] else None
            landedBrick["supports"].append(brick["name"])
            brick["bottom"]=top+1
            brick["top"]=top+brick["zHeight"]
    landedBricks.append(brick)
    landedBricks.sort(key=lambda x: x["top"],reverse=True)

landedBricks.sort(key=lambda x: x["top"],reverse=False)
disintegratedBricks=0
for brick in landedBricks:
    print(f"Brick: {brick['name']}, Supports: {brick['supports']}, Supported By: {brick['supportedBy']}")
    if brick["supports"]==[]:
        disintegratedBricks+=1
    
print()

    
    

