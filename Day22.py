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


with open('day22input.txt') as file:
    bricks=[[np.array(tuple(map(int, part.split(',')))) for part in line.split('~')] for line in file]
bricks.sort(key=lambda x: x[0][2])
totalRanges=[]
for i in range(3):
    low = min([min(brick[0][i],brick[1][i]) for brick in bricks])
    high = max([max(brick[0][i],brick[1][i]) for brick in bricks])
    totalRanges.append((low,high))
print(totalRanges)

diffs = [brick[1]-brick[0] for brick in bricks]

bottoms = [min(brick[0][2],brick[1][2]) for brick in bricks]

Bricks=[]
BrickDict={}
for i,brick in enumerate(bricks):
    new_brick={"name":chr(65+i),"start":brick[0],"end":brick[1],"bottom":brick[0][2],"top":brick[1][2], "zHeight":diffs[i][2]+1,"supports":[],"supportedBy":[],"totalSupport":[],"pops":[],"base":False}
    Bricks.append(new_brick)


Bricks.sort(key=lambda x: x["bottom"])
brickQueue=Bricks.copy()
BrickDict={brick["name"]:brick for brick in Bricks}

landedBricks=[{"name":"base","start":(0,0,0),"end":(totalRanges[0][1],totalRanges[1][1],0),"bottom":0,"top":0, "zHeight":0,"supports":[],"supportedBy":[],"totalSupport":[],"pops":[],"base":True}]

while brickQueue:
    brick=brickQueue.pop(0)
    for landedBrick in landedBricks:
        x=brick["name"]
        y=landedBrick["name"]
        bottom = brick["bottom"]
        if landedBrick["top"] < bottom-1 and len(brick["supportedBy"])!=0:
            break
        top = landedBrick["top"]
        if intersection((brick["start"],brick["end"]),(landedBrick["start"],landedBrick["end"])):
            brick["supportedBy"].append(landedBrick["name"]) if not landedBrick["base"] else None
            landedBrick["supports"].append(brick["name"])
            brick["bottom"]=top+1
            brick["top"]=top+brick["zHeight"]
    landedBricks.append(brick)
    landedBricks.sort(key=lambda x: x["top"],reverse=True)

landedBricks.sort(key=lambda x: x["top"],reverse=False)
Bricks.sort(key=lambda x: x["top"],reverse=False)
disintegratedBricks=0
for brick in Bricks:
    
    disintegrate=False
    print(f"\nBrick: {brick['name']}, Supports: {brick['supports']}, Supported By: {brick['supportedBy']}")
    if brick["supports"]==[]:
        disintegratedBricks+=1
        disintegrate=True
        #print(f"Disintegrated {brick['name']}, supports nothing")
    else:
        disintegrate=True
        for support in brick["supports"]:
            if len(BrickDict[support]["supportedBy"])<=1:
                disintegrate=False
                brick["totalSupport"].append(support)
                #print(f"Can't disintegrate {brick['name']}, only brick that supports {support}")
                
        if disintegrate:
            disintegratedBricks+=1

            #print(f"Disintegrated {brick['name']}, all bricks supported by have multiple supports")
print(f'{disintegratedBricks} bricks disintegrated')
graph = {brick["name"]:{'name':brick["name"],'supports':brick["supports"],'supportedBy':brick["supportedBy"],'totalSupport':brick["totalSupport"],"pops":brick["pops"]} for brick in Bricks}
bases = [brick for brick in graph.values() if not brick['supportedBy']]

tops = [brick for brick in graph.values() if not brick['supports']]



graphList = [value.copy() for value in graph.values()]

# Manually create deep copies for popGraph
popGraph = {}
for brick in graphList:
    new_brick = brick.copy()  # Shallow copy the dictionary
    new_brick['supports'] = brick['supports'].copy()  # Deep copy the list
    new_brick['supportedBy'] = brick['supportedBy'].copy()
    new_brick["totalSupport"] = brick["totalSupport"].copy()
    new_brick["pops"] = brick["pops"].copy()
     # Deep copy the list
    popGraph[brick['name']] = new_brick

# Rest of your code
for start in graph.values():
    if start["totalSupport"]==[]:
        continue
    queue = [start]
    while queue:
        brick = queue.pop(0)
        for support in brick['supports']:
            popGraph[support]['supportedBy'].remove(brick['name'])
            if not popGraph[support]['supportedBy']:
                queue.append(popGraph[support])
                start["pops"].append(support)
    
    for brick in graphList:
        new_brick = brick.copy()  # Shallow copy the dictionary
        new_brick['supports'] = brick['supports'].copy()  # Deep copy the list
        new_brick['supportedBy'] = brick['supportedBy'].copy()
        new_brick["totalSupport"] = brick["totalSupport"].copy()
        # Deep copy the list
        new_brick["pops"] = brick["pops"].copy()
        popGraph[brick['name']] = new_brick
sum=0
for brick in graph:
    sum+=len(graph[brick]["pops"])
print(sum)

                
            
    

        
            
            





            




                
            
                

    
print()

    
    

