
with open("day16input.txt") as file:
    data = file.read().splitlines()
height = len(data)
width = len(data[0])
startsDown = [[[0,y],"down"] for y in range(width)]
startsRight = [[[y,0],"right"] for y in range(height)]
startsLeft = [[[y,width-1],"left"] for y in range(height)]
startsUp = [[[height-1,y],"up"] for y in range(width)]
starts =startsRight + startsDown + startsLeft + startsUp
energizedCounts=[]
tall=0
for start in starts:
    pos=start[0]
    direction=start[1]
    otherGrid =[["." for _ in range(width)] for _ in range(height)]
    beam = [pos,direction]
    beams=[beam]
    previousBeams=[]
    t=0
    while len(beams)>0:
        while pos[0]>=0 and pos[0]<len(data) and pos[1]>=0 and pos[1]<len(data[0]):
            if [pos,direction] in previousBeams:
                break
            previousBeams.append([pos.copy(),direction])
            currPos=data[pos[0]][pos[1]]
            if data[pos[0]][pos[1]]==".":
                otherGrid[pos[0]][pos[1]]="*"
                if direction=="right":
                    pos[1]+=1
                elif direction=="left":
                    pos[1]-=1
                elif direction=="up":
                    pos[0]-=1
                elif direction=="down":
                    pos[0]+=1
                
                
            elif data[pos[0]][pos[1]]=="/":
                otherGrid[pos[0]][pos[1]]="*"
                if direction=="right":
                    direction="up"
                    pos[0]-=1
                elif direction=="left":
                    direction="down"
                    pos[0]+=1
                elif direction=="up":
                    direction="right"
                    pos[1]+=1
                elif direction=="down":
                    direction="left"
                    pos[1]-=1
                
                
            elif data[pos[0]][pos[1]]=="\\":
                otherGrid[pos[0]][pos[1]]="*"
                if direction=="right":
                    direction="down"
                    pos[0]+=1
                elif direction=="left":
                    direction="up"
                    pos[0]-=1
                elif direction=="up":
                    direction="left"
                    pos[1]-=1
                elif direction=="down":
                    direction="right"
                    pos[1]+=1
                
                
            elif data[pos[0]][pos[1]]=="-":
                otherGrid[pos[0]][pos[1]]="*"
                if direction=="right":
                    pos[1]+=1
                elif direction=="left":
                    pos[1]-=1
                elif direction=="up" or direction=="down":
                    newPos=[pos[0],pos[1]+1]
                    newDirection="right"
                    newBeam=[newPos,newDirection]
                    beams.append(newBeam)
                    direction="left"
                    pos[1]-=1
                
                
            elif data[pos[0]][pos[1]]=="|":
                otherGrid[pos[0]][pos[1]]="*"
                if direction=="up":
                    pos[0]-=1
                elif direction=="down":
                    pos[0]+=1
                elif direction=="left" or direction=="right":
                    newPos=[pos[0]+1,pos[1]]
                    newDirection="down"
                    newBeam=[newPos,newDirection]
                    beams.append(newBeam)
                    direction="up"
                    pos[0]-=1
                
            t+=1
            
        beams=beams[1:]
        if len(beams)>0:
            pos=beams[0][0]
            direction=beams[0][1]
    countEnergized=0
    for row in otherGrid:
        countEnergized+=row.count("*")
        #print(row)
    print(countEnergized)
    energizedCounts.append(countEnergized)
    tall+=1
    print(tall)
print(max(energizedCounts))           
#7831